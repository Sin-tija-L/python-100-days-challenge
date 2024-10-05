# 👉 Day 46: 2D Dictionaries

<a href="https://youtu.be/mn1n5db71to?si=B7Cf5qDdprFr71TV" target="_blank">📹 Dāvida video</a>


Oh yes, dictionaries are back. That can mean only one thing. It's time to make the lawyers nervous again with the return of Mokébeasts! Yay!

You'll have to wait for your beast fix though.

First, our examples will focus on the completely original board game of 'A murder has happened in a room with a weapon and you have to guess who did it'. 😆

Nice. Catchy.

Remember that dictionaries are very similar to lists, except that they store data as key:value pairs. The value is what it's worth and the key is what it is called. The key is used to access the value, and keys are more meaningful than index numbers.

Today we are going to expand our mad dictionary skills into the second dimension.

<img id="image" src="assets/day46_1.png" alt="Replit Workspace Overview" width="960">


## Dynamically Adding To A 2D Dictionary

👉 This code dynamically adds to a 2D dictionary by starting with an empty dictionary and using an infinite loop to add user input.

```python
clue = {}

while True:
  name = input("Name: ")
  location = input("Location: ")
  weapon = input("Weapon: ")

  clue[name] = {"location": location, "weapon":weapon} #line 7

  print(clue)
```

The real magic happens on the 7th line of code. Instead of using `.append()` like we would with a list, we create a new dictionary entry.

The key is the name of the beast, but the value is a whole new dictionary that contains the details of the beast.

Each key:value pair in the dictionary is now a key that accesses a related dictionary.

Look at the output and you can see the new dictionary nested inside the first one.

<img id="image" src="assets/day46_2.png" alt="Replit Workspace Overview" width="960">

👉 Can you try this code out with Lady Blurple with a rope in the study?


## Pretty Printing

👉 This example shows you how to add a `prettyPrint()` subroutine that works with a 2D dictionary.

```python
def prettyPrint():
  print()
  
  for key, value in clue.items():
    # moves along every 'key:subDictionary' pair and outputs the key (the name of the character).
    print(key, end=": ")
    for subKey, subValue in value.items():
      # (nested) `for` loop moves along every subkey and subvalue in each subDictionary.
      print(subKey, subValue, end=" | ")
    print()
```

When combined with the 2D dictionary code:

```python
clue = {}
def prettyPrint():
  print()
  
  for key, value in clue.items():
    # moves along every 'key:subDictionary' pair and outputs the key (the name of the character).
    print(key, end=": ")
    for subKey, subValue in value.items():
      # (nested) `for` loop moves along every subkey and subvalue in each subDictionary.
      print(subKey, subValue, end=" | ")
    print()
    
while True:
  name = input("Name: ")
  location = input("Location: ")
  weapon = input("Weapon: ")

  clue[name] = {"location": location, "weapon":weapon} 

  prettyPrint()
```
the output looks like this.

<img id="image" src="assets/day46_3.png" alt="Replit Workspace Overview" width="960">


## Accessing a Single Item

To access a single item in a 2D dictionary, we use two square brackets just like with a 2D list.

👉 This example stores users' data about their 100 Days Of Code progress. Note how I've set each one up as a 1D dictionary before storing them all in a 2D dictionary.

```python
john = {"daysCompleted": 46, "streak": 22}
janet = {"daysCompleted": 21, "streak": 21}
erica = {"daysCompleted": 75, "streak": 6}

courseProgress = {"John":john, "Janet":janet, "Erica":erica}

print(courseProgress)
```

👉 To access one item, I use two square brackets []. So to see only Erica's results, I would add:

```python
print(courseProgress["Erica"])
# The bracket contains the key that references the sub dictionary.
```

👉 What if we only want to see how many days Erica has completed?

