# 👉 Day 22: Libraries

<a href="https://www.youtube.com/watch?v=KQ0hAk_lXCQ" target="_blank">Dāvida video</a>

Libraries are collections of code that other people have written. Video games often use massive libraries (for example: <a href="https://en.wikipedia.org/wiki/List_of_game_engines" target="_blank">game engines</a>) to create the epic water reflections, 3-D graphics, etc.

We are going to start a bit smaller by just generating random numbers. (After all, <a href="https://www.gamedeveloper.com/programming/how-classic-games-make-smart-use-of-random-number-generation" target="_blank">random numbers are the basis of most games</a>).

## Random library

We can use a library by writing `import` and then the library name.

_This should always be one of the first lines of code._

👉 Let's import a library that will generate random numbers: (Does this look familiar from Day 14's Rock, Paper, Scissors game?)

```python
import random
```

## How random works

In the code below, I have created a variable, 'myNumber'. I am making it equal to a random number given to me by the `randint` (random integer) library. I add the lowest number (1) and the highest number (100) that can be picked and the computer will generate a number at random.

```python
import random
myNumber = random.randint(1,100)
print(myNumber)
```

### 👉 Give it a try!

## What do I do with libraries?

In the past, we had to hardcode the value users were looking for (remember the higher or lower guessing game...).

### With random, we can generate a number that even we don't know. (Sounds similar to gaming, huh?)

## Common Errors

First, delete any other code in your `day22.py` file. Copy each code snippet below into `day22.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

## Name Error

👉 Why is this code showing the error of "name not defined?"

```python
import random
myNumber = randint(1, 100)
print(myNumber)
```

<details>
<summary>👀 Answer</summary>

This error is because of the way libraries work. The names of functions and variables in libraries may be similar to the names I chose for my functions and variables. The way to access functions and variables in other libraries is to put `random`. in front of the library name.

<img id="image" src="assets/day22.png" alt="Replit Workspace Overview" width="960">

Now the computer knows to "go in the `random` library, find `randint`, and give me a number between 1-100."

```python
import random

myNumber = random.randint(1, 100)
print(myNumber)
```

</details>

### Error with random numbers and loops

👉 For this code, I want 10 random numbers between 1-100 printed out. Why is it printing the same number instead of ten _different_ random numbers?

```python
import random

myNumber = random.randint(1, 100)
for i in range(10):
  print(myNumber)
```

<details>
<summary>👀 Answer</summary>

The problem is when I am generating my random number, I am doing it before the loop. I am asking for one random number and then storing it in a variable. Then, I am saying to `print` out this random number 10 times. Nowhere in the loop am I asking for a new number each time. I need to rearrange the order of my code.

```python
import random

for i in range(10):
  myNumber = random.randint(1, 100)
  print(myNumber)
```

Now, each time the loop resets, it will generate a new random number. Now I can generate 10 random numbers between 1-100.

</details>

## Fix My Code

👉 Try and fix this code which is full of errors.

First, delete any other code in your `day22.py` file. Copy each code snippet below into `day22.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

```python
importrandom
myNumber = .randint(1, 10)
for i in range(10):
  print(myNumber)
```

  <details>
<summary>👀 Answer</summary>

```python
import random

for i in range(10):
  myNumber = random.randint(1, 100)
  print(myNumber)
```

</details>

## 👉 Day 22 Challenge

Copy and paste your code from Day 18.

We are going to make a change to this project:

Make the number generator completely random between 1 and 1,000,000. Now, the game will always have the user guess a random number each time (now the user can't cheat...)

```python
Totally Random One-Million-to-One
What is your guess?: 500000
Too low
What is your guess?: 750000
Too high
What is your guess?: 600000
Too low
What is your guess?: 650000
Correct!
It took you 4 guesses to get the number correct.
Click 'run' to try again with a different number.
```

<details>
<summary>💡 Hint</summary>

- Remember to import your library first and do NOT add it in the loop.
- You can keep a lot of Day 18's code, but need to add the random library.

</details>

## Solution (No Peeking!)

  <details>
<summary>👀 Answer</summary>

```python
print("Welcome to Guess the Number.")
print()
print("Guess a number between 1 and 1,000,000 and I will tell you if you are too low, too high, or get it correct.")
print()
print("Let's play!")

import random
attempt = 1
myNumber = random.randint(1,1000000)

while True:
  user_guess = int(input("Pick a number between 1 and 1,000,000: "))
  if user_guess < myNumber:
    print("That number is too low. Try again!")
    attempt += 1
  elif user_guess > myNumber:
    print("That number is too high. Try again!")
    attempt += 1
    continue
  elif user_guess == myNumber:
    print("You are a winner! 🥳🥳")
    break
    exit()
  else:
    print("That is not a number I recognize.")
print("It took you", attempt, "attempt(s) to get the correct answer.")
```

</details>
