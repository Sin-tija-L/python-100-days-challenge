# 👉 Day 5: If Statements


<a href="https://www.youtube.com/watch?v=Wmn9yze6m5U" target="_blank">Dāvida video</a>


These statements are a bit like asking a question. You are telling the computer: if something is true, then do this specific block of code. Double equals (`==`) is asking the computer to compare if these two things are exactly the same.

In the code below, I am asking `if` the variable `myName` is the same as the string `David`.

```python 
myName = input("What's your name?: ")
if myName == "David":
```

## But that doesn't print anything?

To create a `print` statement related to the input from the if statement, you must go to the next line and indent once (Luckily, Replit does this for you, but be careful!) so it is all a part of the code we run.

👉 Copy this code and see what happens.

```python 
myName = input("What's your name?: ")
if myName == "David":
  print("Welcome Dude!")
```

### What is else?

If the condition is not met with the `if` statement, then we want the computer to do the `else` part instead. Likewise, `if` the condition is met in the if statement, then the `else` bit is ignored by the computer. The `else` statement must be the first thing unindented after the `if` statement and in line with it (Replit helps you out here too!)

👉 Copy this code and give it a go. Watch those indents!

```python
myName = input("What's your name?: ")
if myName == "David":
 print("Welcome Dude!")
 print("You're just the baldest dude I've ever seen")
else:
 print("Who on earth are you?!")
 ```

 ## Common Errors

First, delete any other code in your` day05.py` file. Copy each code snippet below into `day05.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.


## Syntax Error

👉 What is wrong with this code below?

```python
catsOrDogs = input("Are you a cat person? Or a dog person?: ")
if catsOrDogs = "cat":
  print("Meow")
else:
  print("Woof")
```

<details>
<summary>👀 Answer</summary>

- Our if statement must include == so it should read:
- if catsOrDogs == "cat":
</details>

### Syntax Error...again

👉 What is wrong with this code?

```python
catsOrDogs = input("Are you a cat person? Or a dog person?: ")
if catsOrDogs == "cat"
  print("Meow")
else:
  print("Woof")
```

  <details>
<summary>👀 Answer</summary>

- Our if statement is missing the :

</details>

### Indentation Error

👉 Do you see the error here?

```python
catsOrDogs = input("Are you a cat person? Or a dog person?: ")
if catsOrDogs == "cat":
  print("Meow")
else:
print("Woof")
```

  <details>
<summary>👀 Answer</summary>

- As soon as you see a colon, the next line should be indented one more than the line above it.

</details>

## Fix My Code

👉 Try and fix this code which is *full* of errors.


First, delete any other code in your `day05.py` file. Copy each code snippet below into `day05.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

```python
drink = input("Do you prefer coffee or tea?)
if drink = "coffee"
  print("Tea is better.")
    else:
  print("Excellent choice.")
```

<details>
<summary>👀 Answer</summary>

```python
drink = input("Do you prefer coffee or tea?")
if drink == "coffee":
  print("Tea is better.")
else:
  print("Excellent choice.")
```

</details>

## 👉 Day 5 Challenge

## "Which character are you?" Generator

You will need to:

1. Ask your users a series of questions that identify if they're one of the characters in the world you have created.

<details>
<summary>💡 Hint</summary>

Organize your questions and potential answers before you start to more easily identify how to code it.

</details>

2. Add multiple `if` statements to check the result of each question.

<details>
<summary>💡 Hint</summary>

Use `input` and `variables` to ask the questions, but ask each question only before the next if statement.


</details>


3. Make sure to have a final print if they haven't selected any of the characters so far.


<details>
<summary>💡 Hint</summary>

`ELSE`

</details>

### Example

```python
Marvel Movie Character Creator
--
Do you like 'hanging around'?: No
Then you're not Spider-man

Do you have a 'gravelly' voice?: No
Aww, then you're not Korg

Do you often feel 'Marvelous'?: Yes
Aha! You're Captain Marvel! Hi!
```

## Solution (No Peeking!)

<details>
<summary>👀 Answer</summary>

```python
print("Which character are you from 'Avengers?'")
print()
print("Answer these questions and let's find out.")
print()
print("Please use Y or N for yes and no.")

likeGreen = input("Do you like the color green?: ")
if likeGreen == "Y":
  print("You must be the Hulk!")

IronIsCool = input("Do you think building robots is cool?: ")  
if IronIsCool == "Y":
  print("You must be Iron Man. Cool suit!")

TimeTravel = input("Do you like traveling through time?: ")  
if TimeTravel == "Y":
  print("You must be Captain America!")

Strong = input("Are you super strong?: ")
if Strong == "Y":
  print("You have got to be Thor!")
else:
  print("I guess you are not like anyone from 'Avengers.'")
```

</details>