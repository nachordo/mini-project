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
     


def process_word(word):
    #Sets up the string of the chosen category to load the module
    processed_word=word.lower().replace(" ","_")
    processed_word = processed_word.replace("á","a")
    processed_word = processed_word.replace("é","e")
    processed_word = processed_word.replace("í","i")
    processed_word = processed_word.replace("ó","o")
    processed_word = processed_word.replace("ú","u")
    processed_word = processed_word.replace("ü","u")
    processed_word = processed_word.replace("ñ","n")
    return processed_word

    
def input_word_modules(word_modules):
    #Print possible categories
    print("Categorías disponibles en el juego:")
    print_word_modules(word_modules)
    
    #Choosing a category
    print("\n\n")
    election = input("Escoge una categoría (o 'Sorpresa' para escoger una al azar): ")
    election = process_word(election)
    
    #Chooses a random category if the player wants
    if election.lower() == ("sorpresa"):
        election = random.sample(word_modules, 1)[0]
    
    #Continue asking for a valid option
    while not(election in word_modules):
        election = input("Escoge una categoría correcta: ")
        election = process_word(election)
        if election.lower() == ("sorpresa"):
            election = random.sample(word_modules, 1)[0]
    
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

def guess_word_workflow():
    word_modules = load_word_modules()
    #print_word_modules(word_modules)
    election = input_word_modules(word_modules)
    word_to_guess = choosing_word(election)
    return word_to_guess,election.replace("_"," ").capitalize()


def input_letter(letters_chosen):
    letter = input("Escoge una letra: ")
    letter = letter.upper()
    alphabet = [i for i in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"]
    
    #We continue asking for a letter if it is not a valid option
    #(a previously chosen one, more than one character or not a letter)
    while ((letter in letters_chosen) or (len(letter) != 1)) or not(letter in alphabet):
        if letter in letters_chosen:
            print("Ya has elegido anteriormente esa letra...")
            letter = input("Escoge una letra: ")
            letter = letter.upper()
        if len(letter) != 1:
            print("UNA letra...")
            letter = input("Escoge una letra: ")
            letter = letter.upper()
        if not(letter in alphabet):
            print("Una LETRA...")
            letter = input("Escoge una letra: ")
            letter = letter.upper()

    return letter
