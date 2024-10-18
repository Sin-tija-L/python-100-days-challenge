# 👉 Day 63: Multiple Files


<a href="https://www.youtube.com/watch?v=girsuXz0yA8" target="_blank">📹 Dāvida video</a>


By now, you have written some pretty big programs with lots of lines of code.

This can get pretty cumbersome to deal with. Lots of scrolling to find the right bit...

One of the ways to overcome this is to split the code into multiple files.

That's right. Your programs can consist of more than one python file. The main file will always run first, but you can put parts of your code into other files and bring them in to main.py by importing.

In fact, you've already done this whenever you've used `import random`, `import time`, `import os` and so on. It's just that on those occasions, you were importing code written by someone else.

Today, you'll create your own code file and import it into your main program.

👉 Let's start with a basic 'count to 10' program in the `day63.py` file.

```python
for i in range(10):
  print(i+1)
```

👉 Now let's move it to a new file.

In the files menu click on `python_files`, find the 'New File' and select it.

<img id="image" src="assets/day63_1.png" alt="day63 image" width="960">

Name the file `test63.py` - you **MUST** include the .py to specify that it's a python file.

<img id="image" src="assets/day63_2.png" alt="day63 image" width="960">

Cut and paste the code from `day63.py` to `test63.py`.

<img id="image" src="assets/day63_3.png" alt="day63 image" width="960">


By now, your `day63.py` file should have nothing in it.


👉 To run this code use terminal and run the file. Watch in amazement as nothing happens!

**To run this code open new Terminal and type `python python_files/day63.py` or `python3 python_files/day63.py` and see the result! 🚀**


Remember, Python runs the code in the `day63.py` file, which at the moment is empty. So we need to import the code.

👉 Go to your `day63.py` file and add this code.

```python
import test63 # No need for the .py
```

👉 Now run the code and watch the 'count to 10' program execute.


## It Can't Be That Easy? Can It?

Well....... no. Because we can't control **when** the 'count to 10' program runs. It just runs on import. In this example, it would run *before* the `print("Countdown")` code. Not ideal.

```python
import test63

print("Countdown")
```

To solve this, we need to think more like libraries. They consist of a bunch of subroutines that we can import and then **call only when we need them.**

👉 Back in your `test63.py` file, you need to make the countdown program a subroutine.

```python
def countdown():
  for i in range(10):
    print(i+1)
```

👉 Finally, let's call it in our `day63.py` file.

```python
import test63

print("Countdown")
test.countdown() # Test refers to the file, countdown to the subroutine in that file.
```

### Try it out!

## Nicknames

If your file name is really long, you can give it a pseudonym, or nickname, as I believe the hip young things are calling them these days. This will save you time every time you want to run a subroutine from that file.

👉 Use `as` to nickname your file. Here I've used `tt` for the `test63` file.

```python
import test63 as tt

print("Countdown")
tt.countdown()
```

### Try It Out!



## Common Errors
 
 First, delete any other code in your `day63.py` file. Copy each code snippet below into `day63.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

 ### It's... undefinable!

 👉 Why is it not importing my file?

 ```python
import test63

print("Countdown")
countdown()
```

<details>
<summary>👀 Answer</summary>

We've not referenced the `countdown()` subroutine as belonging to the `test63` file on line 3.

```python
import test63

print("Countdown")
test.countdown()
```

</details>


### It's Running The Subroutine Twice?

👉 What is the problem here?

```python
import test63

print("Countdown")
test.countdown()
```

<details>
<summary>👀 Answer</summary>

This is a cunning one, the error is not in the `day63.py` file. In fact, it's because we've called the `countdown()` subroutine **inside the `test63.py` file.**

Be careful to remove any internal subroutine calls in separate files, especially if you're copying code over from other programs.

This is the code from the `test63.py` file:

```python
def countdown():
  for i in range(10):
    print(i+1)

countdown() # Remove this line
```

</details>


## Fix My Code

👉 Try and fix this code which is full of errors.

First, delete any other code in your `day63.py` file. Copy each code snippet below into `day63.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

```python
## test63.py file ##############
import random

num = randint(10,100)

def countdown():
  for i in range(num):
    print(i+1)

countdown()

### day63.py file ###############

import tt

print("Countdown")
countdown()
```

<details>
<summary>👀 Answer</summary>

```python
## test63.py file ##############
import random

num = random.randint(10,100) # Need the random. to refer to the random library

def countdown():
  for i in range(num):
    print(i+1)

# Removed internal subroutine call.

### day63.py file ###############

import test63 as tt # No such file as tt, that's the nickname I want to give the 'test' file

print("Countdown")
tt.countdown() # Referenced 'tt' file nickname before the call.
```

</details>


## 👉 Day 63 Challenge

Today's challenge is to become your own librarian. Oook!

In the real world, programmers usually keep a library of their most useful subroutines just like this. You're going to curate your own library with these subroutines.

1. Go back through your programs and choose some subroutines that you've used a *lot*. Perhaps it was your dice roller. Could be your *prettyPrint*. Maybe it was your 'generate random baldy insult' subroutine. Whatever. Find them.
2. Create a new file that contains all your best subroutines.
3. Import this file into your `day63.py` and call a few to show that it works.

<details>
<summary>💡 Hint</summary>

- You're better than this by now! No hints today, amigos! Good luck!

</details>


## Solution (No Peeking!)

<details>
<summary>👀 Answer</summary>

```python
## test63.py file ##############
import random

def createCharacter():
  name = input("Name your Legend: ")
  print()
  type = input("Character Type (Human, Elf, Wizard, Orc): ")
  print()
  return name + ": the " + type

def generateStats(name, number):
  diceSides1 = random.randint(1, 100)
  diceSides2 = random.randint(1, 100)
  number1 = random.randint(1, diceSides1)
  number2 = random.randint(1, diceSides2)
  intelligence = ((number1 * number2) / 2) + number
  print(name, intelligence)


### day63.py file ###############

import test63 as tt

print(tt.createCharacter())

print()

tt.generateStats("Alise", 55)
```

</details>


**Run file from terminal in this task**