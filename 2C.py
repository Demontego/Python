# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 15:38:52 2019

@author: vkrin
"""
import time
import functools    
def timeout(rps):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **argv):
            t_start=time.time()
            result=func(*args, **argv)
            if 1/rps-time.time()+t_start>0:
                time.sleep(1/rps-time.time()+t_start)
            return result
        return wrapper
    return decorator       
timeout.counter=0 
