import yaml


def yaml_parser(fp=None):
  return yaml.safe_load(open(fp))  # if fp is not None else ""

# ret = _yaml_parser('utils/configs/tess_paths.yaml')
# print(ret)
