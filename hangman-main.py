#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 12:11:08 2020

@author: Ignacio Ordovas
"""
import os
import numpy as np
import random

word = "CACAHUE"
word_splitted = [letter for letter in word]
letters_in_word = set(word_splitted) - set(" ")

letters_chosen = []
letters_guessed = []
win_trigger = False

letter = ""

while (letter != '0' or win_trigger):
    letter = input("Escoge una letra: ")
    while letter in letters_chosen:
        letter = input("Escoge una letra diferente: ")
    
    #os.system("clear")
    letters_chosen += [letter]
    if letter in word_splitted:
        letters_guessed += [letter]
    
    print(letters_guessed)
    
    if set(letters_guessed) == letters_in_word:
        win_trigger = True
    
    
    print(letter != '0' , not(win_trigger),letter != '0' or not(win_trigger))
    
        
    

