import os
import json


CONFIG_FILE = './config.json'

try:
    with open(CONFIG_FILE) as config_file:
        config = json.load(config_file)
        PROD=config['PROD']
    from .prod import *
    print("prod")


except KeyError:
    print("dev")
    from .dev import *

'''SECRET_KEY = config['SECRET_KEY']'''
