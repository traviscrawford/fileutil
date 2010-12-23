#!/usr/bin/env python

from setuptools import setup

setup(
  name='fileutil',
  version='1.0',
  description=('Unified interface for simple file operations on a '
      'variety of storage systems.'),
  author='Travis Crawford',
  author_email='traviscrawford@gmail.com',
  url='http://github.com/traviscrawford/fileutil',
  packages=['fileutil'],
  package_dir = {'': 'lib'},
  scripts=['scripts/fileutil'],
)
