import json
import logging
import requests
import browser_cookie3 as browser_cookie

from termcolor import colored
from datetime import datetime

from src.aoc.lxml_utils import HTMLHelper
from src.common.configs import BaseConfig
from src.common.utils import SolverFunctions
from src.common.setup_project import SetupProject


logger = logging.getLogger(__name__)


class AdventOfCodeBase:
    urls = {
        'base_url': 'https://adventofcode.com/{year}/day/{day}',
        'input_url': 'https://adventofcode.com/{year}/day/{day}/input',
        'log_in_github': 'https://adventofcode.com/{}/auth/github',
        'aoc_answer': 'https://adventofcode.com/{year}/day/{day}/answer',
        'aoc_owner': 'https://adventofcode.com/settings'
    }

    @classmethod
    def get_aoc_data(cls, year, day, level):
        year_long = f'20{year}'
        request_day = day[1:] if day.startswith('0') else day

        cls.get_cached_html_story(year, day, year_long, request_day, level)

        return cls.get_cached_html_input(year, day, year_long, request_day, level)

    @classmethod
    def get_cached_html_story(cls, year, day, year_long, request_day, level):
        url = cls.urls['base_url'].format(year=year_long, day=request_day)
        print(f'Request {url=}')
        logger.info(colored('Requesting AoC story!', 'black', 'on_light_yellow'))
        return cls.get_cached_html(year, day, url, level)

    @classmethod
    def get_cached_html_input(cls, year, day, year_long, request_day, level):
        logger.info(colored('Requesting AoC input!', 'black', 'on_light_yellow'))
        url = cls.urls['input_url'].format(year=year_long, day=request_day)
        return cls.get_cached_html(year, day, url, level, need_input=True).text_content()

    @classmethod
    def get_cached_html(cls, year, day, url, level, need_input=False):
        cached_html_directory = SetupProject.paths_dir['cached_html'].format(year=year)
        _day = 'day{day}_{level}'.format(day=day, level=level)
        
        if need_input:
            _day = 'day{day}_input'.format(day=day)

        file_path = f'{cached_html_directory}{_day}.html'

        try:
            with open(file_path, 'r') as file:
                file_response = file.read()
            return HTMLHelper.content_helper(file_response)
        except FileNotFoundError:
            SetupProject.make_dir(cached_html_directory)
            response = cls.make_request(method='GET', url=url)
            
            with open(file_path, 'wb+') as file:
                file.write(response.content)
    
            return HTMLHelper.content_helper(response.content)

    @classmethod
    def make_request(cls, method, url, data=None):
        cookies = {
            'session': cls.get_token(),
        }
        response = requests.request(method=method, url=url, cookies=cookies, data=data)
        response.raise_for_status()
    
        return response

    @classmethod
    def get_token(cls):
        return BaseConfig.github_session(value=cls.get_chrome_cookies())

    @staticmethod
    def get_chrome_cookies():
        # using configparser to save cookies as some users may use Windows instead Linux/macOS
        # cookie_file = glob.glob(os.path.expanduser('~/.config/google-chrome/*/Cookies'))
        chrome = browser_cookie.chrome(domain_name='.adventofcode.com')  # cookie_file=cookie_file, 
        chrome_cookie = [c for c in chrome if c.name == 'session']
        session = [c.value for c in chrome_cookie][0]
        return session

    @classmethod
    def submit_answer(cls, year, day, title, level, answer):
        submitted = False
        star = None
        message = None
        right_answer = 'the right answer'
        wrong_answer = 'not the right answer'
        too_high = 'too high'
        too_low = 'too low'
        
        year_long = f'20{year}'
        day = day[1:] if day.startswith('0') else day
        data = {'level': level, 'answer': answer}
        url = cls.urls['aoc_answer'].format(year=year_long, day=day)

        response = cls.make_request(method='POST', url=url, data=data)

        if response.status_code == 200:
            content = HTMLHelper.content_helper(response.content)
            content = content.text_content()
            print(content)

            if wrong_answer in content:
                logger.info(colored(f'{wrong_answer}', 'red', 'on_black'))
                submitted = True
                message = wrong_answer
            
            if right_answer in content:
                logger.info(colored(f'{right_answer}', 'green', 'on_black'))
                submitted = True
                star = '*' if 'one gold star' in content else "**" if 'two gold stars' in content else None
                message = right_answer
     
        cls.save_answer(year_long, day, title, level, answer, star, submitted, message)
        
        return logger.info(colored(f'{message}', 'green', 'on_black')) if message == right_answer \
            else logger.info(colored(f'{message}', 'red', 'on_light_grey')) if message == wrong_answer \
            else logger.info(colored(f'Something went wrong!', 'red', 'on_black'))

    @classmethod
    def save_answer(cls, year_long, day, title, level, answer, star, submitted, message):
        now = datetime.now()
        json_file = SetupProject.paths_dir['results_file']
        new_data = {
            'year': year_long, 'day': day, 'title': title, 'level': level, 'answer': str(answer), 
            'submitted': submitted, 'message': message, 'time': now.strftime("%Y-%m-%d %H:%M:%S"), 'star ': star
        }
        
        try:
            file = SolverFunctions.read_raw(json_file)
            data = json.loads(file)
            data.append(new_data)
            json_data = json.dumps(data, indent=4, default=str)
            return SolverFunctions.file_handler(json_file, json_data, mode='w')
        
        except json.decoder.JSONDecodeError:
            json_data = json.dumps([new_data], indent=4, default=str)
            return SolverFunctions.file_handler(json_file, json_data, mode='w')
