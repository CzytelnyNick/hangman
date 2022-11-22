import time
import os
import random
# import numpy as np
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
hangmanCheck = True
wordTab = []
while(True):
    
    
    letter = input("\nPODAJ LITERE ")
    
    # len(word)
    

    for i in word:
        
        if(i == letter): 
            k = i
            print(i, end="")
            hangmanCheck = False
        else: 
            k = "_"
            # s1 = ('i', [1, 2, 3])
            print(word.index(i))
        
         

        
    if (hangmanCheck == True):
            
        print(hangman[h])    
        h= h+1
        time.sleep(2)
        os.system('cls')
        
        if h == 7: 
            
            print("PRZEGROŁEŚ")
            break
    if hangmanCheck == False:
        print(wordTab)

