import yaml
import sys

with open(sys.argv[1]) as stream:
    versions = list(yaml.safe_load(stream)['versions'].keys())
    versions.sort()
    print('LATEST={}'.format(versions[-1]))
