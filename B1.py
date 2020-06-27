# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 17:14:45 2019

@author: vkrin
"""
def number(x):
    return x%10+x//10
n=input()
a=tuple(map(int, input().split(' ')))
a=sorted(a)
a=sorted(a, key=number)
for i in a:
    print(i, end=' ')