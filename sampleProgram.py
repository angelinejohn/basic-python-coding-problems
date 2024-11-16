#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 12:08:16 2019

@author: ajohn
"""

def a(x, y, z):
     if x:
         return y
     else:
         return z

def b(q, r):
    return a(q>r, q, r)

print(a(False, 2, 3))
print(b(3, 2))
print(a(3>2, a, b))
print(b(a, b))

