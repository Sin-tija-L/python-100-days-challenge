# 👉 Day 43: Take Your List To A New Dimension

<a href="https://youtu.be/lRJ6AJkb4W0?si=AOD0EhEpxDI3wQrP" target="_blank">📹 Dāvida video</a>


Pay close attention, folks, because 2D lists are basically tables.

Tables are two-dimensional data structures where we can store data both vertically and horizontally.

Usually this means that vertical data is used for fields (one category - name, ID, favorite biscuit, etc.) and horizontal data is used for records (all the data for each category).

Behind the scenes, we see a list inside a list. Forget what you know about reading a table with math or geography: 'across the corridor (x-axis) first and then down the stairs (y-axis)'.

Here, we will do row index first and then the column index.

<img id="image" src="assets/day43_1.png" alt="Replit Workspace Overview" width="960">

### Remember...

Here's a 1D list. We have the list name as a variable, single equals to set the value, and sqaure brackets to show this is a list. 2D lists are very similar.

```python
my1DList = ["Johnny", 21, "Mac"]
```


### Adding The Second Dimension

To add the second dimension, we put lists inside the first list.

<img id="image" src="assets/day43_2.png" alt="Replit Workspace Overview" width="960">

👉 Each new list has its own set of square brackets and is separated by a comma. This layout of code is nice to help us visualize the 2D list a a table, but...

```python
my2DList = [ ["Johnny", 21, "Mac"],
             ["Sian", 19, "PC"],
             ["Gethin", 17, "PC"] ]
```

...you can also lay it out like this below:

```python
my2DList = [ ["Johnny", 21, "Mac"], ["Sian", 19, "PC"], ["Gethin", 17, "PC"] ]
```

Now, let's `print` this list.

## Printing From a 2D List

Remember, any comments about the code are written like this:

```python
#these are comments for you, the computer will ignore them
```

### the entire list

👉 We can print an entire 2D list just like we do with a 1D list. However, this will output (print) all of the square brackets, commas, etc.

```python
print(my2DList)

# This will output [['Johnny', 21, 'Mac'], ['Sian', 19, 'PC'], ['Gethin', 17, 'PC']]
```

### a single row

To print a single row, use a single square bracket `[]` in the `print` command. However, you will still get all of those square brackets and commas.

👉 In this example, I'm outputting the first row (index 0) - all of the data about Johnny.

```python
print(my2DList[0])

# This code outputs ['Johnny', 21, 'Mac'].
```

### a single piece of data

The first square bracket references the list, while the second references the item inside that list.

👉 Here are a couple of examples:

```python
my2DList = [ ["Johnny", 21, "Mac"],
             ["Sian", 19, "PC"],
             ["Gethin", 17, "PC"] ]

print(my2DList[0][0])
# This code outputs 'Johnny'. It's Johnny's name from list 0 (first square bracket), item 0 (second square bracket)

print(my2DList[1][2])
# This code outputs 'PC'. It's Sian's computing preference from list 1 (first square bracket), item 2 (second square bracket)
```

## Editing a 2D List

We can edit values in a 2D list in the same way as variables and 1D lists. You just need to change the value to the new row and column index numbers.

👉 In this example, Sian has joined the dark side, so we're updating her computing preference to Linux.

```python
my2DList = [ ["Johnny", 21, "Mac"],
             ["Sian", 19, "PC"],
             ["Gethin", 17, "PC"] ]

my2DList[1][2] = "Linux"
# The line above changes list 1, item 2 from PC to Linux

print(my2DList[1])
# I'm using this line to output list 1 to check that the change has happened correctly.
```

### Play around with assigning new data to the list.

# Common Errors

First, delete any other code in your main.py file. Copy each code snippet below into main.py by clicking the copy icon in the top right of each code box. Then, hit run and see what errors occur. Fix the errors and press run again until you are error free. Click on the 👀 Answer to compare your code to the correct code.

