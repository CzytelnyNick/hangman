import time
import os
import random

words= ["piesek","kotecek","mialemtakiegopsa"]
wordsChoice = random.randint(0,2)
word = words[wordsChoice]
hangman = [""" 
______
|/   |
|   
|    
|    
|    
|
|_____
""",
"""
______
|/   |
|   (_)
|    
|    
|    
|
|_____
""",
"""
______
|/   |
|   (_)
|    |
|    |    
|    
|
|_____
""",
"""
______
|/   |
|   (_)
|   \|
|    |
|    
|
|_____
""",
"""
______
|/   |
|   (_)
|   \|/
|    |
|    
|
|_____
""",
"""
______
|/   |
|   (_)
|   \|/
|    |
|   | 
|
|_____
""",
"""
______
|/   |
|   (_)
|   /|\\
|    |
|   | |
|
|_____
"""]
h=0
j=0
while(True):
    for x in word:
        print("_", end="")
    letter = input("\nPODAJ LITERE ")
    
    # len(word)
    

    for i in word:
        
        if(i != letter): 
            print(i)
            print(word)
        
    if (i == letter):
        print(hangman[h])    
        h= h+1
        time.sleep(2)
        os.system('cls')
        print(word)
        if h == 7: 
            
            print("PRZEGROŁEŚ")
            break
