#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 12:55:30 2020

@author: ordovas
"""
from library.hangman_ascii import *



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

def printing_progress(word,category,counter,used, guess,hangman):
    print(hangman[counter])
    print("\nCategoría: ",category,"\n")
    print(print_chosen(used))
    print(print_guess(guess))
    print("\n")
    print(print_word(word, guess))
    print("\n\n")


    
    

