## Animal sounds (while loop game)

game = ""

while game != "no":
    animal = input("What animal sound do you want?")
    if animal == "dog":
        print("Dog says woof woof")
    elif animal == "cat":
        print("Cat says meouw")
    elif animal == "cow":
        print("Cow says mooo")
    else:
        print("Sorry, I don't know this.")
    game = input("Do you want to ask another sound?")

print("Thanks for playing! See you next time.")