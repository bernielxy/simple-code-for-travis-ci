#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pytest

from sample import func, get_url


def test_integer():
    assert func(3) == 4

def test_float():
    assert func(0.1) == 1.1

def test_None():
    with pytest.raises(TypeError):
        assert func(None) == None

def test_get_url():
    assert get_url('http://www.baidu.com') == 200
