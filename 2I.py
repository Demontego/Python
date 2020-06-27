# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 08:48:55 2019

@author: vkrin
"""
import copy
class FragileDict:
    def __init__(self,Dict=None):
        if Dict is None:
            self._data = dict()
        elif type(Dict) is not dict:
            self._data = copy.deepcopy(dict.fromkeys(Dict))
        else:
            self._data=copy.deepcopy(Dict)
        self._lock=False
    
    def __getitem__(self, key):
        if not key in self._data:
            raise KeyError(key)
        if (self._lock):
            return self._data[key]
        return copy.deepcopy(self._data[key])
   
    def __setitem__(self, key, value):
        if (self._lock):
            self._data[key] = copy.deepcopy(value)
        else:
            raise RuntimeError("Protected state")
    
    def __enter__(self):
        self.buffer = copy.deepcopy(self._data)
        self._lock = True
        return self

 
    def __exit__(self, exp_type, exp_value, exp_ptr):
        if exp_type:
            self._data = copy.deepcopy(self.buffer)
            self._lock=False
            print("Exception has been suppressed.")
            del self.buffer
            return True
        self._data = copy.deepcopy(self._data)
        self._lock=False
        del self.buffer
    
    def __contains__(self, key):
        for i in self._data:
            if (i == key):
                return True
        return False

