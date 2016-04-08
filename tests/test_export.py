#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:  Dominik Gresch <greschd@gmx.ch>
# Date:    08.04.2016 15:05:59 CEST
# File:    test_export.py

import pytest
import fsc.export

def test_foo():
    fsc.export.test_doc(False)
    import foo
    assert foo.__all__ == ['foo']
    assert foo.bar.__all__ == ['bar']
    
def test_bar():
    fsc.export.test_doc(True)
    with pytest.raises(AssertionError):
        import bar

def test_baz():
    fsc.export.test_doc(True)
    import baz
    assert baz.__all__ == ['foo']
    assert baz.bar.__all__ == ['bar']
