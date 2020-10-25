# Hangman 
## An Ironhack game-project by Ignacio Ordovás

Welcome to my version of the Hangman game! Sit and enjoy :) 

The only thing you need to do to execute this game is to execute the “hangman-main.py” file in the terminal. Then you must follow the instructions.

The game language is spanish, as it is the one used in the classes. The comments in the python files are in english so more people can check and get ideas from my code.

In the game you must select a category in order to guess the word/names/etc. related to this category. The program asks the user to type the category from the ones that are available. The input is not case sensitive nor is affected accents, but you must be careful to not introduce extra spaces. The game will continue asking for an input until a valid choice is given.

In the hangman game, you can enter the letters in lowercase or uppercase, it is the same. But the program will not accept more than one character, numbers, special characters or spaces. Nevertheless, the game will ask again and again for a valid input.

If the letter is not present in the word that you have to guess, the game will increase your failure count. Of course, you are only allowed to fail several times. Watch the face of the hanged man to see how good/bar are you doing! The game will tell you when there is only one trial left.

When the game is finished, you can choose to play another round or close the game.



### Modding the game

You can easily mod this game adding additional categories to use your favourite themes or removing ones that you may find silly. The procedure is the following:

- You must create a txt file with the name of your category, separating with _ the words of the name of the category. For example, “stupid_category.txt” will be displayed in the game as “Stupid category”.

- Fill the file with one input to be guessed for each line, without accents. The program will get all the characters of each line to be the string to guess, so you can use for example a name and a surname. This means you can put spaces, but it is encouraged to only put them to separate for example the name and the surname, and not at the beginning or at the end of the string.

- Don’t leave empty lines!

- Place this file in the “words” folder, and that’s it!



### Possible future modifications

I find the game awesome as it is uploaded! but there are always some improvements that can be implemented. Due to the very limited time to to complete this project I chose to not complicate the game excessively and implement only a limited set of cool things. Here I list some possible improvements:

- There are words in spanish with accents, and when the words are displayed I choose to not show accents. I may need to tell the program that “A” and “Á” are the same letter, but they are not the same character!. It is possible to do it in a reasonable amount of time I think, but is certainly not immediate.

- I could improve the program adding difficulty levels (different lives, biasing the random method to select more often words with different type of letters)

- Just for curiosity, I may show a description of the guess at the end of the game (may be useful for teaching purposes). THis implementation requires adding this for each word. 

