#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 11:54:00 2019

@author: angelineflorajohn
"""
"""
Scope example
    -- Inside a function, can access a variable defined outside
    -- Inside a function, cannot modify a variable defined outside
"""

#Example 1:
def f(y):
    x = 1
    x += 1
    print(x)

x = 5
f(x)
print(x)

#Example 2:
def g(y):
    print(x)
    print(x + 1)

x = 5
g(x)
print(x)

#Example 3:
def g(x):
    def h():
        x = 'abc'
    x = x + 1
    print('in g(x): x = ', x)
    h()
    return x

x = 3
z = g(x)
print('z = ', z)


#Example last:
def h(y):
    x = x + 1

x = 5
h(x)
print(x)

