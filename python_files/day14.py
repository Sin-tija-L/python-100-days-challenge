## Rock, paper, Scissors

##from getpass import getpass as input

play1 = input("Player 1, pick your weapon (R, P or S): ")
if play1 == "R" or play1 == "P" or play1 == "S":
    print("Good choice!")
else:
    print("Is that a new weapon? Try again!")
    play1 = input("Player 1, pick your weapon (R, P or S): ")
    
play2 = input("Player 2, pick your weapon (R, P or S): ")
if play2 == "R" or play2 == "P" or play2 == "S":
    print("Good choice!")
else:
    print("Is that a new weapon? Try again!")
    play1 = input("Player 1, pick your weapon (R, P or S): ")

if play1 == play2:
    print("It's a tie! Try again!")
    
elif play1 == "R":    
    if play2 == "P":
        print("Player 2 wins with a paper over rock.")
    else:
        print("Player 1 wins, crushing opponent's scissors with a rock.")
        
elif play1 == "S":    
    if play2 == "P":
        print("Player 1 wins cutting opponent's paper with scissors.")
    else:
        print("Player 2 wins, crushing opponent's scissors with a rock.")
        
elif play1 == "P":    
    if play2 == "S":
        print("Player 2 wins cutting opponent's paper with scissors.")
    else:
        print("Player 1 wins with a paper over rock.")