#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 00:40:10 2019

@author: ajohn
"""
"""
Problem Statement: Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. 
For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

"""

s = 'ABCBCD'
current = ''
longest = ''
previous = ''
for i in s:
    if previous <= i:
        current += i
        if len(current) > len(longest):
            longest = current
    else:
        current = i
    previous = i   
print(longest)



#s = 'abcbcd'
#new = ''
#long = ''
#i = 0
#while i < len(s):
#    print(i)
#    if s[i-1] <= s[i]:
#        print("in if at i = ", i)
#        new += s[i]
#        print(new)
#    else:
#        long = new
#        long += s[i]
#        print("long", long)
#    i += 1        
#print(new)
#print("long", long)