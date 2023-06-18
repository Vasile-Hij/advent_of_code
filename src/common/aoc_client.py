import requests
import os
from lxml import html
from src.common.util import read_raw
from src.common.paths import paths_dir 
from src.common.settings import get_config_file_auth
from setup_proj import make_dir

selector_sign_in = 'header div nav ul li a'
selector_get_yor_input = ''
selector_post_result = ''

urls={
    'base_url':'https://adventofcode.com/{year}/day/{day}',
    'log_in_github': 'https://adventofcode.com/{}/auth/github'
}


def log_in():
    try:
        token = get_config_file_auth()
    except FileNotFoundError:
        raise('Please make a GitHub Fine-grained-token as described in README')
    return token


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
    params = log_in()
    
    try:
        response = requests.get(url=base_url)
        response.raise_for_status()
    except Exception as e:
        print(e)    
   
    return response

get_html = get_cached_html(2022, 1)

print(get_html)