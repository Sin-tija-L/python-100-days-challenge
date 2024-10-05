# 👉 Day 33: Dynamic Lists

<a href="https://www.youtube.com/watch?v=O26Y99VRsgQ" target="_blank">Dāvida video</a>


Dynamic lists are ways of using a blank list and adding or removing items to it as we go.

### Blank lists

👉 Let's make an agenda for today. I am not going to put anything in this list (yet). Behind the scenes, the computer is going to recognize this code as a blank list.

```python
myAgenda = []
```

<img id="image" src="assets/day33.png" alt="Replit Workspace Overview" width="960">

### Append a list

`.append` will let us add whatever is in `()` to the list.

<img id="image" src="assets/day33-01.png" alt="Replit Workspace Overview" width="960">

👉 Let's use a `while True` loop to add items to the list. We will store this in a variable called `item`. Add this code to the end of the code above:

```python
while True:
  item = input("What's next on the Agenda?: ")
  myAgenda.append(item)
  printList()
```

👉 What is next on your agenda? Type it in the console.

### Printing our new list
👉 Wait?! Why can't we see what we just added to the list? We need to `print` the list each time to see what has changed. Let's use a subroutine (why not!):

```python
myAgenda = []

def printList():
  print() #this is just to add an extra space between items
  for item in myAgenda:
    print(item)
  print() #this is just to add an extra space between items

while True:
  item = input("What's next on the Agenda?: ")
  myAgenda.append(item)
  printList()
```

```python
#The comments in green are for you and the computer will skip them.
```

Do you see how the subroutine allows you to add a new item to your agenda and prints the entire list each time?

You could even import `os` and `sleep` libraries to pause and clear your code to make this dyanmic list look even nicer.

*Remember: The list that's blank needs to be listed first...even before the subroutines.*

#### Try it for yourself!

## Removing Items from a List

👉 Let's make a few changes to our list. We want to ask the user if they want to add or remove an item from their list:


```python
myAgenda = []

def printList():
  print() 
  for item in myAgenda:
    print(item)
  print() 

while True:
  menu = input("add or remove?: ")
  if menu == "add":
    item = input("What's next on the Agenda?: ")
    myAgenda.append(item)
  elif menu == "remove":
    item = input("What do you want to remove?: ")
    myAgenda.remove(item)
  printList()
```

Notice how using `.remove` will remove what is inside the `( )`.


<img id="image" src="assets/day33-02.png" alt="Replit Workspace Overview" width="960">

#### You just build a pretty comprehensive program. Go you!


## Common Errors


First, delete any other code in your `day33.py` file. Copy each code snippet below into `day33.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

### Removing something that is not there

👉 Add "recording" to your list when you hit `run`. Now, remove "nap." Yikes! An ugly error message.

```python
myAgenda = []

def printList():
  print() 
  for item in myAgenda:
    print(item)
  print() 

while True:
  menu = input("add or remove?: ")
  if menu == "add":
    item = input("What's next on the Agenda?: ")
    myAgenda.append(item)
  elif menu == "remove":
    item = input("What do you want to remove?: ")
    myAgenda.remove(item)
  printList()
  ```

  <details>
<summary>👀 Answer</summary>

The error message is just saying "x not in list". What does that mean? The thing you asked to remove is not there. (i.e. You asked to remove a nap from a list that it was not added to in the first place). The best workaround is to add a nested `if` statement to your code:


```python
myAgenda = []

def printList():
  print() 
  for item in myAgenda:
    print(item)
  print() 

while True:
  menu = input("add or remove?: ")
  if menu == "add":
    item = input("What's next on the Agenda?: ")
    myAgenda.append(item)
  elif menu == "remove":
    item = input("What do you want to remove?: ")
    if item in myAgenda:
      myAgenda.remove(item)
    else:
      print(f"{item} was not in the list")
  printList()
```

Try it again. Can you try to remove something that does not already exist in the list?

</details>

👉 Yuck! Why is this not working? What does that error even mean?

```python
myAgenda = []

def printList():
  print() 
  for item in myAgenda:
    print(item)
  print() 

