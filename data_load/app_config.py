'''
Read and parse app_config.yml and store it in app_config variable
'''

import os
import yaml

app_basedir=os.path.abspath(os.path.dirname(__file__))
app_config_filename=os.path.join(app_basedir, 'app_config.yml')
app_config={}
def read_app_config_filename():
    with open(app_config_filename, 'r') as stream:
        try:
            app_config = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return app_config

app_config=read_app_config_filename()
