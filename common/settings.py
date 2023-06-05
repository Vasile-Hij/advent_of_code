import os
import configparser, sys
from pathlib import Path
from common.util import find_strings, check_len_string, read_raw


def get_path():
    path = Path(__file__)
    return path.parent.parent


def get_input_path(value):
    year = value
    ROOT_DIR = get_path()
    input_path = os.path.join(ROOT_DIR, 'input')
    
    
    for dirpath, dirnames, filenames in os.walk(input_path):
        dirnames.sort(reverse=True)
        available_year = (dirnames[:1])[0]

        if year == available_year:
            return year
        if year != available_year:
            year = available_year
            return year


files = {
    'input_path_sample': 'input/{year}/day{day}{sample}.txt',
    'input_path': 'input/{year}/day{day}.txt',
    'script_path': 'py.{year}.day{day}'
    }


def get_credentials(account_name):
    account_name_length = check_len_string(account_name)
    
    if account_name_length:
            checking_account_name = find_strings(account_name)
            if checking_account_name:
                checked_account_name = account_name
            else:
                print('The config param you have typed is not a string!')
                sys.exit(1)
            
    else:
        print('Your input for config account is too short!')
        sys.exit(1)
    
    
    
    lowered_account_name = ''.join(list(map(str.lower, checked_account_name)))
    
    
    ROOT_DIR = get_path()
    
    print(lowered_account_name)
    config_path = os.path.join(ROOT_DIR, '.config.cfg')
    config = configparser.ConfigParser()
    

    username = 'u'
    password ='p'
    
    if config:
    
        try:
            username = config.get(lowered_account_name, 'username')
            password = config.get(lowered_account_name, 'password')
        except configparser.NoOptionError:
            raise('Check .config.cfg file for right credentials')
    
    return username, password
    