while True:
  menu = input("Add or Remove?: ")
  if menu == "add":
    item = input("What's next on the Agenda?: ")
    item.append(myAgenda)
  elif menu == "remove":
    item = ("What do you want to remove?: ")
    if item in myAgenda:
      item.remove(myAgenda)
    else:
      print(f"{item} was not in the list")
  printList()
  ```

  <details>
<summary>👀 Answer</summary>

The problem is with the `append` function. We have two objects backwards. The list name comes first and then what's being added to the list goes inside `()`. Hint: You will see the same issue with `remove` too.

It always needs to be: `listname.append()` or `listname.remove()`

```python
myAgenda = []

def printList():
  print() 
  for item in myAgenda:
    print(item)
  print() 

while True:
  menu = input("Add or Remove?: ")
  if menu == "add":
    item = input("What's next on the Agenda?: ")
    myAgenda.append(item)
  elif menu == "remove":
    item = input("What do you want to remove?: ")
    if item in myAgenda:
      myAgenda.remove(item)
    else:
      print(f"{item} was not in the list")
  printList()
```

</details>

## Fix My Code


👉 Try and fix this code which is full of errors.

First, delete any other code in your `day33.py` file. Copy each code snippet below into `day33.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

```python
def printList():
  print() 
  for item in myPartyList:
    print(item)
  print() 

while True:
  menu = input("add or remove?: )
  if menu = "add":
    item = input("Who should I add to the party list?: ")
    myPartyList.add(item)
  elif menu == "remove":
    item = input("Who should I remove from the party list?: ")
    if item in myPartyList:
      myPartyList.remove(list)
    else:
      print("{item} was not in the list)
  printList()
  ```

  <details>
<summary>👀 Answer</summary>

```python
myPartyList = []

def printList():
  print() 
  for item in myPartyList:
    print(item)
  print() 

while True:
  menu = input("add or remove?: ")
  if menu == "add":
    item = input("Who should I add to the party list?: ")
    myPartyList.append(item)
  elif menu == "remove":
    item = input("Who should I remove from the party list?: ")
    if item in myPartyList:
      myPartyList.remove(item)
    else:
      print(f"{item} was not in the list")
  printList()
```

- You have to start with the name of your blank list.
- Make sure you use `append` and `remove` (not `add`).
- Don't forget your f-string.
- There may be a few `=` and `"` missing too.

</details>

## 👉 Day 33 Challenge

Create your own to do list manager. (This can be super useful!)

- Ask the user whether they want to view, add, or edit their to do list.
- If they want to view it, `print` it out in a nice way (Hint: subroutine).
- If they choose to add an item to the to do list, allow them to type in the item and then add it to the bottom of the list.
- If they want to edit the to do list, ask them which item they completed, and remove it from the list.
- Don't worry about duplicates!
- The first item you put in the list should be the first item you remove.
- Add a title, some color, alignment to the text, or emojis. Show off your skills!

Example:

```python
To Do List Manager:
Do you want to view, add, or edit your to do list?
view

Record video for day 34
```

<details>
<summary>💡 Hint</summary>

- Import libraries first. What libraries will allow you to clear your code and pause it?
- Remember, your list name needs to come before any subroutines or lists.
- Create a subroutine very similar to the one we looked at in the common errors section.
- Add a `while True` loop with `if` statements that allow the user to add, edit, or view their to do list.
- Also, remember what we did to fix the second common error related to removing an item that is not in the to do list. (a nested `if` statement)
- End with pausing and clearing your code.

</details>

## Solution (No Peeking!)


<a href="https://www.youtube.com/watch?v=Csi3vGGYwuk" target="_blank">Solution video</a>

<details>
<summary>👀 Answer</summary>

```python
toDoList = []

def printList():
    print()
    for item in toDoList:
        print(item)
    print()

while True:
    menu = input("ToDoList Manager\n\nDo you want to view, add, edit, or exit the todo list?\n").lower()
    if menu == "view":
        printList()
    elif menu == "add":
        item = input("What do you want to add?\n")
        toDoList.append(item)
    elif menu == "edit":
        item = input("What do you want to remove?\n")
        if item in toDoList:
            toDoList.remove(item)
    elif menu == "exit":
        print("Thank you for using the ToDoList Manager. Goodbye!")
        break
```

</details>