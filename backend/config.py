import os
import configparser

real_path = os.path.realpath(__file__)
dir_path = os.path.dirname(real_path)

config_local = configparser.ConfigParser()
config_local.read('{}/db.ini'.format(dir_path))