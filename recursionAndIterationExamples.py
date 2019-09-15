#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 17:09:45 2019

@author: angelineflorajohn
"""

'''
Write an iterative function iterPower(base, exp) that calculates the exponential  baseexp  by simply using successive multiplication. For example, iterPower(base, exp) should compute  baseexp  by multiplying base times itself exp times. Write such a function below.

This function should take in two values - base can be a float or an integer; exp will be an integer  ≥  0. It should return one numerical value. Your code must be iterative - use of the ** operator is not allowed.

'''


def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    answer = base
    if exp > 0:
        for i in range(1, exp):
            answer *= base
    else:
        answer = 1
    return answer

print(iterPower(2,4))
print(iterPower(-5.06, 0))

'''
Write a function recurPower(base, exp) which computes  baseexp  by recursively calling itself to solve a smaller version of the same problem, and then multiplying the result by base to solve the initial problem.

This function should take in two values - base can be a float or an integer; exp will be an integer  ≥0 . It should return one numerical value. Your code must be recursive - use of the ** operator or looping constructs is not allowed.
'''
def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp <= 0:
        return 1
    else:
        return base * recurPower(base, exp - 1)
    
print(iterPower(2,4))
print(iterPower(-5.06, 0))

'''
Exercise: gcd iter
5.0/5.0 points (graded)
ESTIMATED TIME TO COMPLETE: 5 minutes

The greatest common divisor of two positive integers is the largest integer that divides each of them without remainder. For example,

gcd(2, 12) = 2

gcd(6, 12) = 6

gcd(9, 12) = 3

gcd(17, 12) = 1

Write an iterative function, gcdIter(a, b), that implements this idea. One easy way to do this is to begin with a test value equal to the smaller of the two input arguments, and iteratively reduce this test value by 1 until you either reach a case where the test divides both a and b without remainder, or you reach 1.
'''
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    value = min(a, b)
    while True:
        if value == 1:
            return 1
        elif a % value == 0 and b % value == 0:
            return value
        else:
            value -= 1

print(gcdIter(19, 12))           
print(gcdIter(9, 12))
print(gcdIter(17, 12))

'''
The greatest common divisor of two positive integers is the largest integer that divides each of them without remainder. For example,

gcd(2, 12) = 2

gcd(6, 12) = 6

gcd(9, 12) = 3

gcd(17, 12) = 1

A clever mathematical trick (due to Euclid) makes it easy to find greatest common divisors. Suppose that a and b are two positive integers:

If b = 0, then the answer is a

Otherwise, gcd(a, b) is the same as gcd(b, a % b)

See this website for an example of Euclid's algorithm being used to find the gcd.

Write a function gcdRecur(a, b) that implements this idea recursively. This function takes in two positive integers and returns one integer.
'''
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b, a%b)
    
print(gcdIter(19, 12))           
print(gcdIter(9, 12))
print(gcdIter(17, 12))

    
