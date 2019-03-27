#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json


if __name__ == '__main__':
    os.system('rm -rf node_modules/')
    os.system('mv package-lock.json /tmp')

    with open('package.json') as fp:
        d = json.loads(fp.read())
    for dep in d['devDependencies']:
        os.system('npm install %s@latest --save-dev' % dep)
    for dep in d['dependencies']:
        os.system('npm install %s@latest --save' % dep)
