#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:  Dominik Gresch <greschd@gmx.ch>
# Date:    30.03.2016 00:29:06 CEST
# File:    setup.py

import sys

from setuptools import setup

pkgname = 'export'
pkgname_qualified = 'fsc.' + pkgname

with open('doc/description.txt', 'r') as f:
    description = f.read()
try:
    with open('doc/README', 'r') as f:
        readme = f.read()
except IOError:
    readme = description

with open('version.txt', 'r') as f:
    version = f.read().strip()

setup(
    name=pkgname_qualified,
    version=version,
    packages=[pkgname_qualified],
    url='http://frescolinogroup.github.io/frescolino/pyexport/' + '.'.join(version.split('.')[:2]),
    include_package_data=True,
    author='C. Frescolino',
    author_email='frescolino@lists.phys.ethz.ch',
    description=description,
    python_requires=">=3.6",
    install_requires=[],
    extras_require={
        'test': ['pytest'],
        'doc': ['sphinx', 'sphinx_rtd_theme'],
        'precommit':
        ['pre-commit==1.20.0', 'prospector==1.1.7', 'pylint==2.3.1', 'yapf==0.28', 'mypy'],
    },
    long_description=readme,
    classifiers=[
        'License :: OSI Approved :: Apache Software License', 'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6', 'Programming Language :: Python :: 3.7',
        'Topic :: Utilities'
    ],
    license='Apache',
)
