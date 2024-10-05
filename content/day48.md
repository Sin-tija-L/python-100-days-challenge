# 👉 Day 48: File Writing

<a href="https://youtu.be/b2NlupcxRew?si=cw8It_kDlpLym64z" target="_blank">📹 Dāvida video</a>

**To run this days code use terminal and run the file 😎**


Our VSCode structure doesn't need to be just one file that contains all of the code and data. We can write data to other files for longer term storage, then access it when we need it.

👉 To do this we're going to use the files directory under python_files directory. It looks like this:

<img id="image" src="assets/day48_1.png" alt="Replit Workspace Overview" width="960">


## Temporary Memory

When we use variables, lists, dictionaries and other data structures in our code, the data inside them are stored in the computer's RAM.

RAM is temporary storage (usually called memory). It's used to hold data and instructions for programs that your computer currently has open.

The problem is, that when a program finishes, or is closed, its data and instructions are removed from the RAM to free up space.

This is why you had to re-input all of your test data for your dynamic list & dictionary programs every time you ran them. The contents of those lists/dictionaries were removed from RAM when the program finished executing.


## Creating A New File

To avoid this incredibly annoying data re-entry task, we are going to get the program to save data into a file. 

👉 Here's how to open a file. This one line of code has three important features:

```python
import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the path to the 'files' directory, relative to the script's location
file_path = os.path.join(script_dir, "files/savedFile.txt")

# Ensure the 'files' directory exists
os.makedirs(os.path.dirname(file_path), exist_ok=True)

# Create the empty file
f = open(file_path, "w")
```

<img id="image" src="assets/day48_2.png" alt="Replit Workspace Overview" width="960">

1. **The variable `(f)`**: This is needed to allow your program to communicate to the file. Normally this would have a lovely meaningful name. However, you will need to type this variable name lots, and lots, and lots. So short is good. `f` is short for 'file'.

2. **The file name (the first item in brackets, `"savedFile.txt"`)**: You **MUST** code this to match the filename **EXACTLY** and include the file extension.

3. **The `'w'` (second item in brackets)**: This sets the permissions for the file. `'w'` means 'write'. This means that if the file doesn't already exist, the program will create a new blank file with that file name. However, if it **does** already exist it will be overwritten with a blank file.

## Save Me! Writing Data To The File

👉 The `.write()` command will write the piece of data in brackets into the file. You can use as many of these as you want. In your existing code only update these lines.

```python
f = open(file_path, "w")
f.write("Hello there")
```

<img id="image" src="assets/day48_3.png" alt="Replit Workspace Overview" width="960">

## Close

👉 However, this data IS STILL IN THE RAM. Nothing gets saved until we close the file using the `.close()` command.

```python
f = open(file_path, "w")
f.write("Hello there")
f.close()
```

<img id="image" src="assets/day48_4.png" alt="Replit Workspace Overview" width="960">

When you run this code, nothing will appear in the console, but check the files tab on the left.

Gasp! A file has been created.

<img id="image" src="assets/day48_5.png" alt="Replit Workspace Overview" width="960">

Click on it to view the contents!

<img id="image" src="assets/day48_6.png" alt="Replit Workspace Overview" width="960">


# Saving to Files

👉 Now let's get some input, store it in a variable, and write it to the file.

```python
f = open(file_path, "w")
whatText = input("> ")
f.write(whatText)
f.close()
```

### Preventing Overwrite
We're going to change the file permissions from 'w' to 'a+'.

'a' means append - add to the end of the file.

However, if the file doen't exist, then it will crash.

'a+' means 'add to the end of the file, or create a new one if it doesn't exist'.

👉 Here's the amended code with the change on line 1:

```python
f = open(file_path, "a+")
whatText = input("> ")
f.write(whatText)
f.close()
```

The problem with this is that it just glues the second input straight on to the first. Like this:

<img id="image" src="assets/day48_7.png" alt="Replit Workspace Overview" width="960">

So we need some.......


### New Lines

👉 We can use our old friend, the fString, to format a new line. I've used the `\n` new line character.

```python
f = open(file_path, "a+")
whatText = input("> ")
f.write(f"{whatText}\n")
f.close()
```

That's better.

<img id="image" src="assets/day48_8.png" alt="Replit Workspace Overview" width="960">

**Make sure you follow all three steps so the file saves.**

## Common Errors

First, delete any other code in your `day48.py` file. Copy each code snippet below into `day48.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

### I/O operation error

👉 What is the problem here?

```python
f = open(file_path, "a")
whatText = input("> ")
f.write(f"{whatText}\n")
f.close()
whatText = input("> ")
f.write(f"{whatText}\n")
```

<details>
<summary>👀 Answer</summary>

The second input and write command are after the file has been closed instead of before.

```python
f = open(file_path, "a+")
whatText = input("> ")
f.write(f"{whatText}\n")
whatText = input("> ")
f.write(f"{whatText}\n")
f.close()
```

</details>

## Fix My Code

👉 Try and fix this code which is full of errors.

First, delete any other code in your `day48.py` file. Copy each code snippet below into `day48.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

```python
f = open("savedFoal.", "a")
whatText = input("> ")
f.write(f"{whatText}\n")
f.close
whatText = input("> ")
f.write(f"{whatText}\n")
```

<details>
<summary>👀 Answer</summary>

- This was subtle (on purpose). 'Erica' and 'streak' are incorrect in the `print` statement.

```python
f = open(file_path, "a+")

whatText = input("> ")
f.write(f"{whatText}\n")
whatText = input("> ")
f.write(f"{whatText}\n")

f.close()
```

</details>


# 👉 Day 48 Challenge

Today's challenge is to create a high score table.

Your program should:

1. Ask the user to input their three-letter initials and score (out of about 100,000).
2. Save both those values into a file called 'high.score'.
3. This should use append mode. If the file doesn't exist, it should be created. If it does, the score should be added to the end.
4. Each new entry score should go on a new line as `initials space score`. Then start a new line for the next entry.
5. Add 2-3 scores for testing in a loop.
6. The loop should ask the user if they've finished entering data and stop if they have.

🎉 **Extra points for getting all the inputs with just one `input` command and the `split` function.**

**Example:**

<img id="image" src="assets/day48_9.png" alt="Replit Workspace Overview" width="960">

<details>
<summary>💡 Hints</summary>

- Not much here that you can't get from the examples.
- Don't forget to put a new line character at the end of each write command.

</details>

## Solution (No Peeking!)

<a href="https://youtu.be/KobdLjIvoeE?si=m0j7NlG1cGdV9nIB" target="_blank">Solution video</a>

<details>
<summary>👀 Answer</summary>

```python
import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(script_dir, "files/high.score")

f = open(file_path, 'a')

print("🌟HIGH SCORE TABLE🌟")
userInput = input("\nInput your initials and score (e.g., DJM 89764): ")
initials, scoreStr = userInput.split()
score = int(scoreStr)
f.write(f"{initials} {score}\n")
print("\nAdded to high score table.")
```

</details>