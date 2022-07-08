from termcolor import colored

levels = {
  'info': 'blue',
  'warning': 'yellow',
  'danger': 'red'
}

def _log(msg: str, warning_level: str = 'info'):
  "prints message with warning level"
  ret = colored(msg, levels[warning_level])
  print(ret)