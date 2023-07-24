import requests
from src.aoc.lxml_utils import content_helper, lxml_select
from src.common.settings import github_session
from setup_proj import make_dir, paths_dir
import browser_cookie3 as bc3 


urls = { 
    'base_url':'https://adventofcode.com/{year}/day/{day}',
    'log_in_github': 'https://adventofcode.com/{}/auth/github',
    'aoc_answer': 'https://adventofcode.com/{day}/day/{day}/answer',
    'aoc_owner': 'https://adventofcode.com/settings'
}


def get_aoc_data(year, day):
    year_long = f'20{year}'
    request_day = day[1:] if day.startswith('0') else day
    input_day = f'{request_day}/input'

    get_cached_html_story(year, day, year_long, request_day)
    input_html_data = get_cached_html_input(year, day, year_long, input_day)
   
    return lxml_select(input_html_data)
    
    
def get_cached_html_input(year, day, year_long, request_day):
    _input = True
    print('Requesting AoC input!')
    return get_cached_html(year, day, year_long, request_day, _input)
    

def get_cached_html_story(year, day, year_long, request_day):
    print('Requesting AoC story!')
    return get_cached_html(year, day, year_long, request_day)


def get_cached_html(year, day, year_long, request_day, _input=None):
    cached_html = paths_dir['cached_html'].format(year=year)
    _day = 'day{day}.html'.format(day=day)
    if _input:
        _day = 'day{day}_input.html'.format(day=day, input=_input)
    day_file = f'{cached_html}{_day}'
    
    try:
        with open(day_file, 'r') as file:
            file_response = file.read()
        return content_helper(file_response)

    except FileNotFoundError:
        make_dir(cached_html)
        response = get_response(year_long, request_day)
        with open(day_file, 'wb+') as file:
            file.write(response.content)

        return content_helper(response.content)


def get_response(year, day):
    base_url = urls['base_url'].format(year=year, day=day)
    cookies = {'session': get_cookies()}
    
    response = requests.get(url=base_url, cookies=cookies, allow_redirects=False)
    response.raise_for_status()

    return response
    
    
def get_chrome_cookies():
    # using configparser to save cookies as some users may use Windows instead Linux/macOS
    #cookie_file = glob.glob(os.path.expanduser('~/.config/google-chrome/*/Cookies'))
    chrome = bc3.chrome(domain_name='.adventofcode.com')  # cookie_file=cookie_file, 
    chrome_cookie = [c for c in chrome if c.name == 'session']
    session = [c.value for c in chrome_cookie][0]
    return session


def get_cookies():
    return github_session(value=get_chrome_cookies())

