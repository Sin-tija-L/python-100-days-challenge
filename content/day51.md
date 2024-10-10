# 👉 Day 51: Save to and Load From Files

<a href="https://youtu.be/ITGtT9EEgL8?si=GaFLaq1FJ939uCil" target="_blank">📹 Dāvida video</a>

**To run this day's code use terminal and run the file 😎**

There are some things that primary storage in the RAM does better.

For example, it's easy to access, amend, or remove a piece of data held in a list (in the RAM).

Holding data in secondary storage in a file makes this more difficult. Or does it?

With Python, there's more than meets the eye.

---

👉 The program below lets me add & remove events and dates into a diary system. It adds the name & date of an event to the 2D list. Or it searches for an existing name & date and removes it.

```python
myEvents = []

def prettyPrint():
  print()
  for row in myEvents:
    print(f"{row[0] :^15} {row[1] :^15}")
  print()

while True:
  menu = input("1: Add, 2: Remove\n")

  if menu == "1":
    event = input("What event?: ").capitalize()
    date = input("What date?: ")
    row = [event,date]
    myEvents.append(row)
    prettyPrint()

  else:
    criteria = input("What event do you want to remove?: ").title()
    for row in myEvents:
      if criteria in row:
        myEvents.remove(row)
```

Manually saving and loading from this program to a file each time would be a massive faff. Instead, we can set up an auto-save by writing the save code at the end of our infinite loop.


### Auto-Save

👉 At the bottom of the code, we are going to add an autosave just before the loop repeats.

*Make sure this new code matches the indent for the while loop, so it is part of the loop.*

```python
import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the 'files/calendar.txt' file
file_path = os.path.join(script_dir, "files", "calendar.txt")

# Ensure the 'files' directory exists
os.makedirs(os.path.dirname(file_path), exist_ok=True)

myEvents = []

def prettyPrint():
  print()
  for row in myEvents:
    print(f"{row[0] :^15} {row[1] :^15}")
  print()

while True:
  menu = input("1: Add, 2: Remove\n")

  if menu == "1":
    event = input("What event?: ").capitalize()
    date = input("What date?: ")
    row = [event, date]
    myEvents.append(row)
    prettyPrint()

  else:
    criteria = input("What event do you want to remove?: ").title()
    for row in myEvents:
      if criteria in row:
        myEvents.remove(row)

  ########### THIS IS THE NEW BIT ########
  f = open(file_path, "w")  # Use the constructed file path
  f.write(str(myEvents))  # Write the list to the file
  f.close()
  #########################################
```

**🐞 There is a potential problem with this system. Try running the program a few times and add events to the calendar.**


## Preventing Data Loss

Did you find the problem?

Yep. Every time we run the program, it creates a new, blank `myEvents[]` list which gets written to the file.

This overwrites any events in the file that we saved when we ran the program previously.

To solve this, we set up the program to load any pre-existing data from the file into the `myEvents` list at the very start of the code.

Pay close attention to the `eval()` function. It's the special sauce here...


<img id="image" src="assets/day51_1.png" alt="Replit Workspace Overview" width="960">

👉 `eval()` takes the text from the file, converts it into running code, and assigns it to `myEvents[]` as a 2D list. Good, eh?

```python
import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the 'files/calendar.txt' file
file_path = os.path.join(script_dir, "files", "calendar.txt")

# Ensure the 'files' directory exists
os.makedirs(os.path.dirname(file_path), exist_ok=True)

myEvents = []

####### THIS IS THE NEW BIT ################
# Open the file with read permissions to load the events
if os.path.exists(file_path):  # Only try to read if the file exists
    f = open(file_path, "r")  
    myEvents = eval(f.read())
    f.close()
########################################

def prettyPrint():
    print()
    for row in myEvents:
        print(f"{row[0] :^15} {row[1] :^15}")
    print()

while True:
    menu = input("1: Add, 2: Remove\n")

    if menu == "1":
        event = input("What event?: ").capitalize()
        date = input("What date?: ")
        row = [event, date]
        myEvents.append(row)
        prettyPrint()

    else:
        criteria = input("What event do you want to remove?: ").title()
        for row in myEvents:
            if criteria in row:
                myEvents.remove(row)

    # Save the updated events to the file
    f = open(file_path, "w")
    f.write(str(myEvents))
    f.close()
```

**Try it out! Did you run the auto-save code first?**


## Common Errors

