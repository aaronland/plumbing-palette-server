#!/usr/bin/env python

import os
import sys
import shutil

from setuptools import setup, find_packages

packages = find_packages()
desc = open("README.md").read()
version = open("VERSION").read()

setup(name='plumbing-palette-server',
      version=version,
      description='A Flask-based HTTP pony for extracting colors from images',
      author='Cooper Hewitt Smithsonian Design Museum',
      url='https://github.com/cooperhewitt/plumbing-palette-server',
      scripts=[
          'scripts/palette-server.py',
      ],
      download_url='https://github.com/cooperhewitt/plumbing-palette-server/tarball/master#egg=0.22',
      license='BSD')
