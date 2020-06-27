# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 22:32:45 2019

@author: vkrin
"""
from collections import deque
class Node:
    def __init__(self, val, l=None,r=None):
        self.val=val
        self.l=l
        self.r=r

class BinarySearchTree:
    def __init__(self, val=None):
        self.root=Node(val)
    def append(self, val):
        if self.root.val is None:
            self.root.val=val
            return
        current=self.root
        while current:
            if val < current.val:
                if current.l is None:
                    current.l=Node(val)
                    break
                current=current.l
            elif val > current.val:
                if current.r is None:
                    current.r=Node(val)
                    break
                current=current.r
            else:
                break
        return
    def __contains__(self, val):
        if self.root.val is None:
            return False
        current=self.root
        while current:
            if current.val==val:
                return True
            elif val<current.val:
                if current.l is None:
                    return False
                current=current.l
            elif val>current.val:
                if current.r is None:
                    return False
                current=current.r
    def __iter__(self):
        self.d=deque()
        if self.root.val is not None:
            self.d.appendleft(self.root)
        while len(self.d)>0:
            a=self.d.pop()
            yield a.val
            if a.l is not None:
                self.d.appendleft(a.l)
            if a.r is not None:
                self.d.appendleft(a.r)


