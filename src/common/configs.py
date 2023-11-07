import os
import logging
import inspect
from pathlib import Path
from configparser import ConfigParser, NoOptionError, NoSectionError
from src.common.utils import SolverFunctions

logger = logging.getLogger(__name__)


class BaseConfig:
    @staticmethod
    def get_path():
        path = Path(__file__)
        return path.parent.parent
    
    @classmethod
    def get_input_path(cls, value):
        year = value
        ROOT_DIR = cls.get_path()
        input_path = os.path.join(ROOT_DIR, 'input')
        
        for dirpath, dirnames, filenames in os.walk(input_path):
            dirnames.sort(reverse=True)
            available_year_or_last_year = (dirnames[:1])[0]
    
            if year == available_year_or_last_year:
                return year
            if year != available_year_or_last_year:
                year = available_year_or_last_year
                return year

    @staticmethod
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
                
            if cfg_name not in gitignore_file:
                with open('.gitignore', 'a+') as gf:
                    if gitignore_file[-1] != '':
                        gf.write(f'\n')
                        gf.write(cfg_name)
                    else:
                        gf.write(cfg_name)

                logger.info(f'{cfg_name} added to .gitignore')
                        
            token = config.get(header_name, field_name)
            created = True
    
        return token, created
    
    @classmethod
    def github_session(cls, value=None):
        cfg_name = '.config.cfg'
        header_name = 'GitHub'
        field_name = 'session'
    
        try:
            token, created = cls.get_config_value
        except TypeError:
            token, created = cls.get_config_value(
                cfg_name=cfg_name, header_name=header_name, field_name=field_name, value=value
            )
            if created:
                logger.info('AoC cookies are cached now!')
    
        return token
    
    @classmethod
    def make_setup(cls):
        cfg_name = '.setup.cfg'
        header_name = 'SETUP'
        field_name = 'project'
        value = 'True'
        
        return cls.get_config_value(
            cfg_name=cfg_name, header_name=header_name, field_name=field_name, value=value
            )
    
    # @staticmethod
    # def get_function(function: str):
    #     method_name = function
    #     possibles = globals().copy()
    #     possibles.update(locals())
    #     method = possibles.get(method_name)
    #     print(possibles)
    #     if not method:
    #         raise NotImplementedError(f'Method {method_name} not implemented')
    #     return method
    # 
    # def get_functions(self, *functions: str) -> list:
    #     return [self.get_function(func) for func in functions]

    @staticmethod
    def get_method(method_name: str):
        method_exist = isinstance(SolverFunctions.__dict__[f'{method_name}'], classmethod)
        
        isinstance(SolverFunctions.__dict__[f'{method_name}'], classmethod)
        return SolverFunctions.__dict__[f'{method_name}']
