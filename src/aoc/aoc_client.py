import json
import sys
import logging
from datetime import datetime

import requests
import browser_cookie3 as browser_cookie

from termcolor import colored
from src.aoc.lxml_utils import HTMLHelper
from src.common.checker import InputCheck
from src.common.configs import BaseConfig
from src.common.utils import SolverFunctions
from src.common.setup_project import SetupProject
from typing import ClassVar
from src.common.configs import (
    CONFIG,
    DEFAULT_BROWSER,
    DEFAULT_BROWSER_HEADER,
    GITHUB_HEADER_NAME,
    DOMAIN_NAME,
    BROWSER_OPTIONS,
)


logger = logging.getLogger(__name__)


class AdventOfCodeBase:
    html_parser = HTMLHelper
    base_config = BaseConfig
    solver_functions = SolverFunctions

    urls: ClassVar[dict[str, str]] = {
        'base_url': 'https://adventofcode.com/{year}/day/{day}',
        'input_url': 'https://adventofcode.com/{year}/day/{day}/input',
        'log_in_github': 'https://adventofcode.com/{}/auth/github',
        'aoc_answer': 'https://adventofcode.com/{year}/day/{day}/answer',
        'aoc_owner': 'https://adventofcode.com/settings',
    }

    @classmethod
    def get_story_input(cls, year, day):
        long_year = f'20{year}'
        request_day = day[1:] if day.startswith('0') else day
        url = cls.urls['input_url'].format(year=long_year, day=request_day)
        return cls.get_content(url)

    @classmethod
    def get_content(cls, url, data=None, method='GET', selector=None):
        response = cls.make_request(method=method, url=url, data=data)
        logger.info(colored(f'AoC url request: {url}', 'green', 'on_black'))
        if selector:
            return cls.html_parser.get_data_from_html_selector(response.content, selector=selector)
        return cls.html_parser.get_data_from_html(response.content)

    @classmethod
    def make_request(cls, method, url, data=None):
        cookies = {
            'session': cls.get_token(),
        }
        response = requests.request(method=method, url=url, cookies=cookies, data=data)

        if response.status_code == 200:
            content = cls.html_parser.get_data_from_html(response.content)

            if 'To play, please identify yourself via one of these services' in content:
                cls.base_config.delete_file('.config.cfg')
                return None

        if response.status_code == 400:
            cls.base_config.clear_cached_token(
                cfg_name=CONFIG,
                header_name=GITHUB_HEADER_NAME,
                field_name=DEFAULT_BROWSER,
            )
            logger.info(colored('Cache was cleared! Run again!', 'yellow', 'on_black'))
            sys.exit()

        response.raise_for_status()

        return response

    @classmethod
    def get_token(cls):
        token = cls.get_github_token()
        if not token:
            raise NotImplementedError

        return token

    @classmethod
    def get_github_token(cls):
        browser_choice = cls.base_config.get_or_create_config_value(
            cfg_name=CONFIG,
            header_name=DEFAULT_BROWSER_HEADER,
            field_name=DEFAULT_BROWSER,
            force=False,
        )
        if browser_choice:
            logger.info(colored('Cached cookies returned for AoC!', 'green', 'on_black'))
            return cls.base_config.get_or_create_config_value(
                cfg_name=CONFIG,
                header_name=GITHUB_HEADER_NAME,
                field_name=BROWSER_OPTIONS[browser_choice],
            )

        if not browser_choice:
            choice = str(InputCheck.get_browser_preference())
            cls.base_config.get_or_create_config_value(
                cfg_name=CONFIG,
                header_name=DEFAULT_BROWSER_HEADER,
                field_name=DEFAULT_BROWSER,
                value=choice,
            )

            token = getattr(AdventOfCodeBase, f'get_{BROWSER_OPTIONS[choice]}_cookies')()
            cls.base_config.get_or_create_config_value(
                cfg_name=CONFIG,
                header_name=GITHUB_HEADER_NAME,
                field_name=BROWSER_OPTIONS[choice],
                value=token,
            )
            logger.info(
                colored(
                    f'AoC cookies from --{BROWSER_OPTIONS[choice]}-- are cached now!',
                    'yellow',
                    'on_black',
                )
            )

            return token

    @staticmethod
    def get_chrome_cookies():
        # using configparser to save cookies as some users may use Windows instead Linux/macOS
        # cookie_file = glob.glob(os.path.expanduser('~/.config/google-chrome/*/Cookies'))
        try:
            chrome_cookies = browser_cookie.chrome(domain_name=DOMAIN_NAME)
            return [c for c in chrome_cookies if c.name == 'session'][0].value
        except IndexError:
            logger.info(colored(f'No cookies in Google Chrome!', 'red', 'on_black'))
            return None

    @classmethod
    def get_firefox_cookies(cls):
        try:
            firefox_cookies = browser_cookie.firefox(domain_name=DOMAIN_NAME)
            if not firefox_cookies:
                firefox_cookies = browser_cookie.firefox(
                    cookie_file=cls.base_config.get_macos_firefox_cookies_custom_user(),
                    domain_name=DOMAIN_NAME,
                )
            return [f for f in firefox_cookies if f.name == "session"][0].value
        except IndexError:
            logger.info(colored('No cookies in Firefox!', 'red', 'on_black'))
            return None

    @staticmethod
    def get_edge_cookies():
        try:
            edge = browser_cookie.edge(domain_name=DOMAIN_NAME)
            edge_cookie = [e for e in edge if e.name == "session"]
            return [c.value for c in edge_cookie][0]
        except IndexError:
            logger.info(colored('No cookies in Microsoft Edge!', 'red', 'on_black'))
            return None

    @classmethod
    def submit_answer(cls, year, day, title, level, answer):
        submitted = False
        star = None
        gold_star = 'gold star'
        message = None
        right_answer = 'the right answer'
        wrong_answer = 'not the right answer'
        too_high = 'too high'
        too_low = 'too low'
        need_to_wait = ['you have to wait after submitting an answer before trying again', 'try again', 'wait']
        submitted_already = "you don't seem to be solving the right level.  did you already complete it?"

        long_year, day = cls.get_long_year_and_day(year, day)
        data = {'level': level, 'answer': answer}
        url = cls.urls['aoc_answer'].format(year=long_year, day=day)

        content = cls.get_content(method='POST', url=url, data=data)

        if content:
            content = content.lower()

            if wrong_answer in content:
                if too_high in content:
                    logger.info(colored(f'{wrong_answer}|{too_high}', 'red', 'on_black'))
                    sys.exit()

                if too_low in content:
                    logger.info(colored(f'{wrong_answer}|{too_low}', 'red', 'on_black'))
                    sys.exit()

            if (right_answer and gold_star) in content:
                star = '**' if level == 2 else '*'
                logger.info(colored(f'{right_answer}', 'green', 'on_black'))

            if submitted_already in content:
                logger.info(colored(f'{submitted_already}', 'green', 'on_black'))

            if any([wrong_answer, right_answer, submitted_already]) != True:
                logger.info(colored('Something went wrong!', 'red', 'on_black'))
                sys.exit()

            for phrase in need_to_wait:
                if phrase in content:
                    logger.info(colored(f'{phrase}', 'magenta', 'on_black'))
                    sys.exit()

        cls.save_answer(long_year, day, title, level, answer, star, submitted, message)

    @classmethod
    def save_answer(cls, long_year, day, title, level, answer, star, submitted, message):
        now = datetime.now()
        json_file = SetupProject.paths_dir['results_file']
        new_data = {
            'year': long_year,
            'day': day,
            'title': title,
            'level': level,
            'answer': str(answer),
            'submitted': submitted,
            'message': message,
            'time': now.strftime('%Y-%m-%d %H:%M:%S'),
            'star ': star,
        }

        try:
            file = cls.solver_functions.reader(json_file)
            data = json.loads(file)
            data.append(new_data)
            json_data = json.dumps(data, indent=4, default=str)
            return cls.solver_functions.file_handler(json_file, json_data, mode='w')

        except json.decoder.JSONDecodeError:
            json_data = json.dumps([new_data], indent=4, default=str)
            return cls.solver_functions.file_handler(json_file, json_data, mode='w')
