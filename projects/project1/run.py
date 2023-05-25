from utils import subtract

from configparser import ConfigParser

config = ConfigParser()

config.read('config.ini')

print(subtract(2, 1))

print(config['TEST_CONFIG']['config_value'])
