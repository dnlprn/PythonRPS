#function that always returns the losing result
def lose(move):
    
    if move == 1:
        print("Paper! I won!\n")
    
    elif move == 2:
        print("Scissors! I won!\n")
    
    elif move == 3:
        print ("Rock! I won!\n")

#function that always returns the winning result
def win(move):
    
    if move == 1:
        print("Scissors! You won!\n")
    
    elif move == 2:
        print("Rock! You won!\n")
    
    elif move == 3:
        print ("Paper! You won!\n")

#function that randomizes the computer move making the game fair
def fair(usermove):

    import random
    
    #the random move is based on a random number between 0 and 99
    #if the random number is between 0 and 33 then the computer plays Rock
    #if the random number is between 34 and 66 then the computer plays Paper
    #if the random number is between 67 and 99 then the computer plays Scissors
    
    randomove = random.randint(0, 99)

    if randomove >= 0 and randomove <= 33:
        pcmove = 1
    
    elif randomove >= 34 and randomove <= 66:
        pcmove = 2
    
    elif randomove >= 67 and randomove <= 99:
        pcmove = 3

    if pcmove == usermove:
        print("Both chose the same! Tie!\n")

    if pcmove == 1 and usermove == 2:
        print("Rock! You won!\n")

    if pcmove == 1 and usermove == 3:
        print("Rock! I won!\n")

    if pcmove == 2 and usermove == 3:
        print("Paper! You won!\n")

    if pcmove == 2 and usermove == 1:
        print("Paper! I won!\n")

    if pcmove == 3 and usermove == 1:
        print("Scissors! You won!\n")

    if pcmove == 3 and usermove == 2:
        print("Scissors! I won!\n")

#game introduction strings
print("Welcome to Rock Paper Scissors. Please choose the game mode.\n")
print("1) Fair game")
print("2) You always lose")
print("3) You always win\n")
print("Just type 'exit' when you want to finish.\n")

game = input("Enter your value: ")

#conferms the choice made
if game == "1":
    print("Ok, you have chosen a fair game.\n")

elif game == "2":
    print("Ok, you have chosen to always lose.\n")

elif game == "3":
    print("Ok, you have chosen to always win.\n")

#the computer will keep playing until the player writes 'exit'

count = 1

while count != 2:
    
    usermovestr = input("[R]ock, [P]aper or [S]cissor? ")

    if usermovestr == "R" or usermovestr == "r":
        usermoveint = 1

    elif usermovestr == "P" or usermovestr == "p":
        usermoveint = 2

    elif usermovestr == "S" or usermovestr == "s":
        usermoveint = 3

    elif usermovestr == "exit" or usermovestr == "Exit" or usermovestr == "EXIT":
        count = 2
        usermoveint = 0

    if game == "1":
        fair(usermoveint)

    elif game == "2":
        lose(usermoveint)

    elif game == "3":
        win(usermoveint)

print("Thanks for playing!\n")