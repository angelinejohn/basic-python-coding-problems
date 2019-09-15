#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 11:40:34 2019

@author: angelineflorajohn
"""
"""
Write a Python function, square, that takes in one number and returns the square of that number.

This function takes in one number and returns one number.
"""

def square(n):
    """
    Input:  a parameter number n either int or float.
    Output: square of n (n**2)
    """
    return n**2

print(square(3))
print(square(3.14))

def fourthPower(x):
    '''
    x: int or float.
    '''
    return square(square(x))

print(fourthPower(3))


def odd(x):
    '''
    x: int

    returns: True if x is odd, False otherwise
    '''
    return x % 2 != 0

print(odd(2))
print(odd(17))




