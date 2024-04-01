import yaml
import sys

with open(sys.argv[1]) as stream:
    print('LATEST={}'.format(list(yaml.safe_load(stream)['versions'].keys())[0]))
