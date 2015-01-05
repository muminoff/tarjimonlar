#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import tarjimonlar
version = tarjimonlar.__version__

setup(
    name='tarjimonlar',
    version=version,
    author='',
    author_email='smuminov@gmail.com',
    packages=[
        'tarjimonlar',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.7.1',
    ],
    zip_safe=False,
    scripts=['tarjimonlar/manage.py'],
)
