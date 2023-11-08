import logging
import requests
from src.aoc.lxml_utils import HTMLHelper
from src.common.configs import BaseConfig
from src.common.setup_project import SetupProject
import browser_cookie3 as bc3 

logger = logging.getLogger(__name__)


class AdventOfCodeBase:
    urls = {
        'base_url': 'https://adventofcode.com/{year}/day/{day}',
        'log_in_github': 'https://adventofcode.com/{}/auth/github',
        'aoc_answer': 'https://adventofcode.com/{day}/day/{day}/answer',
        'aoc_owner': 'https://adventofcode.com/settings'
    }
    
    @classmethod
    def get_aoc_data(cls, year, day):
        year_long = f'20{year}'
        request_day = day[1:] if day.startswith('0') else day
        input_day = f'{request_day}/input'
    
        cls.get_cached_html_story(year, day, year_long, request_day)
        return cls.get_cached_html_input(year, day, year_long, input_day)

    @classmethod
    def get_cached_html_input(cls, year, day, year_long, request_day):
        _input = True
        logger.info('Requesting AoC input!')
        return cls.get_cached_html(year, day, year_long, request_day, _input).text_content()

    @classmethod
    def get_cached_html_story(cls, year, day, year_long, request_day):
        logger.info('Requesting AoC story!')
        return cls.get_cached_html(year, day, year_long, request_day)
    
    @classmethod
    def get_cached_html(cls, year, day, year_long, request_day, _input=None):
        cached_html = SetupProject.paths_dir['cached_html'].format(year=year)
        _day = 'day{day}.html'.format(day=day)
        if _input:
            _day = 'day{day}_input.html'.format(day=day, input=_input)
        day_file = f'{cached_html}{_day}'
        
        try:
            with open(day_file, 'r') as file:
                file_response = file.read()
            return HTMLHelper.content_helper(file_response)
        except FileNotFoundError:
            SetupProject.make_dir(cached_html)
            response = cls.get_response(year_long, request_day)
            
            with open(day_file, 'wb+') as file:
                file.write(response.content)
    
            return HTMLHelper.content_helper(response.content)
    
    @classmethod
    def get_response(cls, year, day):
        base_url = cls.urls['base_url'].format(year=year, day=day)
        cookies = {'session': cls.get_cookies()}
        
        response = requests.get(url=base_url, cookies=cookies, allow_redirects=False)
        response.raise_for_status()
    
        return response
    
    @classmethod
    def get_cookies(cls):
        return BaseConfig.github_session(value=cls.get_chrome_cookies())
    
    @staticmethod
    def get_chrome_cookies():
        # using configparser to save cookies as some users may use Windows instead Linux/macOS
        # cookie_file = glob.glob(os.path.expanduser('~/.config/google-chrome/*/Cookies'))
        chrome = bc3.chrome(domain_name='.adventofcode.com')  # cookie_file=cookie_file, 
        chrome_cookie = [c for c in chrome if c.name == 'session']
        session = [c.value for c in chrome_cookie][0]
        return session
    
    