First, delete any other code in your `day51.py` file. Copy each code snippet below into `day51.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

### No Such File

👉 Why am I getting a 'no such file' error?

```python
f = open("calendar.txt","r") 
myEvents = eval(f.read())
f.close()
```

<details>
<summary>👀 Answer</summary>
Well friends, this happens when the file does not exist yet. The auto-load code below tries to open the file and if it can't find it, it crashes. There has to be a 'calendar.txt' file for it to work.

This fix is a temporary one because we'll learn how to sort this properly in tomorrow's lesson.

For today, we'll just comment out the auto-load code to give the auto-save the chance to create the file.

```python
#f = open("calendar.txt","r") 
#myEvents = eval(f.read())
#f.close()
```

Once the file has been created, remove the comments to enable auto-load.

</details>


## Fix My Code

👉 Try and fix this code which is full of errors.

First, delete any other code in your `day51.py` file. Copy each code snippet below into `day51.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

```python
myEvents = []

f = open("calendar.txt","r")
myEvents = eval(f.read())
f.close()

def prettyPrint():
  print()
  for row in myEvents:
    print(f"{row[0] :^15} {row[1] :^15}")
  print()

while True:
  menu = input("1: Add, 2: Remove\n")

  if menu == "1":
    event = input("What event?: ").capitalize()
    date = input("What date?: ")
    row = [event,date]
    myEvents.append(row)
    prettyPrint()

  else:
    criteria = input("What event do you want to remove?: ").title()
    for row in myEvents:
      if criteria in row:
        myevents.remove(row)

  
f = open("calendar.txt", "w") 
f.write(str(myEvents)) 
f.close()
```

<details>
<summary>👀 Answer</summary>

```python
import os

myEvents = []

# Will crash on first run if file doesn't exist
#f = open("calendar.txt","r") 
#myEvents = eval(f.read())
#f.close() # Forgot to close the file


def prettyPrint():
  print()
  for row in myEvents:
    print(f"{row[0] :^15} {row[1] :^15}")
  print()

while True:
  menu = input("1: Add, 2: Remove\n")

  if menu == "1":
    event = input("What event?: ").capitalize()
    date = input("What date?: ")
    row = [event,date]
    myEvents.append(row)
    prettyPrint()

  else:
    criteria = input("What event do you want to remove?: ").title()
    for row in myEvents:
      if criteria in row:
        myEvents.remove(row) # List identifier wasn't correct

  # Lines below weren't indented to make them part of the loop.
  # Get the directory where the script is located
  script_dir = os.path.dirname(os.path.abspath(__file__))

  # Construct the path to the 'files/calendar.txt' file
  file_path = os.path.join(script_dir, "files/calendar.txt")
  f = open(file_path, "w") 
  f.write(str(myEvents)) 
  f.close()
```

</details>


## 👉 Day 51 Challenge

###  Someone is wrong on the Internet!
Remember the early days when all this was just lists?

Good! Get back over to Day 45 and grab your to do list code. You'll need it today.

Improve your to do list to add auto-save and auto-load.

That's it. Go get 'em, tiger!

<details>
<summary>💡 Hints</summary>

- Nothing today, just look back at the lesson and add the relevant code sections to your 'to do' program.

</details>


## Solution (No Peeking!)

<a href="https://youtu.be/bK3-x_9iFh8?si=rA0z9LIaiIZTjfAO" target="_blank">Solution video</a>

<details>
<summary>👀 Answer</summary>

