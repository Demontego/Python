# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 16:14:15 2019

@author: vkrin
"""

def solution1(s):
    return [i*4 for i in s];
def solution2(s):
    return [i*j for i,j in zip(s, range(1,len(s)+1))];
def solution3(a):
    return [i for i in a if i%3==0 or i%5==0]
def solution4(v):
    return [j for i in v for j in i ]
def solution5(n):
    return [(i,j,k) for i in range(1,n+1) for j in range(i,n+1) for k in range(j,n+1) if i**2+j**2==k**2 ]
def solution6(v):
    return [[i+j for j in v[1]] for i in v[0] ]
def solution7(v):
    return [[i[j] for i in v] for j in range(len(v[0]))]
def solution8(v):
    return [list(map(int, j.split())) for j in v]
def solution9(v):
    return {chr(i+97): i**2 for i in v}
def solution10(v):
    return set({i.title() for i in v if len(i)>3})


solutions = {
    'solution1': solution1,
    'solution2': solution2,
    'solution3': solution3,
    'solution4': solution4,
    'solution5': solution5,
    'solution6': solution6,
    'solution7': solution7,
    'solution8': solution8,
    'solution9': solution9,
    'solution10': solution10,
}
#a=['Alice', 'vova', 'ANTON', 'Bob', 'kAMILA', 'CJ', 'ALICE', 'Nastya']
#print(solution10(a))