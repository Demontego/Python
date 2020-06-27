# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 18:33:14 2019

@author: vkrin
"""

x=list(map(int, input().split(' ')))

if ((x[0]-x[1])%2==0):
    for i in range(x[0]-x[1]):
        if (i+1)%2==0:
            print(2, end=' ')
        else: print(1, end=' ')
    for j in range(x[1]):
        print(j+1, end=' ')
else:
    for i in range(x[0]-x[1]+1):
        if (i+1)%2==0:
            print(2, end=' ')
        else: print(1, end=' ')
    for j in range(x[1]):
        j+=1
        if j!=2:
            print(j, end=' ')
            