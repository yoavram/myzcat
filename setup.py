# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

setup(
    name='myzcat',
    version='0.1.0',
    url='https://github.com/yoavram/myzcat',
    license='MIT',
    author='Yoav Ram',
    author_email='yoav@yoavram.com',
    description='Opens gzip-compressed text files',
    packages=find_packages(),
    install_requires=[
        'click>=0.6'
    ],
    extras_require={
        'tests': [
            'nose',
            'coverage'
        ]
    },
    entry_points={
        'console_scripts': [
            'myzcat=myzcat.cli:main',
        ]
    }
)
