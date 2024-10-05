# Day25 - Return Command

<a href="https://www.youtube.com/watch?v=jPF_tAnYY44" target="_blank">Dāvida video</a>

Let's go deeper into subroutines. Can they send information back to the main part of the program?

Let's do this with the `day` command.

<img id="image" src="assets/day25.png" alt="Replit Workspace Overview" width="960">

The `return` command sends some information back to the part of the code that called it. This means the function call is replaced with whatever was returned.

We saw this before with importing libraries and random numbers. We could use the random number wherever we wanted.

## Pin Picker

This subroutine creates a random pin number for us. This subroutine (called `pinPicker`) has the parameter called number (how many `numbers` I want to have in this pin). Then, there is a string (called `pin`) that is empty and a `for` loop that is used to create a defined amount of random numbers. The variable `number` controls how many times the loop will add the new number to the pin. This is done through `+=` and concatenating new values. We will cast the random number as a string so it can be concatenated together.

Then...the magic...we `return` the pin.

👉 Let's see what happens:

```python
#subroutine has parameter called `number`
#`number` shows how many numbers we want the pin to have
def pinPicker(number):
  import random
  pin = "" #this is the empty string
  for i in range(number): #for loop shows defined amount of random numbers
    pin += str(random.randint(0,9)) #we want a string of random numbers between 0-9
  return pin

pinPicker(4) #4 means we want 4 random numbers
```

## Nothing happens? Why?

The line `pinPicker(4)` that calls for a 4 digit pin is being replaced by a 4 digit pin. (That's great, but I don't see that happening...)

We are not telling the computer to do anything with the string that was created. How do we make the string appear?

With `print` of course!

👉 Let's assign a variable to `pinPicker`:

```python
myPin = pinPicker(4)
```

👉 Now print it out:

```python
print(myPin)
```

### 👉 That was quite a doozy. Take time to pause and really try this code out.

## Common Errors

First, delete any other code in your `day25.py` file. Copy each code snippet below into `day25.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

## Nothing is happening

👉 What is the problem here? Why is nothing happening?

```python
def areaOfTriangle(base, height):
  area = 0.5 * base * height
  return area
areaOfTriangle (5, 22)
```

<details>
<summary>👀 Answer</summary>

We need to assign a variable to `areaOfTriangle` and `print` it out.

```python
def areaOfTriangle(base, height):
  area = 0.5 * base * height
  return area

area = areaOfTriangle (5, 22)
print(area)
```

</details>

## Name Error

👉 Why is it saying area is not defined!? We see it inside the subroutine.

```python
def areaOfTriangle(base, height):
  area = 0.5 * base * height
  return area

areaOfTriangle (5, 22)
print(area)
```

<details>
<summary>👀 Answer</summary>

- This is where we see a concept called scope. Scope is a variable only available from inside the region it was created.
- Variables that are created for the first time in a subroutine are only available inside that subroutine.
- We cannot call the variable `area` outside the subroutine.
- We need to create the variable `area` inside the subroutine.

```python
def areaOfTriangle(base, height):
  area = 0.5 * base * height
  return area

area = areaOfTriangle (5, 22)
print(area)
```

</details>

## Fix My Code

👉 Try and fix this code which is full of errors.

First, delete any other code in your `day25.py` file. Copy each code snippet below into `day25.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

```python
def area_square(side1 side2):
  area = side1 * side2
  return area_square
area_square(4, 12)
print(area)
```

<details>
<summary>👀 Answer</summary>

```python
def area_square(side1, side2):
  area = side1 * side2
  return area

area = area_square(4, 12)
print(area)
```

</details>

## 👉 Day 25 Challenge

Let's extend Day 24's project and create a health stats generator for a character in a video game.

1. Create a subroutine that rolls a dice of any size and returns that number.
2. Then, create a second subroutine that rolls one six-sided dice and one eight-sided dice.
3. Multiply the number from the six-sided dice and eight-sided dice together and return that subroutine as a character's health stats for a video game.
4. Print out the character's health stats.
5. Add a loop to give the user the option to generate health stats for another character.

(We genuinely see this in video games!)

🥳 Extra points if you ask for the character's name and double extra points if you use different colors!

```python
⚔️ Character Stats Generator ⚔️

Name your warrior: Agnes
Their health is: 20hp

Name your warrior: Ian
Their health is: 6hp

Name your warrior: Penelope
Their health is: 48hp
```

<details>
<summary>💡 Hint</summary>

- Import your library first.

- Create one subroutine for a dice of any number and `return` it.

- Create a subroutine that rolls a dice with numbers 1-6 and a dice with numbers 1-8 and multiplies the two numbers together. `Return` that subroutine.

- Ask the user to name their character and `print` that character's health stats.

- Create a `while` loop to allow the user to generate a new character's health stats.

</details>

## 25% Complete...

Go You! 🎊

## Solution (No Peeking!)

<details>
<summary>👀 Answer</summary>

```python
import random

def rollDice(sides):
  result = random.randint(1,sides)
  return result

def roll_6_and_8():
  roll_6_sided_dice = rollDice(6)
  roll_8_sided_dice = rollDice(8)
  health = roll_6_sided_dice * roll_8_sided_dice
  return health

print("⚔️Character stats generator⚔️")


haveACharacter = "yes"

while haveACharacter == "yes":
  character = input("Name your warrior: ")
  health = str(roll_6_and_8())
  print("Their health is ", health,"hp" )
  haveACharacter = input("Want to create another character?")
```

</details>
