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
def fair(user_move):

    import random
    
    #the random move is based on a random number between 1 and 100
    #if the random number is between 1 and 33 then the computer plays Rock
    #if the random number is between 34 and 66 then the computer plays Paper
    #if the random number is between 67 and 100 then the computer plays Scissors
    
    random_move = random.randint(1, 100)

    if random_move >= 1 and random_move <= 33:
        pc_move = 1
    
    elif random_move >= 34 and random_move <= 66:
        pc_move = 2
    
    elif random_move >= 67 and random_move <= 100:
        pc_move = 3

    if pc_move == user_move:
        print("Both chose the same! Tie!\n")

    if pc_move == 1 and user_move == 2:
        print("Rock! You won!\n")

    if pc_move == 1 and user_move == 3:
        print("Rock! I won!\n")

    if pc_move == 2 and user_move == 3:
        print("Paper! You won!\n")

    if pc_move == 2 and user_move == 1:
        print("Paper! I won!\n")

    if pc_move == 3 and user_move == 1:
        print("Scissors! You won!\n")

    if pc_move == 3 and user_move == 2:
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
    
    user_move_string = input("[R]ock, [P]aper or [S]cissor? ")

    if user_move_string == "R" or user_move_string == "r":
        usermoveint = 1

    elif user_move_string == "P" or user_move_string == "p":
        usermoveint = 2

    elif user_move_string == "S" or user_move_string == "s":
        usermoveint = 3

    elif user_move_string == "exit" or user_move_string == "Exit" or user_move_string == "EXIT":
        count = 2
        usermoveint = 0

    if game == "1":
        fair(usermoveint)

    elif game == "2":
        lose(usermoveint)

    elif game == "3":
        win(usermoveint)

print("Thanks for playing!\n")