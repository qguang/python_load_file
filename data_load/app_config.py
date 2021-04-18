'''
Read and parse app_config.yml and store it in app_config variable
'''

import os
import yaml

APP_BASEDIR=os.path.abspath(os.path.dirname(__file__))
APP_CONFIG_FILENAME=os.path.join(APP_BASEDIR, 'app_config.yml')
APP_CONFIG={}
def read_app_config_filename():
    with open(APP_CONFIG_FILENAME, 'r') as stream:
        try:
            app_config = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return app_config

APP_CONFIG=read_app_config_filename()
