from termcolor import colored
from utils.extra.yaml_data import _yaml_parser
import os

_lev = os.path.join(os.getcwd(), 'utils/configs/log_levels.yaml')

levels = _yaml_parser(_lev)

def _log(msg: str, warning_level: str = 'info'):
  "prints message with warning level"
  ret = colored(msg, levels[warning_level])
  print(ret)
