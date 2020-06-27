# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 21:27:24 2019

@author: vkrin
"""


def product(a):
    if not a:
        yield a
    else:
        yield from ((x,*p) for x in a[0] for p in product(a[1:]))


