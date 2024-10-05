## Name the lyrics game

print("Let's play a game. Can you guess the missing word?")

guesses = 1

while True:
    print("Never gonna ____ you up!")
    word = input("What is the missing word?")
    if word == "give":
        if guesses == 1:
            print("Correct! And on your first guess!")
        else:
            print("Correct! It took you", guesses, "guesses.")
        break
    else:
        print("Nope, try again!")
        guesses += 1