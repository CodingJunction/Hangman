import random
words=["abruptly","affix","awkward","bagpipes","beekeeper","cobweb","crypt","disavow","dog","fragile","galaxy","ivory","ballon"]
word=random.choice(words)
chances=6
condition=True
stages=['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


print("""
  ___ ___                                              
 /   |   \_____    ____    ____   _____ _____    ____  
/    ~    \__  \  /    \  / ___\ /     \\__  \  /    \ 
\    Y    // __ \|   |  \/ /_/  >  Y Y  \/ __ \|   | \\
 \___|_  /(____  /___|  /\___  /|__|_|  (____  /___|  /
       \/      \/     \//_____/       \/     \/     \/ 

Welcome to the Hangman game
You have only 6 lives to guess correct word
Best of luck !!!

""")
display=["_" for i in range(len(word))]
#print('Final answer', word)
while chances>0:
    k=0
    guess=input('Enter a guess letter : \n').lower()
    for i in range(len(word)):
        if word[i]==guess:
            if display[i]=="_":
                display[i]=guess
                k=1
                break
                
    for i in display:
        print(i,end=" ")
    print()
    if k==0:
        print('Wrong guess, one chance lost')
        chances-=1
    
    print("Number of chances remaining",chances)
    print(stages[6-chances])
    if "_" not in display:
        chances=0

if "_" not in display:
    print("Congratulations")
    print("You have won the game")
    print("You have guesses the word correctly")
    print("The word is : ",word)
else:
    print("You lose.")
    print("You have guesses the word incorrectly")
    print("The word is : ",word)


    
        

