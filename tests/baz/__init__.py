#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:  Dominik Gresch <greschd@gmx.ch>
# Date:    08.04.2016 15:06:23 CEST
# File:    __init__.py

from fsc.export import export

from . import bar


@export
def foo():
    """baz.foo"""
    pass