```python
john = {"daysCompleted": 46, "streak": 22}
janet = {"daysCompleted": 21, "streak": 21}
erica = {"daysCompleted": 75, "streak": 6}

courseProgress = {"John":john, "Janet":janet, "Erica":erica}

print(courseProgress["Erica"]["daysCompleted"])
# The first bracket contains the key that references the sub dictionary. The second bracket contains the key that references the sub item. This will output '75'.
```

## Common Errors

First, delete any other code in your `day46.py` file. Copy each code snippet below into `day46.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

### Key Error

👉 Why am I getting the 'key error'... error?

```python
john = {"daysCompleted": 46, "streak": 22}
janet = {"daysCompleted": 21, "streak": 21}
erica = {"daysCompleted": 75, "streak": 6}

courseProgress = {"John":john, "Janet":janet, "Erica":erica}

print(courseProgress["Erica"]["daysComplete"])
```

<details>
<summary>👀 Answer</summary>

I had tried to reference 'daysComplete' on the last line. This key doesn't exist. It's called 'daysCompleted' in the code.

```python
john = {"daysCompleted": 46, "streak": 22}
janet = {"daysCompleted": 21, "streak": 21}
erica = {"daysCompleted": 75, "streak": 6}

courseProgress = {"John":john, "Janet":janet, "Erica":erica}

print(courseProgress["Erica"]["daysCompleted"])
```

</details>

## Fix My Code

👉 Try and fix this code which is full of errors.

First, delete any other code in your `day46.py` file. Copy each code snippet below into `day46.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

```python
john = {"daysCompleted": 46, "streak": 22}
janet = {"daysCompleted": 21, "streak": 21}
erica = {"daysCompleted": 75, "streak": 6}

courseProgress = {"John":john, "Janet":janet, "Erica":erica}

print(courseProgress["erica"]["daysCompleted"])
print(courseProgress["Janet"]["Streak"])
```

<details>
<summary>👀 Answer</summary>

- This was subtle (on purpose). 'Erica' and 'streak' are incorrect in the `print` statement.

```python
john = {"daysCompleted": 46, "streak": 22}
janet = {"daysCompleted": 21, "streak": 21}
erica = {"daysCompleted": 75, "streak": 6}

courseProgress = {"John":john, "Janet":janet, "Erica":erica}

print(courseProgress["Erica"]["daysCompleted"])
print(courseProgress["Janet"]["streak"])
```

</details>

# 👉 Day 46 Challenge

Today, you're going to program a full on Mokébeast Mokédex. Yep, think we're getting away with it so far...

Don't forget, you can reuse your code from **Day 42** here.

Your Mokédex should:
1. Store multiple Mokébeasts using a loop.
2. Get user input of the beasts' details.
3. Add the details to a 2D dictionary.
4. Repeat until the user wants to stop.
5. Output the full Mokédex using a `prettyPrint()` function.

Example:

<img id="image" src="assets/day46_4.png" alt="Replit Workspace Overview" width="960">

<details>
<summary>💡 Hints</summary>

- Not much here you can't get from the examples on pages 1 and 2 for today.
- Think about what you can add to make the spacing look nice? (fstrings, `>`, etc.)

</details>

## Solution (No Peeking!)

<a href="https://youtu.be/fcdIMAXYqsQ?si=38W3vo6Wf1enbcGm" target="_blank">Solution video</a>

<details>
<summary>👀 Answer</summary>

```python
beasts = {}

def prettyPrint():
  print()
  
  for key, value in beasts.items():
    for subKey, subValue in value.items():
      print(subKey,": ", subValue, end=" | ")
    print()
    
print("🌟MokeBeast Generator🌟")
print()
while True:
  name = input("Input the beast name > ")
  element = input("Input the beast element > ")
  move = input("Input the beast special move > ")
  startingHP = input("Input the beast starting HP > ")
  startingMP = input("Input the beast starting MP > ")
  beasts[name] = {"name": name, "element": element, "move": move, "startingHP": startingHP, "startingMP": startingMP}
  print()
  prettyPrint()
  end = input("Again? y/n > ").strip().lower()
  if end == "n":
    break
```

</details>