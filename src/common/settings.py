import os
from pathlib import Path
from configparser import ConfigParser, NoOptionError, NoSectionError



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


def github_session(value=None):
    path = Path(__file__)
    ROOT_DIR = path.parent.parent.parent
    cfg_name = '.config.cfg'
    
    config_path = os.path.join(ROOT_DIR, cfg_name)
    config = ConfigParser()
    config.read(config_path)

    try:
        token = config.get('GitHub', 'session')
    except (NoOptionError, NoSectionError):
        config.add_section('GitHub')
        config.set('GitHub', 'session', value)
        
        with open(cfg_name, 'w') as cfg:
            config.write(cfg)
            
        with open('.gitignore', 'r') as rf:
            gitignore_file = rf.read().splitlines()
        
        if not cfg_name in gitignore_file:
            with open('.gitignore', 'a+') as gf:
                gf.write(cfg_name)
            
        token = config.get('GitHub', 'session')
    
    return token
