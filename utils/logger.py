from termcolor import colored

levels = {
  'info': 'blue',
  'warning': 'yellow',
  'danger': 'red'
}

def _log(msg: str, warning_level: str):
  ret = colored(msg, levels[warning_level])
  print(ret)