#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 11:45:28 2019

@author: angelineflorajohn
"""
"""
Write a Python function, evalQuadratic(a, b, c, x), that returns the value of the quadratic  𝑎⋅𝑥2+𝑏⋅𝑥+𝑐 .

This function takes in four numbers and returns a single number.
"""

def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    return a * x**2 + b * x + c

print(evalQuadratic(1,2,3,10))


