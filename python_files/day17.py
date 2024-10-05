## Rock, paper, Scissors

from getpass import getpass as input

victoryPlay1 = 0
victoryPlay2 = 0
rounds = 1

while True:
    print("Round", rounds)
    
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
            victoryPlay2 += 1
        else:
            print("Player 1 wins, crushing opponent's scissors with a rock.")
            victoryPlay1 += 1
            
    elif play1 == "S":    
        if play2 == "P":
            print("Player 1 wins cutting opponent's paper with scissors.")
            victoryPlay1 += 1
        else:
            print("Player 2 wins, crushing opponent's scissors with a rock.")
            victoryPlay2 += 1
            
    elif play1 == "P":    
        if play2 == "S":
            print("Player 2 wins cutting opponent's paper with scissors.")
            victoryPlay2 += 1
        else:
            print("Player 1 wins with a paper over rock.")
            victoryPlay1 += 1
    
    rounds +=1
    
    if victoryPlay1 == 3:
        print("You've played", rounds, "rounds.")
        print("Player 1 won 3 rounds! you emerge victorious!")
        break
    elif victoryPlay2 == 3:
        print("Player 2 won 3 rounds! you emerge victorious!")
        break
    else:
        continue