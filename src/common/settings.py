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
        available_year_or_last_year = (dirnames[:1])[0]

        if year == available_year_or_last_year:
            return year
        if year != available_year_or_last_year:
            year = available_year_or_last_year
            return year


def get_config_value(cfg_name, header_name, field_name, value):
    path = Path(__file__)
    ROOT_DIR = path.parent.parent.parent

    config_path = os.path.join(ROOT_DIR, cfg_name)
    config = ConfigParser()
    config.read(config_path)
    created = False

    try:
        token = config.get(header_name, field_name)
    except (NoOptionError, NoSectionError):
        config.add_section(header_name)
        config.set(header_name, field_name, value)

        with open(cfg_name, 'w') as cfg:
            config.write(cfg)

        with open('.gitignore', 'r') as rf:
            gitignore_file = rf.read().splitlines()
        print(gitignore_file[-1])
        if cfg_name not in gitignore_file:
            with open('.gitignore', 'a+') as gf:
                if gitignore_file[-1] != '':
                    gf.write(f'\n')
                    gf.write(cfg_name)
                else:
                    gf.write(cfg_name)
                    
        token = config.get(header_name, field_name)
        created = True

    return token, created


def github_session(value=None):
    cfg_name = '.config.cfg'
    header_name = 'GitHub'
    field_name = 'session'

    try:
        token, created = get_config_value
    except TypeError:
        token, created = get_config_value(
            cfg_name=cfg_name, header_name=header_name, field_name=field_name, value=value
        )
        if created:
            print('AoC cookies are cached now!')

    return token


def make_setup():
    cfg_name = '.setup.cfg'
    header_name = 'SETUP'
    field_name = 'project'
    value = 'True'
    
    return get_config_value(
        cfg_name=cfg_name, header_name=header_name, field_name=field_name, value=value
        )
    
    
