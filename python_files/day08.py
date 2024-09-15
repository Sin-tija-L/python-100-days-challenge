print("Welcome!")
name = input("What is your name?")
print("Hello", name, "! Nice to meet you!")
day = input("What day is today?")
if day == "Monday":
    print("Ooof, I hate mondays.")
    mood = input("Are you feeling energized today?")
    if mood == "yes":
        print("Awesome!")
        choice = input("Are you looking for a joke or an advice?")
        if choice == "joke":
            print("Funny joke about Mondays.")
        elif choice == "advice":
            print("Monday is  a good day to starts something new,", name, "!")
        else:
            print("Can't help you with that.")
    else:
        print("I see. Here's some energy bombs for you. 💣💣💣")
elif day == "Tuesday":
    print("Tuesdays are cool. That's when the actual work starts.")
    mood = input("Do you have a lot planned for today?")
    if mood == "yes":
        print("You will rock it,", name, "!")
    else:
        print("It's not too late to plan something grand.")
        goal = input("What would you like to achieve in life?")
        print("Great! Take action on", goal, "!")
elif day == "Wednesday":
    print("It's the middle of the workweek.")
    mood = input("Have you managed to achieve something this week?")
    if mood == "yes":
        print("I'm proud of you!")
    else:
        choice = input("Would you like to change it")
        if choice == "yes":
            obstacle = input("What stands in your way?")
            print("I'm sure you can deal with it. Soon", obstacle, "will not be in your way and you will be victorious.")
        else:
            print("There's nothing wrong with living at ease.")
elif day == "Thursday":
    print("It's almost Friday.")
    mood = input("On the scale form 1 to 10, how happy are you about the upcoming week-end?")
    if mood == "1" or mood == "2":
        print("Honney, I'm worried about you.")
    elif mood == "3" or mood == "4":
        print("It seems like something is bothering you.")
    elif mood == "5":
        print("Average results. I think you're better than that.")
    elif 5 < int(mood) and int(mood) < 9:
        print("Pretty exciting, right?")
    else:
        print("That's the spirit!")
elif day == "Friday!":
    print("Yeah, baby! Thank god it's Friday!")
else:
    print("Sorry, I'm out of office. Get back to me on Monday.")
