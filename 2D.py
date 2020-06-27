# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 17:55:11 2019

@author: vkrin
"""

import functools
def counter(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if(wrapper.ncalls==wrapper.complete):
            wrapper.ncalls=0
            wrapper.complete=0
            wrapper.rdepths=0
            wrapper.rdepth=0
            wrapper.completes=0
        wrapper.ncalls +=1
        wrapper.rdepths+=1
        res = func(*args, **kwargs)
        wrapper.completes=1
        wrapper.complete+=1
        if(wrapper.rdepths>wrapper.rdepth):
            wrapper.rdepth=wrapper.rdepths
        wrapper.completes=0
        wrapper.rdepths-=1
        return res
    wrapper.completes=0
    wrapper.rdepths=0
    wrapper.ncalls=0
    wrapper.complete=0
    wrapper.rdepth=0
    return wrapper   
