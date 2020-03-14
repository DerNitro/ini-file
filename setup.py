#!/usr/bin/env python3
# -*- coding: utf8 -*-

from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='ini-file',
    version='1.0.0',
    packages=[''],
    url='https://github.com/DerNitro/ini-file',
    license='GPLv3',
    author='Sergey V. Utkin',
    author_email='utkins01@gmail.com',
    description='A small utility for get value from .ini files',

    classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Environment :: Console',
            'Intended Audience :: Information Technology',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Programming Language :: Python :: 3 :: Only',
            'Natural Language :: Russian',
            'Operating System :: POSIX :: Linux',
            'Topic :: System'
        ],

        scripts=['bin/ini-file']
)
