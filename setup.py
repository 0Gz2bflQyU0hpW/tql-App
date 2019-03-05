#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'setup.py'
__author__ = 'JieYuan'
__mtime__ = '18-12-14'
"""
import io
import re
import os
from setuptools import find_packages, setup

with open('restful_api/__init__.py', encoding='utf8') as f:
    version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)

with open("readme.md", encoding='utf-8') as f:
    long_description = f.read()


def get_requirements():
    _ = './requirements.txt'
    if os.path.isfile(_):
        with open(_) as f:
            return f.read().split()


setup(
    name='restful_api',
    version=version,
    url='https://github.com/Jie-Yuan/RestfulApi',
    keywords=["restful_api"],
    description=('description'),
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='YuanJie',
    author_email='313303303@qq.com',
    maintainer='YuanJie',
    maintainer_email='313303303@qq.com',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['*.*']},
    platforms=["all"],
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],

    install_requires=get_requirements()
)
