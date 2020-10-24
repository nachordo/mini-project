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




def core_hangman_game():
    word = "CACAHUE"
    word_splitted = [letter for letter in word]
    letters_in_word = set(word_splitted) - set(" ")
    alphabet = [i for i in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"]
    
    letters_chosen = []
    letters_guessed = []
    win_trigger = False
    game_on = True
    fail_count = 0

    letter = ""
    hangman_ascii_art = get_ascii_hangman()
    hangman_screen = hangman_ascii_art[1:-1]
    victory_screen = hangman_ascii_art[0]
    gameover_screen = hangman_ascii_art[-1]
    
    
    while game_on:
        #Begining the game, the hangman is printed
        #with its current progress, and the list og the used
        #and guessed letters
        printing_progress(word,counter,used, guess,hangman)
        
        #The program asks for a letter 
        letter = input("Escoge una letra: ")
        letter = letter.upper()
        
        #We continue asking for a letter if it is not a valid option
        #(a previously chosen one, more than one character or not a letter)
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
        
        #It piles up the letter with the used ones
        letters_chosen += [letter]
        
        #Checks if the player guesed it
        if letter in word_splitted:
            letters_guessed += [letter]
        else:
            fail_count +=1
            
        print("USADAS: ", letters_chosen)
        print(letters_guessed)

        print(letters_in_word)
        
        if set(letters_guessed) == letters_in_word:
            win_trigger = True
        
        print(letter != '0' , not(win_trigger),letter != '0' or not(win_trigger))
        #os.system("clear")
        
    
core_hangman_game()
