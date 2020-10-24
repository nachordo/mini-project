#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 12:11:08 2020

@author: Ignacio Ordovas
"""
import os
import numpy as np
import random
from hangman_ascii import *
from chose_word import *

hangman = get_ascii_hangman()


def core_hangman_game():
    word = "CACAHUE"
    word_splitted = [letter for letter in word]
    letters_in_word = set(word_splitted) - set(" ")
    alphabet = [i for i in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"]
    
    letters_chosen = []
    letters_guessed = []
    win_trigger = False
    game_on = True

    letter = ""

    while game_on:
        letter = input("Escoge una letra: ")
        letter = letter.upper()
        while (letter in letters_chosen) or (len(letter) != 1):
            if letter in letters_chosen:
                print("Ya has elegido anteriormente esa letra...")
                letter = input("Escoge una letra: ")
            elif len(letter) != 1:
                print("UNA letra...")
                letter = input("Escoge una letra: ")
            elif not(letter in alphabet):
                print("Una LETRA...")
                letter = input("Escoge una letra: ")
                    
        letters_chosen += [letter]
        if letter in word_splitted:
            letters_guessed += [letter]
            
        print("USADAS: ", letters_chosen)
        print(letters_guessed)

        print(letters_in_word)
        
        if set(letters_guessed) == letters_in_word:
            win_trigger = True
        
        print(letter != '0' , not(win_trigger),letter != '0' or not(win_trigger))
        #os.system("clear")
        
    
core_hangman_game()
