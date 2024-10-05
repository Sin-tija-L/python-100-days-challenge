# 👉 Day 49: Reading From a File

<a href="https://youtu.be/kDQLt3V9WQE?si=DHFkiMXDNMFO8MC8" target="_blank">📹 Dāvida video</a>

**To run this code use terminal and run the file 😎**


Once we've got data into a file, wouldn't it be just splendid to load it back into our program to use again?

Yes. Yes is the answer you're looking for.


### Open

👉 The code to load from a file is pretty similar to that for writing. The command is `open` instead of `read`, and the permissions are slightly different.
**Remember to create file first! Look at the day 48 example!**

```python
f = open("filenames.list", "r")
```

<img id="image" src="assets/day49_1.png" alt="Replit Workspace Overview" width="960">


### Read and Close

👉 In this example, the permission 'r' means 'read only'. Now we load the contents of the file into a variable using the `read` function. Next, close the file to free up the RAM used to store it.

```python
f = open("filenames.list", "r")
contents = f.read()
f.close()
```

<img id="image" src="assets/day49_2.png" alt="Replit Workspace Overview" width="960">


### Print

👉 Finally output the contents of the 'contents' variable to test that it worked.

```python
f = open("filenames.list", "r")
contents = f.read()
f.close()

print(contents)
```


### Split

Bringing everything in in one go is fine, but it would be much more useful to have it as separate items so we can examine it more easily.

👉 To do this, use the `.split()` function in the second to last line. This splits the string into a list of individual elements.

```python
f = open("filenames.list", "r")
contents = f.read()
f.close()

contents = contents.split() #added split here

print(contents)
```

<img id="image" src="assets/day49_3.png" alt="Replit Workspace Overview" width="960">

**Try it out and load away! Remember to create file before opening and reading it!**


## One At A Time
### Form an orderly queue

Reading all the data at once is fine, reading one item at a time works slightly differently.

It uses the `.readline()` function.
👉 The code below reads one line from the file.

```python
f = open("filenames.list","r")
contents = f.readline()
print(contents)

f.close()
```

<img id="image" src="assets/day49_4.png" alt="Replit Workspace Overview" width="960">


### Repeat

To read more than one line, we repeat the command.

👉 The `strip()` function removes the default new line from each print, which would cause an empty line between each line from the file.

```python
f = open("filenames.list","r")
contents = f.readline().strip()
print(contents)
contents = f.readline().strip()
print(contents)
contents = f.readline().strip()
print(contents)
contents = f.readline().strip()
print(contents)

f.close()
```


### Just Use a Loop!
👉 If you're screaming **'LOOP! USE A FREAKING LOOP!'** at the screen right about now.

Your wish is my command.

```python
f = open("filenames.list","r")
while True:
  contents = f.readline().strip()
  
  if contents == "":
    break
  #The last line in the file will be a blank
  #We break the loop if the line read is a blank

  print(contents)
  # Moved the print after the break so it won't output the final blank line.

f.close()
```


## Common Errors

First, delete any other code in your `day49.py` file. Copy each code snippet below into `day49.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

### It's outputting a blank at the end?

👉 What's wrong with this code

```python
f = open("filenames.list","r")
while True:
  contents = f.readline().strip()
  print(contents)
  
  if contents == "":
    break
```

<details>
<summary>👀 Answer</summary>

- The print goes after the break (but not inside the selection branch).

```python
f = open("filenames.list","r")
while True:
  contents = f.readline().strip()
  
  if contents == "":
    break

  print(contents)
```

</details>

### Make it stop! **MAKE IT STOP!**

👉 What is the problem here?

```python
f = open("filenames.list","r")
while True:
  contents = f.readline().strip()
  
  print(contents)
```

<details>
<summary>👀 Answer</summary>

Somebody forgot to break the while loop. no dessert for you....

```python
f = open("filenames.list","r")
while True:
  contents = f.readline().strip()
  
  if contents == "":
    break

  print(contents)
```

</details>


## Fix My Code

👉 Try and fix this code which is full of errors.

First, delete any other code in your `day49.py` file. Copy each code snippet below into `day49.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

```python
while True:
  contents = f.readline().strip()
  
  print(contents)
```

<details>
<summary>👀 Answer</summary>

```python
f = open("files/filenames.list","r")
while True:
  contents = f.readline().strip()
  
  if contents == "":
    break

  print(contents)
```

</details>


# 👉 Day 49 Challenge

In yesterday's challenge, you created a file called high.score and stored some high scores in it.

We've added a version of that file to this repl.

Your program should:

1. Read in the data from the high.score file.
2. Identify which of those users had the highest score. Automatically! (Not you doing it!)
3. Output the name and score of the winner.

**Example:**

<img id="image" src="assets/day49_5.png" alt="Replit Workspace Overview" width="960">

<details>
<summary>💡 Hints</summary>

- Read each element one at a time.
- Split each element into two pieces.
- You'll have to cast one element as an integer to make it a number.
- Think back to list indexing to access the second index for the score.
- Use a max_score list to store the details of the high scorer (starting with line 1 from the file, overwrite the details if the current line has a higher score).

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

f = open(file_path,"r")
highestScore = -1
leaderName = ""
print("🌟Current Leader🌟")
print()
print("Analyzing high scores......")
print()
while True:
  contents = f.readline().strip()
  if contents == "":
    break

  score = int(contents.split()[1])
  if score > highestScore:
        highestScore = score
        leaderName = contents.split()[0]

print(f"Current leader is {leaderName} {highestScore}")
```

</details>