# 👉 Day 36: String Manipulation

<a href="https://www.youtube.com/watch?v=2XBhtE3Pl6M" target="_blank">Dāvida video</a>


Let's do some string manipulation to make `if` statements even easier.

👉 Does this code look familiar from the insult generator project?

```python
name = input("What's your name? ")
if name == "David" or name == "david":
  print("Hello Baldy!")
else: 
  print("What a beautiful head of hair!")
```

Right now, if the user writes "DAVID" or "david", the `if` statement works correctly. However, "DaVID" does not give the correct output.

To the computer, " david", "dAviD", and "david" are completely different.

To simplify what the user typed in, we can add these functions to the end of the name of the variable:

<img id="image" src="assets/day36.png" alt="Replit Workspace Overview" width="960">

- `.lower` = all letters are lower case
- `.upper` = all letters are upper case
- `.title` = capital letter for the first letter of every word
- `.capitalize` = capital letter for the first letter of only the first word

### lower

👉 The computer is converting everything to lowercase before it compares my `if` statements.

You need to type your `if` statement in lower case when you use `.lower`. The `if` statement needs to be written in upper case when you use `.upper`, etc.

```python
name = input("What's your name? ")
if name.lower() == "david": 
  print("Hello Baldy!")
else: 
  print("What a beautiful head of hair!")
```

## What if we put a space first?
Adding `.strip()` removes any spaces on either side of the word.

👉 We can chain these functions together.

```python
name = input("What's your name? ")
if name.lower().strip() == "david": 
  print("Hello Baldy!")
else: 
  print("What a beautiful head of hair!")
```

### Try it out!

## No Duplicates

This is a simple program that creates a list with a simple subroutine. In the `while True` loop, the user is adding something to the list. (This is nowhere near as complicated as what you have done).

👉 What happens when you `run` this code and add 'phone' and 'Phone' to your list? Does it create duplicates?

```python
myList = []

def printList():
  print()
  for i in myList:
    print(i)
  print()

while True:
  addItem = input("Item > ")
  if addItem not in myList:
    myList.append(addItem) 
  printList()
```

👉 Here is an easier way to ensure you do not have duplicates. Use these various string manipulations in your loop:


```python
myList = []

def printList():
  print()
  for i in myList:
    print(i)
  print()

while True:
  addItem = input("Item > ").capitalize().strip()
  if addItem not in myList:
    myList.append(addItem)
  printList()
```

Note: Whatever you do after the . will happen to the string. If you use `.lower`, then the string will print in lower case.

## Common Errors

First, delete any other code in your `day36.py` file. Copy each code snippet below into `day36.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

 ### Order matters

👉 What happens if you enter a space before ' phone' when you `run` this code? It duplicates!

```python
myList = []
 
def printList():
 print()
 for i in myList:
   print(i)
 print()
 
while True:
 addItem = input("Item > ").capitalize().strip()
 if addItem not in myList:
   myList.append(addItem)
 printList()
 ```


<details>
<summary>👀 Answer</summary>

- The functions manipulating the strings are applied in the order we add them. In this code, the first character is capitalized and then the spaces are stripped. We need to switch the order in which these functions are added.

```python
while True:
  addItem = input("Item > ").strip().capitalize()
  if addItem not in myList:
    myList.append(addItem)
  printList()
```

</details>

## Fix My Code


👉 Try and fix this code which is full of errors.

First, delete any other code in your `day36.py` file. Copy each code snippet below into `day36.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

```python
whatToEat = input("What do you fancy for dinner? ")
if whatToEat.strip = "pasta": 
  print("Get out the pasta maker.")
elif whatToEatlower() == "TACOS":
  print("Let's do Taco Tuesday!")
else: 
  print("Go search the fridge.")
```

<details>
<summary>👀 Answer</summary>

- Make sure you include `.` and `()` in your string manipulations.
- Strip the spaces first.
- The string manipulation needs to match the string. Ex: `.lower` = lowercase string
- Are your logical operators correct for the `if` statement?

```python
whatToEat = input("What do you fancy for dinner? ")
if whatToEat.strip().lower() == "pasta": 
  print("Get out the pasta maker.")
elif whatToEat.strip().lower() == "tacos":
  print("Let's do Taco Tuesday!")
else: 
  print("Go search the fridge.")
```
</details>

## 👉 Day 36 Challenge

- Create a list of people's names. Ask for first and last name (surname) separately.
- Strip any extra spaces.
- Store names in a capitalized version.
- Create a new string using an fString that combines the tidied up version of the first name and tidied up version of the last name.
- Add those new versions to a list.
- Do not allow duplicates.
- Each time you add a new name, you should print out the full list.

<details>
<summary>💡 Hint</summary>

- Start with your list name. Remember, it should be blank.
- Create your subroutine.
- Next, create a `while True` loop, including input for first and last name.
- Use `.capitalize()` to ensure the first letter is capitalized.
- Get rid of spaces before you capitalize with `.strip()`.
- Use an `if` statement to eliminate duplicates.

</details>

## Solution (No Peeking!)

<a href="https://www.youtube.com/watch?v=Co-jqvo0cDI" target="_blank">Solution video</a>

<details>
<summary>👀 Answer</summary>

```python
rolodex = []

def printList():
  print()
  for name in rolodex:
    print(name)
  print()

while True:
  firstName = input("First Name: ").strip().capitalize()
  lastName = input("Last Name: ").strip().capitalize()
  name = f"{firstName} {lastName}"
  if name not in rolodex:
    rolodex.append(name)
  else:
    print("ERROR: Duplicate name")
  printList()
```

</details>


## !NB 

Please note that this error will show up on pressing cancel
<img id="image" src="assets/day36-01.png" alt="Replit Workspace Overview" width="960">
