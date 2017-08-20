#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests


def func(x):
    return x + 1

def get_url(url):
    req = requests.get(url)
    return  req.status_code
