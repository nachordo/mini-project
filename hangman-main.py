#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 12:11:08 2020

@author: Ignacio Ordovas
"""
import os
import random
from library.hangman_ascii import *
from library.chose_word import *
from library.printing_game import *
from library.core_game import *


game_playing = True

#Intro screen


while game_playing:
    os.system("clear")
    #Choose the difficulty
    dificulty = choose_difficulty()
    
    #Begins the game
    core_hangman_game(dificulty)
    
    #Asks if the player wants play again
    continua = continue_playing()
    
    os.system("clear")
    if continua[0]=="N":
        game_playing=False
        print("\n\nPues lávate los dientes y vete a la cama.\n\n")
        
