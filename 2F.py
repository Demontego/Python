# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 22:03:10 2019

@author: vkrin
"""

def func(n, os, cs, s):
    if(os + cs == 2 * n):
        yield s
    if(os < n):
        yield from func(n, os + 1, cs, s + '(')
    if(cs < os):
        yield from func(n, os, cs + 1, s + ')')

def brackets(n):
    yield from func(n,0,0,'')

n=int(input())
print(*brackets(n), sep='\n')

