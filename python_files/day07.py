print("😀 Fake Fan Finder 😎")
print("-----------------------")
tvshow = input("What is your favourite vampire TV show?")
if tvshow == "Vampire Diaries":
    print("Cool, I like it too.")
    mmc = input("Are you Stefan or Damon fan?")
    if mmc == "Stefan":
        print("Yes, he's a goodie.")
    elif mmc == "Damon":
        print("Stand in line!")
    else:
        print("Sorry, do you even know the show?")
elif tvshow == "Twilight":
    format = input("Is it even a TV show?")
    if format == "no":
        print("Exactly!")
        mmc = input("So who is your favourite?")
        if mmc == "Edward":
            print("Sparkly!")
        elif mmc == "Jacob":
            print("Mmmm, hot!")
        else:
            print("You're thinking outside of the box, I like it!")
    else:
        print("Sorry, I don't think you've actually seen it.")
else:
    print("I haven't seen it, you probably are a fan.")
