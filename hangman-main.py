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
from core_game import *


game_playing = True

while game_playing:
    

    core_hangman_game()
    
    continua = input("\n¿Continuar jugando? (SI/NO): ")
    continua = continua.upper()
    
    while not(continua[0]=="S" or continua[0]=="N"):
        continua = input("\n¿Continuar jugando? (SI/NO): ")
        continua = continua.upper()
    
    os.system("clear")
    if continua[0]=="N":
        game_playing=False
        print("\n\nPues lávate los dientes y vete a la cama.\n\n")
        