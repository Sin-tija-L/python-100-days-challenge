# 👉 Day 16: while True Loop

<a href="https://www.youtube.com/watch?v=cuseM3bReT4" target="_blank">Dāvida video</a>

On Day 15, you learned how to create a `while` loop. However, there are a lot of moving parts that can turn the `while` loop into an accidental infinite loop...and a nightmare.

## Introducing the while True loop...

<img id="image"src="assets/day16.png" alt="Replit Workspace Overview" width="960">

### 👉Let's try it out.

What do you think the below code does?

Remember you can use the big Stop button on the top if your program does not end.

```python
while True:
  print("This program is running")
print("Aww, I was having a good time 😭")
```

This type of loop only has two conditions: `True` and `False`. Make note of the capital `"T"` and `"F"`.

<details>
<summary>Fun Fact</summary>

A Boolean Loop has two values: True or False. Impress your friends and tell them you know how to use a Boolean Loop.

</details>

In this loop, I am saying to the computer:

_"while True is True...do this over and over again."_

### Yes, we made an infinite loop, but hold on...

## Make it stop

There is a way to stop the loop with the word `break`. This exits the loop and stops all code at that point. Even if there is more code written after `break` that is inside the loop.

After `break`, the computer jumps out of the loop to the next unindented line of code.

<img id="image" src="assets/day16-01.png" alt="Replit Workspace Overview" width="960">

## 👉 Let's try it out

`Run` the code below and notice how the loop will continue until `break`. Then the next line of unindented code will run.

```python
while True:
  print("This program is running")
  goAgain = input("Go again?: ")
  if goAgain == "no":
    break
print("Aww, I was having a good time 😭")
```

## Common Errors

First, delete any other code in your `day16.py` file. Copy each code snippet below into `day16.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

### Name Error

👉 What is the error here?

```python
counter = 0
while true:
  answer = int(input("Enter a number: "))
  print("Adding it up!")
  counter += answer
  print("Current total is", counter)
  addAnother = input("Add another? ")
  if addAnother == "no":
    break
print("Bye!")
```

<details>
<summary>👀 Answer</summary>

`while true` needs to be `while True`.

Notice when you change the lowercase` "t"` to a capital `"T"`, the color of the word changes as Replit is now recognizing this as a Boolean loop.

</details>

### Syntax Error

👉 What about this one? What happens when you hit `run`?

```python
counter = 0
while True:
  answer = int(input("Enter a number: "))
  print("Adding it up!")
  counter += answer
  print("Current total is", counter)
addAnother = input("Add another? ")
if addAnother == "no":
  break
print("Bye!")
```

<details>
<summary>👀 Answer</summary>

Notice the error message is saying the syntax error "break outside loop". Do you notice how the last three lines before the bottom `print` statement are not a part of the loop as they are not properly indented (look at the vertical lines)?

</details>

## Fix My Code

👉 Try and fix this code which is full of errors.

First, delete any other code in your `day16.py` file. Copy each code snippet below into `day16.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

```python
while true:
  color = input("Enter a color: ")
  if color = "red":
  break
  else:
    print("Cool color!")
print("I don't like red")
```

<details>
<summary>👀 Answer</summary>

```python
while True:
  color = input("Enter a color: ")
  if color == "red":
    break
  else:
    print("Cool color!")
print("I don't like red")
```

- The word 'true' needs to be capitalized for a `while True` loop.
- The `if` statement needs `==`.
- There is an indention error with `break`.

</details>

## 👉 Day 16 Challenge

Create a "Name the Lyrics" game. Write your favorite song lyrics with a word or two missing. The user has to figure out the correct song lyric in as few attempts as possible. Find the true lyric master among you!

### Example

```python
Fill in the blank lyrics!
(Type in the blank lyrics and see if you are as cool as me.)

Never going to ______ you up.
put
Nope, try again.

Never going to ______ you up.
let
Nope, try again.

Never going to ______ you up.
give

Well done! It only took you 3 attempts.
```

<details>
<summary>💡 Hint</summary>

- Think of your `while True` loop as a replacement for the `if` statement.
- Place your `break` after the code identifying the correct lyric answer.

</details>

## Solution (No Peeking!)

<details>
<summary>👀 Answer</summary>

```python
print("Welcome to Name the Song Lyric")
print()
print("Figure out the missing word as quickly as you can!")
print()

counter = 1
while True:
  lyrics = input("I don't wanna ______ a thing. ")
  if lyrics == "miss" or lyrics == "Miss":
    print("You got it!")
  else:
    print("Nope! Try again!")
    counter +=1
  if lyrics == "miss":
    break
print("Thanks for playing!")

print("You got the correct lyrics in", counter, "attempt(s).")
```

</details>
