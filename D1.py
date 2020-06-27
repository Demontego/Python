# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 21:32:40 2019

@author: vkrin
"""
a=int(input())
b=int(input())
s=[]
for i in range(b):
    x,y=input().split(' ')
    x=int(x)
    y=int(y)
    s.append(set(j for j in range(x,y+1)))
count=0
for i in range(len(s)):
    count+=1
    for j in range(0,i):
        if s[i].intersection(s[j]):
            count-=1
            s[j]={0}
print(count)
