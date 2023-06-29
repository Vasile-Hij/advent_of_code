import requests
import os
from lxml import html
from src.common.settings import github_session
from setup_proj import make_dir, paths_dir
import browser_cookie3 as bc3 
import glob


urls={
    'base_url':'https://adventofcode.com/{year}/day/{day}',
    'log_in_github': 'https://adventofcode.com/{}/auth/github',
    'aoc_answer': 'https://adventofcode.com/{day}/day/{day}/answer',
    'aoc_owner': 'https://adventofcode.com/settings'
}


def get_chrome_cookies():
    # using configparser to save cookies as some users may use Windows instead Linux/macOS
    #cookie_file = glob.glob(os.path.expanduser('~/.config/google-chrome/*/Cookies'))
    chrome = bc3.chrome(domain_name='.adventofcode.com')  # cookie_file=cookie_file, 
    chrome_cookie = [c for c in chrome if c.name == 'session']
    session = [c.value for c in chrome_cookie][0]
    return session


def get_cookies():
    try:
        cookie = github_session()
    except TypeError:
        cookie = github_session(get_chrome_cookies())
        
    return cookie


def get_cached_html(year, day):
    cached_html = paths_dir['cached_html'].format(year=year)
    make_day = 'day{day}.html'.format(day=day)
    
    day_file = ''.join([cached_html, make_day])
    
    try:
        with open(day_file, 'r') as file:
            file_response = file.read()
        return html.fromstring(file_response)
            
    except FileNotFoundError:
        make_dir(cached_html)

        response = get_response(year, day)
        with open(day_file, 'wb+') as file:
            file.write(response.content)

        return html.fromstring(response.text)

            
def get_response(year, day):
    base_url = urls['base_url'].format(year=year, day=day)
    cookies = {'session': get_cookies()}
    
    response = requests.get(url=base_url, cookies=cookies, allow_redirects=False)
    response.raise_for_status()
      
    return response


