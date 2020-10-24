#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 12:55:30 2020

@author: ordovas
"""
from hangman_ascii import *


wordd = "BABA YETU YETU"

gss=set(["A","T"]) 
ch=set(["A","T","X"])

def print_word(word, guess):
    string_word = "   "
    for el in word:
        if el in guess:
            string_word += el+" "
        elif el == " ":
            string_word += "    "
        else:
            string_word += "_ "
    return string_word


def print_chosen(lst):
    string_letters = "Letras Usadas: "
    for el in lst:
        string_letters += el+" "

    return string_letters

def print_guess(lst):
    string_letters = "Letras Adivinadas: "
    for el in lst:
        string_letters += el+" "

    return string_letters

#wdd= print_word(word,)
#print(wdd)
hangman = get_ascii_hangman()[1:-1]

def printing_progress(word,counter,used, guess,hangman):
    print(hangman[counter])
    print(print_chosen(used))
    print(print_guess(guess))
    print("\n")
    print(print_word(word, guess))
    print("\n\n")


printing_progress(wordd, 5, ch, gss, hangman)
    
    
    

