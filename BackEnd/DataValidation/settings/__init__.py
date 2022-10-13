import os
import json


CONFIG_FILE = '/etc/config.json'
print(CONFIG_FILE)

try:
    with open(CONFIG_FILE) as config_file:
        config = json.load(config_file)
        PROD = config['PROD']
        print(config['PROD'])
        print(PROD)
    from .prod import *
    print("prod")


except KeyError:
    print("dev")
    from .dev import *
    print("apres dev")

'''SECRET_KEY = config['SECRET_KEY']'''

