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
zycia=0
hangmanCheck = True
wordTab = []
z = 0;
while (len(word) > z):
    wordTab.append("_")
    z+=1

while(h <= 6):
    if hangmanCheck == False:
            print("\n")
            print(wordTab)
            
            
    hangmanCheck = True

    letter = input("\nPODAJ LITERE ")

    # len(word)

    for i in range(len(word)):

        if(word[i] == letter): 
            
            # print(i, end="")
            wordTab[i] = letter
            hangmanCheck = False
           
        else: 
            k = "_"
            # s1 = ('i', [1, 2, 3])
            # print(word.index(i))



    
    if (hangmanCheck == True):

        print(hangman[h])    
        h= h+1
        time.sleep(2)
        os.system('cls')
print("PRZEGROŁEŚ")
