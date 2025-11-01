import yaml
import sys
from packaging.version import Version

with open(sys.argv[1]) as stream:
    versions = list(yaml.safe_load(stream)['versions'].keys())
    versions.sort(key=Version)
    print('LATEST={}'.format(versions[-1]))
