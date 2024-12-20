import os
import logging
import sys
import re
from pathlib import Path
from configparser import ConfigParser, NoOptionError, NoSectionError, DuplicateSectionError
from src.common.utils import SolverFunctions

logger = logging.getLogger(__name__)


GITIGNORE = '.gitignore'
CONFIG = '.config.cfg'
GITHUB_HEADER_NAME = 'GitHub'
SETUP_CONFIG = '.setup.cfg'
SETUP_HEADER_NAME = 'SETUP'
SETUP_FIELD_NAME = 'project'
DOMAIN_NAME = '.adventofcode.com'
DEFAULT_BROWSER_HEADER = 'Default browser'
DEFAULT_BROWSER = 'choice'
BROWSER_OPTIONS = {'1': 'chrome', '2': 'firefox', '3': 'edge'}
MACOS_FIREFOX_PATH = '~/Library/Application Support/Firefox/Profiles'


class BaseConfig:
    solver_functions = SolverFunctions()

    @staticmethod
    def get_path():
        path = Path(__file__)
        return path.parent.parent

    @classmethod
    def get_input_path(cls, value):
        year = value
        ROOT_DIR = cls.get_path()
        input_path = os.path

        for dirpath, dirnames, filenames in os.walk(input_path.join(ROOT_DIR, 'input')):
            dirnames.sort(reverse=True)
            available_year_or_last_year = (dirnames[:1])[0]

            if year == available_year_or_last_year:
                return year
            if year != available_year_or_last_year:
                year = available_year_or_last_year
                return year

    @classmethod
    def get_or_create_config_value(cls, cfg_name, header_name, field_name, value=None, force=True):
        path = Path(__file__)
        ROOT_DIR = path.parent.parent.parent

        config_path = os.path
        config = ConfigParser()
        config.read(config_path.join(ROOT_DIR, cfg_name))

        try:
            return config.get(header_name, field_name)
        except (NoOptionError, NoSectionError):
            if not force:
                return

            try:
                config.add_section(header_name)
            except DuplicateSectionError:
                config.set(field_name, f'{value}')
            else:
                config.set(header_name, field_name, value)

            with Path.open(cfg_name, 'w') as cfg:
                config.write(cfg)

            with Path.open(GITIGNORE, 'r') as rf:
                gitignore_file = rf.read().splitlines()

            if cfg_name not in gitignore_file:
                with Path.open(GITIGNORE, 'a+') as gf:
                    if gitignore_file[-1] != '':
                        gf.write('\n')
                        gf.write(cfg_name)
                    else:
                        gf.write(cfg_name)

                logger.info(f'{cfg_name} added to {GITIGNORE}')

            return config.get(header_name, field_name)

    @classmethod
    def clear_cached_token(cls, cfg_name, header_name, field_name):
        path = Path(__file__)
        ROOT_DIR = path.parent.parent.parent

        config_path = os.path
        config = ConfigParser()
        config.read(config_path.join(ROOT_DIR, cfg_name))

        config.remove_section(header_name)
        config.remove_section(field_name)

        cls.write_file(config)

    @classmethod
    def delete_file(cls, file_path):
        if Path.isfile(file_path):
            Path.unlink(file_path)
            print('File was deleted!')
        else:
            print('File does not exist!')

    @classmethod
    def make_setup(cls):
        created = cls.get_or_create_config_value(
            cfg_name=SETUP_CONFIG,
            header_name=SETUP_HEADER_NAME,
            field_name=SETUP_FIELD_NAME
        )
        if not created:
            return bool(cls.get_or_create_config_value(
                cfg_name=SETUP_CONFIG,
                header_name=SETUP_HEADER_NAME,
                field_name=SETUP_FIELD_NAME,
                value=True
            ))
        return bool(created)

    @staticmethod
    def get_method(method_name: str):
        isinstance(SolverFunctions.__dict__[f'{method_name}'], classmethod)
        return getattr(SolverFunctions, method_name)

    @classmethod
    def get_macos_firefox_cookies_custom_user(cls):
        if sys.platform != 'darwin':
            return NotImplementedError

        full_path = Path.expanduser(MACOS_FIREFOX_PATH)

        files = [
            re.search('[A-Za-z0-9].*default-release', file) for file in os.listdir(full_path)
        ]
        if not files:
            raise f'Your cookies were not found! Verify {MACOS_FIREFOX_PATH} if "default-release" exists.'
        file_name = [file_name.group(0) for file_name in files if file_name is not None][0]
        return f'{full_path}/{file_name}/cookies.sqlite'
