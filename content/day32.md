# 👉 Day 32: Lists

<a href="https://www.youtube.com/watch?v=sylq300J9EM" target="_blank">Dāvida video</a>


In Computer Science, we learn about a data structure called arrays. Arrays are a place to store more than one thing with the same variable name.

However, Python uses lists instead. Lists are literally lists of items. Any piece of data from any data type can go into a list. We can extract, remove, or change lists.

#### You may be asking: "What is the point of a list?"

Sometimes, you don't always know how much data you need to store. We can use a loop to move through data in a list without having to first manually tell the computer how many things are in that list.

### Starting at 0

As far as Python is concerned, this is a list. Notice we start counting the first item at 0 (instead of 1).

<img id="image" src="assets/day32.png" alt="Replit Workspace Overview" width="960">

Example: In this list, "lots" is index 0, "of" is index 1, etc.

We can directly add to the list with the variable name, `[ ]` with the index number of the row.

<img id="image" src="assets/day32-01.png" alt="Replit Workspace Overview" width="960">

## Printing Lists

We can print out data in the same way.

<img id="image" src="assets/day32-02.png" alt="Replit Workspace Overview" width="960">


👉 Let's make a list of our class schedule.

```python
timetable = ["Computer Science", "Math", "English", "Art", "Sport"]
```

👉 Let's `print` our list:

```python
timetable = ["Computer Science", "Math", "English", "Art", "Sport"]
print(timetable)
```

### Yikes!

That looks awful with all the `[ ],""` printing too! If I want to print out index 1 in my timetable, I need to tell the computer!

<img id="image" src="assets/day32-03.png" alt="Replit Workspace Overview" width="960">

👉 Let's try to `print` math from our list above:


```python
timetable = ["Computer Science", "Math", "English", "Art", "Sport"]
print(timetable[1])
```

Remember, we start counting at 0. So the second index, math, is 1.

#### Can you `print` the entire timetable?

## Changing Lists

We can also change lists and the index.

We built our list with `timetable =`, but we want to change index 4, "sport". We can do this by calling it with `[ ]`.

```python
timetable = ["Computer Science", "Math", "English", "Art", "Sport"]
print(timetable[0])
print(timetable[1])
print(timetable[2])
print(timetable[3])
print(timetable[4])
```

👉 Add this to to the code above:

```python
timetable[4]= "Watch TV"
``` 

Why is it not printing correctly? I have created the timetable, printed it out, and changed index 4 of the timetable.

👉 However, I need to `print` the changed version. Let's `print` our new index:


```python
timetable[4]= "Watch TV"
print(timetable[0])
print(timetable[1])
print(timetable[2])
print(timetable[3])
print(timetable[4])
```

#### Can you change another index and print the new list?


## Lists and Loops

Why would I want to write all of those lines of code?

#### Introducing lists' best friend...loops

<img id="image" src="assets/day32-04.png" alt="Replit Workspace Overview" width="960">


👉 We can replace a lot of those lines of code we just wrote with just two lines of code. Change your code to look like this:


```python
timetable = ["Computer Science", "Math", "English", "Art", "Watch TV"]
for lesson in timetable:
  print(lesson)
```

Now we have given the computer a list. We said "make `lesson` each value within this list and then do something with it."

<details>
<summary>Flashback</summary>

Remember, `for` loops work by creating the variable right after the word `for` and setting it equal to each value in a list (so far we have only used numbers with the `range` function).

</details>

#### Try it out!

## Common Errors

First, delete any other code in your `day32.py` file. Copy each code snippet below into `day32.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

### Start counting from 0

👉 I used an f-string to print out the first color in my list. Why is it printing the second color in my list, orange, instead of red?

```python
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Violet"]
print(f"The first color is {colors[1]}")
```

<details>
<summary>👀 Answer</summary>

```python
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Violet"]
print(f"The first color is {colors[0]}")
```

- Remember, start counting from 0. The first color in the list, red, is index 0.


</details>

👉 I want to access the last color in my list, violet. Why is my code crashing?

```python
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Violet"]
print(f"The first color is {colors[6]}")
```

<details>
<summary>👀 Answer</summary>

```python
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Violet"]
print(f"The last color is {colors[5]}")
```

- There is no index 6 because you need to start counting from 0. The 6th item in the list, violet, is index 5.

</details>

## Fix My Code

👉 Try and fix this code which is full of errors.

First, delete any other code in your `day32.py` file. Copy each code snippet below into `day32.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

```python
grocery list = ["bananas", "bread", "milk", "eggs", "juice", "cheese"]
print("The first grocery item to buy is {grocery list[1]}.")
```


<details>
<summary>👀 Answer</summary>

```python
grocery_list = ["bananas", "bread", "milk", "eggs", "juice", "cheese"]
print(f"The first grocery item to buy is {grocery_list[0]}.")
```

- Your variable cannot have spaces.
- Don't forget your f-string.
- Remember to start at 0 with the first item on your list.

</details>

## 👉 Day 32 Challenge

- Create a list that stores greetings in different languages. Start with the language you speak.
- Then, go on the internet to find other greetings in other languages. Here is a list of greetings to get you started.
- Import random library. Generate a random number between 0 and maximum number of items in your list.
- At random, when the user clicks run, print one of the greetings.
- Use an f-string.


<details>
<summary>💡 Hint</summary>

- Start with importing your library.
- Add your greetings as your list.
- Remember how you used `random.randint` to generate random numbers? Try that again here. (Don't forget to assign a variable to this).
- Remember your first greeting is index 0.
- `print` a random greeting.
- You will only need four lines of code to make this project run!

</details>


## Solution (No Peeking!)

<a href="https://www.youtube.com/watch?v=qTyCw0q8a70" target="_blank">Solution video</a>

<details>
<summary>👀 Answer</summary>

```python
import random
greetings = ["Hello there!", "Konnichiwa", "Guten Tag!", "Bore Da!"]
index = random.randint(0,3)
print(greetings[index])
```

</details>

