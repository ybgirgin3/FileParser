from termcolor import colored
from utils.extra.yaml_data import yaml_parser
import os

_lev = os.path.join(os.getcwd(), 'utils/configs/log_levels.yaml')

levels = yaml_parser(_lev)


def log(msg: str, warning_level: str = 'info'):
  "prints message with warning level"
  #ret = colored(msg, levels[warning_level])
  ret = colored(msg, 'red', 'on_grey',)

  print(ret)
