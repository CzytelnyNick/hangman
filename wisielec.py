
import os
import random

words= ["piesek","kotecek","mialemtakiegopsa"]
wordsChoice = random.randint(0,2)
word = words[wordsChoice]
hangman0 = """ 
____
|/   |
|   
|    
|    
|    
|
|_____
"""
hangman1="""
 ____
|/   |
|   (_)
|    
|    
|    
|
|_____
"""
hangman2="""
 ____
|/   |
|   (_)
|    |
|    |    
|    
|
|_____
"""
hangman3 = """
 ____
|/   |
|   (_)
|   \|
|    |
|    
|
|_____
"""
hangman4="""
 ____
|/   |
|   (_)
|   \|/
|    |
|    
|
|_____
"""
hangman5="""
 ____
|/   |
|   (_)
|   \|/
|    |
|   | 
|
|_____
"""
hangman6="""
 ____
|/   |
|   (_)
|   /|\\
|    |
|   | |
|
|_____
"""
j=0
while(True):
    
    letter = input("PODAJ LITERE")

    # len(word)
    for x in word:
        print("_", end="")

    for i in word:
          
        if(i == letter): 
            print(tab[word[i]])
