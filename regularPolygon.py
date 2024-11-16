#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 19:08:26 2019

@author: ajohn
"""
'''
A regular polygon has n number of sides. Each side has length s.

The area of a regular polygon is:  (0.25 * n * s**2) / tan(pi/n)
The perimeter of a polygon is: length of the boundary of the polygon
Write a function called polysum that takes 2 arguments, n and s. This function should sum the area and square of the perimeter of the regular polygon. The function returns the sum, rounded to 4 decimal places.
'''
import math
# math library contains the functions to perform mathematical functions
def polysum(n, s):
    '''
    Input: 
        n is the number of sides of a regular polygon
       ,s is the length of the side of the polygon
    Output: adding the area and square of the perimeter of the regular polygon rounded to 4 decimal places
    '''
    area = (0.25 * n * s**2) / math.tan(math.pi/n)
    perimeter = n * s
    return round(area + perimeter**2, 4)