### 'Index out of range'?

👉 What is an 'out of range' error?

```python
my2DList = [ ["Johnny", 21, "Mac"],
             ["Sian", 19, "PC"],
             ["Gethin", 17, "PC"] ]

print(my2DList[0][3])
```

<details>
<summary>👀 Answer</summary>

- The second square bracket references item 3 in list 0. There is no item 3 as the list index only goes up to 2. Remember, everything starts at index 0.

```python
my2DList = [ ["Johnny", 21, "Mac"],
             ["Sian", 19, "PC"],
             ["Gethin", 17, "PC"] ]

print(my2DList[0][2])
```

</details>

# Fix My Code

👉 Try and fix this code which is full of errors.

First, delete any other code in your main.py file. Copy each code snippet below into main.py by clicking the copy icon in the top right of each code box. Then, hit run and see what errors occur. Fix the errors and press run again until you are error free. Click on the 👀 Answer to compare your code to the correct code.

```python
my2DList =  ["Johnny", 21, "Mac"],
             ["Sian" 19, "PC"]
             ["Gethin", 17, "PC"], ]

print(my2DList[0][1])
```

<details>
<summary>👀 Answer</summary>

Lots of lovely syntax errors here. Read the code comments for each one.

```python
my2DList =  [ ["Johnny", 21, "Mac"], # No opening square bracket
             ["Sian", 19, "PC"], # Missing , between Sian and 19. Also missing , after the square bracket for this sub-list.
             ["Gethin", 17, "PC"] ] #Extra , after this sub list - the last sub-list doesn't have a comma after it.

print(my2DList[0][1])
```

</details>

# 👉 Mecca Your Nan Very Happy

Today's challenge is to create a bingo card. Oh yes, because programming's not just for you hip, young cats. 😆

Anyway, your challenge is to enable "gambling for the elderly" (aka Bingo), and you'll achieve it like this:

Randomly generate a series of number between 0 and 90.
Allocate each number to a place in a 2D list.
The numbers should be in numerical order, left to right.
Numbers should not be repeated.
The center square should not contain a number. It should contain the word 'BINGO!'.
When the program is run, the bingo card should be displayed on screen.
Example:

<img id="image" src="assets/day43_3.png" alt="Replit Workspace Overview" width="960">

### ➡️ To run this code use terminal and run the file ⬅️

<details>
<summary>💡 Hints</summary>

- Make sure you include 'prettyprinting'.
- Try using a 2D list with each sublist as a row.
- Randomly generate the numbers and append each to a list as you do.
- Use `.sort()` to put the list of numbers in order before adding to the card.

</details>


## Solution (No Peeking!)

<a href="https://youtu.be/5NpIRejBPiQ?si=Mtrkhw_eUYhwFi5z" target="_blank">Solution video</a>

<details>
<summary>👀 Answer</summary>

```python
import random

bingo = []
print("\033[33mAlises Bingo Card Generator ⭐️")
print()

def generateNumber():
    return random.randint(1, 90)

def prettyPrint():
    print(" ┌───────────┬───────────┬───────────┐")
    for i, row in enumerate(bingo):
      is_last_row = i == len(bingo) - 1  
      print(" │", end=" ")
      for j, number in enumerate(row):
          if number == "⭐️BINGO⭐️":
              print(number.center(9), end=" │ ")
          else:
              print(str(number).center(9), end=" │ ")

      print("\n", end="")
      if not is_last_row:
          print(" ├───────────┼───────────┼───────────┤")
      else:
          print(" └───────────┴───────────┴───────────┘")

numbers = []
for i in range(8):
    numbers.append(generateNumber())

numbers.sort()
bingo =  [ [numbers[0], numbers[1], numbers[2]],
           [numbers[3], "⭐️BINGO⭐️", numbers[4]],
           [numbers[5], numbers[6], numbers[7]], ]

prettyPrint()
```

</details>