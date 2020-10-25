#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 12:11:08 2020

@author: Ignacio Ordovas
"""
import os
import random
from hangman_ascii import *
from chose_word import *
from printing_game import *



def core_hangman_game():
    os.system("clear")
    
    #The player is asked for a category and the program chooses a random word among it
    word = guess_word_workflow()
    #The program obtains the different letters of the 
    word_splitted = [letter for letter in word]
    letters_in_word = set(word_splitted) - set(" ")
    
    #Setting up the necessary variables
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
    
    #Clears screen
    os.system("clear")
    while game_on:
        #Begining the game, the hangman is printed
        #with its current progress, and the list og the used
        #and guessed letters
        printing_progress(word,fail_count,letters_chosen, letters_guessed,hangman_screen)
        
        #The program asks for a letter 
        letter = input_letter(letters_chosen)
        
        #It piles up the letter with the used ones
        letters_chosen += [letter]
        
        #Checks if the player guesed it
        if letter in word_splitted:
            letters_guessed += [letter]
        else:
            fail_count +=1
            
        
        #Checks if the player has won
        if set(letters_guessed) == letters_in_word:
            win_trigger = True
            game_on = False
        
        #Checks if the player has lost
        if fail_count == len(hangman_screen):
            game_on = False
         
        #Clears screen    
        os.system("clear")
    
    #The game is finished, so it prints either the victory or game over screen
    if win_trigger:
        print(victory_screen)
        print("\n\n Solución:  ",print_word(word, letters_in_word),"\n\n")
    else:
        print(gameover_screen)
        print("\n\n Solución:  ",print_word(word, letters_in_word),"\n\n")
    
    return win_trigger

