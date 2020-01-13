# -*- coding: utf-8 -*-

import click
import datetime
import json
import os
from config.config import CONFIG_DIR

__all__ = ['lint']

ignore_dir = [
    'static',
    'templates',
    'image_temp',
    'website',
    'migrations',
    'node_modules',
    'venv',
    '__pycache__'
]


def f_code(path, md5_dict):
    md5 = os.popen("md5sum {0}|cut -d ' ' -f1".format(path)).read().strip()
    if md5_dict.get(path, None) != md5:
        print(path)
        os.system('isort -e -ns __init__.py -sl -ds -w 80 ' + path)
        os.system('autopep8 --in-place --aggressive --aggressive ' + path)
        md5_dict[path] = os.popen(
            "md5sum {0}|cut -d ' ' -f1".format(path)).read().strip()


def read_dir(path, md5_dict):
    result = []
    for d in os.listdir(path):
        if d not in ignore_dir:
            sub_path = os.path.join(path, d)
            if os.path.isdir(sub_path):
                result += read_dir(sub_path, md5_dict)
            elif sub_path[-3:] == '.py':
                f_code(sub_path, md5_dict)
    return result


@click.command()
def lint():
    base_path = CONFIG_DIR
    print(base_path)
    print(datetime.datetime.now())
    md5_dict = {}
    if not os.path.exists(os.path.join(base_path, '.pymd5')):
        with open(os.path.join(base_path, '.pymd5'), 'w+') as f:
            f.write(json.dumps(md5_dict))
    with open(os.path.join(base_path, '.pymd5'), 'r+') as f:
        md5_dict = json.loads(f.read())
        read_dir(base_path, md5_dict)

    with open(os.path.join(base_path, '.pymd5'), 'w+') as f:
        f.write(json.dumps(md5_dict))
    print(datetime.datetime.now())
