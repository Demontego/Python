# -*- coding: utf-8 -*-
x=input()
a=input().split()
b=[]
for i in a:
    if i not in b:
        b.append(i)
for i in b:
    print(i, end=' ')
print('')
print(len(a)-len(b))