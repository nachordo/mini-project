#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 12:55:30 2020

@author: ordovas
"""
import os
import random

def load_word_modules():
    #This function checks all possible categories that are in the "words" folder
    word_files = os.listdir(path="words/")
    #Only saves the name of the file, not the extension
    word_modules = [ category.split(".")[0] for category in word_files  ]
    return word_modules


def print_word_modules(word_modules):
    #Simple program to print the possible categories, with fancy look
    categories = word_modules
    for element in categories:
        print("   "+element.replace("_"," ").capitalize())
     
    
def input_word_modules(word_modules):
    #Print possible categories
    print("Categorías disponibles en el juego:")
    print_word_modules(word_modules)
    
    #Choosing a category
    election = input("Escoge una categoría: ")
    while not(election.lower().replace(" ","_") in word_modules):
        election = input("Escoge una categoría correcta: ")
    
    return election
        
def choosing_word(election):
    #Load module previously chosen
    file = "words/"+election.lower().replace(" ","_")+".txt"
    with open(file, "r") as f:
        lines = f.readlines()

    #Stores all posible words
    words=[]
    for line in lines:
        words.append(line.split("\n")[0])
    
    #The function returns a random word from the chosen category
    word_to_guess = random.sample(words, 1)[0]
    return word_to_guess.upper()
