#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 09:55:16 2019

@author: angelineflorajohn
"""

low = 0
high = 100
userInput = ''
print('Please think of a number between 0 and 100!')
while userInput != 'c':
    guess = (low+high)/2
    userInput = input('Is your secret number ' + str(int(guess)) + '?' + "\nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if userInput == 'l':
        low = guess
    elif userInput == 'h':
        high = guess
    else:
        print('Wrong input. Try again!')
print('Game over. Your secret number was: ' + str(int(guess)))


