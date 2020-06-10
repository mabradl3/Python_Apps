#!/usr/bin/env python
# coding: utf-8

# In[126]:

# Tic-Tac-Toe Assignment
# Marshall Bradley
# Orange Cohort
# MSA Fall 1

# Define Request Function -- Asks players to input their position.

def request():
    global position 
    position = input("Choose a position: ")

# Define Turn -- Switches the marker for each player for altnerate turns.

def turn():
    global i
    global marker
    if i == 1 or i == 3 or i == 5 or i == 7 or i == 9:
        marker = "X"
    else:
        marker = "O"

# Define Redo -- Recalls the roundx function if players choose unavailable
    # positions.

def redo():
    global redo
    if redo == 1:
        return roundx()
    else:
        return redo == 0
# Define roundx -- The actual game playing function, takes the position that
    # players choose and adds them to the game board.
    
def roundx():
    global game
    global redo
    if position == "A1" and game[0][0] == 0:
        game[0][0] = marker
    elif position == "A1" and game[0][0] != 0:
        print("Try again!")
        redo = 1
        return redo
    elif position == "B1" and game[0][1] == 0:
        game[0][1] = marker
    elif position == "B1" and game[0][1] != 0:
        print("Try again!")
        redo = 1
        return redo
    elif position == "C1" and game[0][2] == 0:
        game[0][2] = marker
    elif position == "C1" and game[0][2] != 0:
        print("Try again!")
        redo = 1
        return redo
    elif position == "A2" and game[1][0] == 0:
        game[1][0] = marker
    elif position == "A2" and game[1][0] != 0:
        print("Try again!")
        redo = 1
        return redo
    elif position == "B2" and game[1][1] == 0:
        game[1][1] = marker
    elif position == "B2" and game[1][1] != 0:
        print("Try again!")
        redo = 1
        return redo
    elif position == "C2" and game[1][2] == 0:
        game[1][2] = marker
    elif position == "C2" and game[1][2] != 0:
        print("Try again!")
        redo = 1
        return redo
    elif position == "A3" and game[2][0] == 0:
        game[2][0] = marker
    elif position == "A3" and game[2][0] != 0:
        print("Try again!")
        redo = 1
        return redo
    elif position == "B3" and game[2][1] == 0:
        game[2][1] = marker
    elif position == "B3" and game[2][1] != 0:
        print("Try again!")
        redo = 1
        return redo
    elif position == "C3" and game[2][2] == 0:
        game[2][2] = marker
    elif position == "C3" and game[2][2] != 0:
        print("Try again!")
        redo = 1
        return redo 
    else:
        print("Try again!")
        redo = 1
        return redo
    
# Define win -- Checks to see if a player has won the game.    
    
def win():
    global won
    if game[0][0] == game[0][1] == game[0][2] != 0:
        print(marker, "won the game!")
        return 1
    elif game [1][0] == game[1][1] == game[1][2] != 0:
        print(marker, "won the game!")
        return 1
    elif game[2][0] == game[2][1] == game[2][2] != 0:
        print(marker, "won the game!")
        return 1
    elif game[0][0] == game[1][0] == game[2][0] != 0:
        print(marker, "won the game!")
        return 1
    elif game[0][1] == game[1][1] == game[2][1] != 0:
        print(marker, "won the game!")
        return 1
    elif game[0][2] == game[1][2] == game[2][2] != 0:
        print(marker, "won the game!")
        return 1
    elif game[0][0] == game[1][1] == game[2][2] != 0:
        print(marker, "won the game!")
        return 1
    elif game[2][0] == game[1][1] == game[0][2] != 0:
        print(marker, "won the game!")
        return 1
    elif game[0][0] != 0 and game[0][1] != 0 and game[0][2] != 0 and game[1][0] != 0 and game[1][1] != 0 and game[1][2] != 0 and game[2][0] != 0 and game[2][1] != 0 and game[2][2] != 0:
        print("There is a tie.")
        return 1
    else:
        return 0
        
    
# Define tictactoe -- The function that calls the game.    
        
def tictactoe():
    global won
    global game
    global i
    global redo
    won = 0
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    i = 1
    while won == 0:
        print('\n'.join([ str(space) for space in game ]))
        turn()
        request()
        redo = roundx()
        while redo == 1:
            request()
            redo = roundx()
        won = win()
       # print(game, sep="\n")
        i = i + 1
    print('\n'.join([ str(space) for space in game ]))

  
# Do you want to play a game?
      
tictactoe()


# In[ ]:




