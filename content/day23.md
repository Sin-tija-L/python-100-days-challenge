# Day23 - Subroutine

<a href="https://www.youtube.com/watch?v=gogQkRaXPmA" target="_blank">Dāvida video</a>

So far, when we wanted to repeat code, we have had to use loops or copy and paste code.

What if I told you there was a way to use code or call it and use it anytime anywhere??

That is a subroutine!!

A subroutine tells the computer that a piece of code exists and to go run that code again and again...

## Just like a recipe

Subroutines work like a recipe in a cookbook. If you want to know how to make a cake, you don't have to start from scratch every time. You can use a recipe to get the same quality each time.

## How do we define a subroutine?

A subroutine is defined by:

```python
def (which stands for definition)
```

You need to give the subroutine a name (and just like with a variable, you can't have spaces).

<img id="image" src="assets/day23.png" alt="Replit Workspace Overview" width="960">

You need to add `()` even if there are no arguments followed by a colon `:`. The code needs to be indented.

## Let's try it

👉 Let's roll a random number on a six-sided dice. Copy the code below and click `run`.

```python
def rollDice():
  import random
  dice = random.randint(1, 6)
  print("You rolled", dice)
```

Why is nothing happening??

In this code, I have defined how to roll a dice (this is my recipe for rolling a dice), but I have not actually 'called' the program to run.

## Call the Subroutine

Calling the subroutine means telling it to run.

👉 We need to 'call' the code by adding one more line to our code with the name of the subroutine and the empty `()`:

```python
def rollDice():
  import random
  dice = random.randint(1, 6)
  print("You rolled", dice)
rollDice()
```

_Note that when you call the subroutine, you need to ensure you do NOT indent._

I can even add a range and roll the dice 100 times by adding this code:

```python
for i in range(100):
  rollDice()
```

### 👉 Try it out for yourself!

## Common Errors

First, delete any other code in your `day23.py` file. Copy each code snippet below into `day23.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

### Name error

👉 Why is this code not working?

```python
def print My Name():
  print("My Name is David")
print My Name()
```

<details>
<summary>👀 Answer</summary>

Just like with variables, you cannot have spaces with subroutines (onlyCamelCase or_using_underscores).

```python
def printMyName():
  print("My Name is David")

printMyName()
```

</details>

## Syntax error

👉 What happens when you `run` this code? Can you spot the error?

```python
def countToFive:
  for i in range(1, 6):
    print(i)
countToFive()
```

<details>
<summary>👀 Answer</summary>

You need to add `()` in the first line, even though there is no argument.

```python
def countToFive():
  for i in range(1, 6):
    print(i)

countToFive()
```

</details>

## What about this one?

👉 Don't be fooled. This error is different than the last example.

```python
def countToFive():
  for i in range(1, 6):
    print(i)
  countToFive()
```

<details>
<summary>👀 Answer</summary>

When you call your subroutine, make sure it is NOT indented.

```python
def countToFive():
  for i in range(1, 6):
    print(i)

countToFive()
```

</details>

## Fix My Code

First, delete any other code in your `day23.py` file. Copy each code snippet below into `day23.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

```python
def print favorite color:
  print("My favorite color is red.)
  print favorite color()
```

<details>
<summary>👀 Answer</summary>

```python
def print_favorite_color():
  print("My favorite color is red.")

print_favorite_color()
```

</details>

## 👉 Day 23 Challenge

1. Create a subroutine with both a username and password.
2. Create a loop to prompt the user again and again until they put in the correct login information.

```python
Replit Login System
What is your username?: david
What is your password? whatAmazingHairYouHave
Whoops! I don't recognize that username or password. Try again!
What is your username? david
What is your password? baldies4life
Welcome to Replit!
```

<details>
<summary>💡 Hint</summary>

- Create one login subroutine. Maybe you should call it `login`.
- Use `input` and `if` statements inside a loop.
- Where does the loop need to `break`? Where does it need to `continue`?

</details>

## Solution (No Peeking!)

  <details>
<summary>👀 Answer</summary>

```python
def login():
  while True:
    username = input("What is your username?: ")
    password = input("What is your password? ")
    if username == "David" and password == "Replit4ev#r":
      print("Welcome David!")
      break
    else:
      print("That is not the correct username or password. Try again!")
      continue

print("REPLIT LOGIN SYSTEM")
login()
```

</details>