```python
import os
import time

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the 'files/todo_list.txt' file
file_path = os.path.join(script_dir, "files/todo_list.txt")

# Clear the console based on the operating system
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def sleep():
    time.sleep(1)
    clear_console()

def ensure_file_exists():
    if not os.path.exists(file_path):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Ensure directory exists
        f = open(file_path, 'w')
        f.close()

def print_todo_list_by_priority(priority):
    ensure_file_exists()
    filtered_list = []
    f = open(file_path, "r")
    for line in f:
        parts = line.strip().split(" (Priority: ")
        if len(parts) == 2:
            item_priority = int(parts[1].rstrip(")"))
            if item_priority == priority:
                filtered_list.append(parts[0])
    f.close()

    if not filtered_list:
        print(f"\n--- No items with priority {priority} ---\n")
    else:
        print(f"\n--- To-do items with priority {priority} ---")
        for index, item in enumerate(filtered_list):
            print(f"{index + 1}: {item}")
        print()

def add_item_to_list():
    ensure_file_exists()
    print("\nLet's add a new item to your list!\n")
    priority = int(input("What is the priority of this task?\n1: High\n2: Medium\n3: Low\nEnter the number: "))
    item = input("\nWhat should I add to your to-do list? ")

    f = open(file_path, "a")
    f.write(f"{item} (Priority: {priority})\n")
    f.close()

    print(f"\n--- {item} added to your list. ---\n")

def print_from_file():
    ensure_file_exists()
    f = open(file_path, "r")
    todo_list = f.readlines()
    f.close()

    if not todo_list:
        print("\n--- Your to-do list is empty. ---\n")
    else:
        print("\n--- Your To-do List ---")
        for idx, item in enumerate(todo_list, start=1):
            print(f"{idx}. {item.strip()}")
        print()

def update_item_in_todo_list():
    ensure_file_exists()
    print_from_file()
    item_index = int(input("\nWhich item would you like to update? ")) - 1

    f = open(file_path, "r")
    lines = f.readlines()
    f.close()

    if item_index < 0 or item_index >= len(lines):
        print("\nInvalid item index.")
        return

    current_item = lines[item_index].strip()

    parts = current_item.split(" (Priority: ")
    if len(parts) != 2:
        print("\nInvalid item format.")
        return

    current_priority = int(parts[1].rstrip(")"))
    current_item_text = parts[0]

    print(f"\nEditing item: {current_item_text} (Priority: {current_priority})\n")

    new_priority = int(input("What is the new priority?\n1: High\n2: Medium\n3: Low\nEnter the number: "))
    new_item_text = input("\nWhat should I update this to? ")

    updated_item = f"{new_item_text} (Priority: {new_priority})\n"
    lines[item_index] = updated_item

    f = open(file_path, "w")
    f.writelines(lines)
    f.close()

    print(f"\n--- Updated item: {new_item_text} (Priority: {new_priority}) ---\n")

def remove_item_from_todo_list():
    ensure_file_exists()
    while True:
        print_from_file()
        item_index = int(input("\nWhich item by index would you like to remove? ")) - 1

        f = open(file_path, "r")
        lines = f.readlines()
        f.close()

        if item_index < 0 or item_index >= len(lines):
            print("\nInvalid item index.")
            return

        removed_item = lines.pop(item_index).strip()

        f = open(file_path, "w")
        f.writelines(lines)
        f.close()

        parts = removed_item.split(" (Priority: ")
        if len(parts) == 2:
            removed_priority = int(parts[1].rstrip(")"))
            removed_item_text = parts[0]
            print(f"\n--- Removed item: {removed_item_text} (Priority: {removed_priority}) ---\n")
        break

def erase_all_items():
    ensure_file_exists()
    f = open(file_path, "w")
    f.close()
    print("\n--- All items have been erased from the file. ---\n")

def get_menu_option():
    print("=== To-do List Menu ===")
    print("1: Add a to-do")
    print("2: Remove a to-do")
    print("3: View to-do list")
    print("4: Edit a to-do")
    print("5: Erase the list")
    print("6: Exit")
    return input("\nSelect an option (1/2/3/4/5/6): ")

def get_priority_option():
    print("\n--- View by priority ---")
    print("1: High")
    print("2: Medium")
    print("3: Low")
    print("4: All")
    return input("\nSelect an option (1/2/3/4): ")

while True:
    print("\n--- To-do List Manager 📝 ---\n")
    ensure_file_exists()
    
    option = get_menu_option()
    if option == "1":
        add_item_to_list()
    elif option == "2":
        remove_item_from_todo_list()
    elif option == "3":
        priority_opt = get_priority_option()
        if priority_opt in ["1", "2", "3"]:
            print_todo_list_by_priority(int(priority_opt))
        elif priority_opt == "4":
            print_from_file()
        else:
            print("\nInvalid option.")
    elif option == "4":
        update_item_in_todo_list()
    elif option == "5":
        confirm_erase = input("\nAre you sure you want to erase your list? (yes/no): ").strip().lower()
        if confirm_erase == "yes":
            erase_all_items()
        else:
            print("\nErase canceled.")
    elif option == "6":
        print("\n--- Goodbye! ---\n")
        break
    else:
        print("\nInvalid option. Please choose a valid option (1/2/3/4/5/6).")

    sleep()
```

</details>