# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 10:55:00 2019

@author: vkrin
"""
import re
import operator
from functools import reduce
def solution1(s):
    return list(map(lambda x: int(re.sub(r'\D','',x[::-1])), s))
def solution2(s):
    return list(map(lambda x: x[0]*x[1], s));
def solution3(a):
    return list(filter(lambda x: (x+2)%6 and (x+3)%6 and (x+5)%6, a))
def solution4(v):
    return list(filter(None, v))
def solution5(v):
    list(map(lambda x: operator.setitem(x,"square",x["width"]*x["length"]) ,v))
    return v
def solution6(v):
     return list(map(lambda x: dict(list(x.items())+list(x.fromkeys(["square"], x["width"]*x["length"]).items())) ,v))
def solution7(v):
    return reduce(lambda x,y: y.intersection(x), v)
def solution8(v):
    return dict(map(lambda x: (x, v.count(x)), v))
def solution9(v):
    return list(map(lambda y: y['name'],filter(lambda x: x['gpa']>4.5, v)))
def solution10(v):
    return list(filter(lambda x: int(x)//100000+int(x)//1000%10+int(x)%100//10==int(x)%10+int(x)%1000//100+int(x)//10000%10 , v))


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
#print(solution1(a))
#print(solution2(a))
#print(solution3(a))
#print(solution4(a))
#print(solution5(a))
#print(solution6(a))
#print(solution7(a))
#print(solution8(a))
#print(solution9(a))
#print(solution10(a))

#a=['12', '25.6', '84,02', '  69-91']
#b=zip(range(2, 5), range(3, 9, 2))
#c=['', 25, None, 'python', 0.0, [], ('msu', '1755-01-25')]
#d=[{1, 2, 3, 4, 5}, {2, 3, 4, 5, 6}, {3, 4, 5, 6, 7}]
#rooms = [
#    {"name": "комната1", "width": 2, "length": 4},
#    {"name": "комната2", "width": 2.5, "length": 5.6},
#    {"name": "кухня", "width": 3.5, "length": 4},
#    {"name": "туалет", "width": 1.5, "length": 1.5},
#]
#students = [
#    {'name': 'Alina', 'gpa': 4.57},
#    {'name': 'Sergey', 'gpa': 5.0},
#    {'name': 'Nastya', 'gpa': 4.21},
#    {'name': 'Valya', 'gpa': 4.72},
#    {'name': 'Anton', 'gpa': 4.32},
#]
#e=['165033', '477329', '631811', '478117', '475145', '238018', '917764', '394286']
#f=[1, 2, 1, 1, 3, 2, 3, 2, 4, 2, 4]
#print(solution1(a))
#print(solution2(b))
#print(solution3(range(20)))
#print(solution4(c))
#solution5(rooms)
#print(rooms)
#print(solution6(rooms))
#print(solution8(f))
#print(solution7(d))
#print(solution9(students))
#print(solution10(e))


