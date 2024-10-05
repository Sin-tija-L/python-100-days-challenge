## Guess the number game

from sys import exit
import random

number = random.randint(1, 1000000)
print(number)
takes = 0
print("")

while True:
    
    guess = int(input("Can you guess my number? > "))
    takes += 1
    
    if guess < 0:
        print("Was I not clear?")
        exit()
    elif guess < number:
        print("Too low")
        print("")
    elif guess > number:
        print("Too high")
        print("")
    elif guess == number:
        if takes == 1:
            print("Wow, are you a mindreader? You guessed it on your first attempt!")
        else:
            print("Exactly! You did it in", takes, "guesses.")
        break
    