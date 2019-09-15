#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 11:51:20 2019

@author: angelineflorajohn
"""

def func_a():
    print('inside a')

def func_b(y):
    print('inside b')
    return y

def func_c(z):
    print('inside c')
    return z()

print(func_a())
print(func_b(2) + 5)
print(func_c(func_a))