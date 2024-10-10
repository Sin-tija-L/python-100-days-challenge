# 👉 Day 55: The os Library

<a href="https://youtu.be/-xhn_qFAEmc" target="_blank">📹 Dāvida video</a>

**To run this day's code use terminal and run the file 😎**

Today's lesson is going to use the `os` library to create folders and navigate around them.

Previously, we've used `os` to clear the screen.

Here are a few other things that it can do:


### List a file

👉 `listdir()` will allow you to list all the files:

```python
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
files_dir = os.path.join(script_dir, "files")

# List all files in the 'files/' directory. Useful for checking that a file is in the folder we think it is.
if os.path.exists(files_dir):
    print("Files in 'files/' directory:")
    files = os.listdir(files_dir)
    print(files)
    
    # Check if 'quickSave.txt' is in the 'files/' directory
    if "quickSave.txt" not in files:
        print("Error: Quick Save not found.")
else:
    print("Error: 'files/' directory not found.")
```


### Create a folder

👉 Try this code with `os.mkdir()`:

```python
import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the 'files/' directory
files_dir = os.path.join(script_dir, "files")

# Ensure the 'files/' directory exists
os.makedirs(files_dir, exist_ok=True)

# Construct the path to the 'hello' folder inside the 'files/' directory
hello_folder_path = os.path.join(files_dir, "hello")

# Create the 'Hello' folder inside the 'files/' directory
if not os.path.exists(hello_folder_path):
    os.mkdir(hello_folder_path)
    print(f"'Hello' folder created inside 'files/' directory at: {hello_folder_path}")
else:
    print(f"'Hello' folder already exists at: {hello_folder_path}")
```


### Rename a file

👉 `os.rename()` takes 2 arguments: the file to rename and the new name.

```python
import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the 'files/hello/' directory
hello_dir = os.path.join(script_dir, "files", "Hello")

# Construct the path to the original file ('myname.txt') inside the 'files/hello/' directory
original_file_path = os.path.join(hello_dir, "myname.txt")

# Construct the path to the new file name ('NEW.o') inside the 'files/hello/' directory
new_file_path = os.path.join(hello_dir, "NEW.o")

# Ensure the 'files/hello/' directory exists
if os.path.exists(hello_dir):
    # Check if 'myname.txt' exists
    if os.path.exists(original_file_path):
        # Rename the file
        os.rename(original_file_path, new_file_path)
        print(f"Renamed 'myname.txt' to 'NEW.o' inside the 'files/hello/' directory.")
    else:
        print("Error: 'myname.txt' does not exist in the 'files/hello/' directory.")
else:
    print("Error: 'files/hello/' directory does not exist.")
```
*Hint: You would need a file called `myname.txt` already uploaded to the file tree in `hello` directory in order to change the file name.*

*The ability to create and manage files & folders is really useful, especially for backups.*

#### ...Which brings us to today's challenge!


## 👉 Day 55 Challenge

Back the 'f' up everybody!

'f' is short for 'file', of course. What did you think I meant?

Get your minds out of the gutter, go back and get your auto save/load to do list from Day 51 and use it here.

Your program should:
1. Create a backup folder.
2. Create a random filename.
3. Save a copy of the data to that file.
4. This should all happen before the auto save.


<details>
<summary>💡 Hints</summary>

- Use a Boolean variable `fileExists` set to False to store whether the file has already been created.
- Use if `fileExists` later on to check the status of the file before creating or writing.
- Use the `os.mkdir()` function.

</details>


## Solution (No Peeking!)

<a href="https://youtu.be/D-z7DHlUEXo" target="_blank">Solution video</a>

<details>
<summary>👀 Answer</summary>

```python
import os
import time
import random

file_exists = False  # Use this to track whether the backups folder has been created

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the 'files' directory
files_dir = os.path.join(script_dir, "files")

# Construct the path to the 'backups' folder inside 'files'
backups_dir = os.path.join(files_dir, "backups")

# Construct the path to 'todo_list.txt'
todo_list_path = os.path.join(files_dir, "todo_list.txt")

# Ensure the 'files' directory exists
os.makedirs(files_dir, exist_ok=True)

def load_todo_list():
    try:
        with open(todo_list_path, "r") as f:
            todo = eval(f.read())
        return todo
    except FileNotFoundError:
        return []

def backup_todo_list():
    global file_exists
    if not file_exists:
        os.makedirs(backups_dir, exist_ok=True)
        file_exists = True

    backup_file_name = f"backup{random.randint(1, 1000000000)}.txt"
    backup_file_path = os.path.join(backups_dir, backup_file_name)
    os.popen(f"cp {todo_list_path} {backup_file_path}")
    print(f"Backup saved as {backup_file_name}")

def sleep_and_clear():
    time.sleep(1)
    os.system("cls" if os.name == "nt" else "clear")

def print_todo_list_by_priority(priority):
    filtered_list = []
    with open(todo_list_path, "r") as file:
        for line in file:
            parts = line.strip().split(" (Priority: ")
            if len(parts) == 2:
                item_priority = int(parts[1].rstrip(")"))
                if item_priority == priority:
                    filtered_list.append(parts[0])

    if not filtered_list:
        print(f"No items with {priority} priority.")
    else:
        for index, item in enumerate(filtered_list):
            print(f"{index + 1}: {item}")

def add_item_to_list():
    print("\nLet's add a new item to your list!")
    while True:
        try:
            priority = int(input("What is the priority of this task?\n1: High\n2: Medium\n3: Low\nEnter the number: "))
            if priority not in [1, 2, 3]:
                print("Invalid priority. Please enter 1, 2, or 3.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number (1, 2, or 3).")

    item = input("What should I add to your to-do list? ")

    with open(todo_list_path, "a") as file:
        file.write(f"{item} (Priority: {priority})\n")

    print(f"{item} added to your list.\n")


def print_from_file():
    if not os.path.exists(todo_list_path):
        print("File not found.")
    else:
        with open(todo_list_path, "r") as file:
            todo_list = file.readlines()
            for idx, item in enumerate(todo_list, start=0):
                print(f"{idx}: {item}")

def update_item_in_todo_list():
    print_from_file()
    item_index = int(input("Which item would you like to update? "))

    # Load the current items from the file
    with open(todo_list_path, "r") as file:
        lines = file.readlines()

    if item_index < 0 or item_index >= len(lines):
        print("Invalid item index.")
        return

    current_item = lines[item_index].strip()

    parts = current_item.split(" (Priority: ")
    if len(parts) != 2:
        print("Invalid item format.")
        return

    current_priority = int(parts[1].rstrip(")"))
    current_item_text = parts[0]

    print(f"Editing item: {current_item_text} (Priority: {current_priority})")

    new_priority = int(input("What is the new priority?\n1: High\n2: Medium\n3: Low\nEnter the number: "))
    new_item_text = input("What should I update this to? ")

    updated_item = f"{new_item_text} (Priority: {new_priority})\n"
    lines[item_index] = updated_item

    with open(todo_list_path, "w") as file:
        file.writelines(lines)

    print(f"Updated item: {new_item_text} (Priority: {new_priority})\n")

def remove_item_from_todo_list():
    while True:
        print_from_file()
        try:
            item_index = int(input("\nWhich item by index would you like to remove? "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        with open(todo_list_path, "r") as file:
            lines = file.readlines()

        if item_index < 0 or item_index >= len(lines):
            print("Invalid item index.")
            return

        removed_item = lines.pop(item_index).strip()

        with open(todo_list_path, "w") as file:
            file.writelines(lines)

        parts = removed_item.split(" (Priority: ")
        if len(parts) != 2:
            print("Invalid item format.")
            return

        removed_priority = int(parts[1].rstrip(")"))
        removed_item_text = parts[0]

        print(f"Removed item: {removed_item_text} (Priority: {removed_priority})\n")
        break

def add_to_empty_list():
    print("\nYour To-do is empty.")
    add_item_to_list()
    sleep_and_clear()

def get_menu_option():
    print("Menu:")
    print("1: Add a to-do")
    print("2: Remove a to-do")
    print("3: View to-do list")
    print("4: Edit a to-do")
    print("5: Erase the list")
    print("6: Exit")
    return input("Select an option (1/2/3/4/5/6): ")

def get_priority_option():
    print("\nView by priority:")
    print("1: High")
    print("2: Medium")
    print("3: Low")
    print("4: All")
    return input("Select an option (1/2/3/4): ")

def erase_all_items():
    with open(todo_list_path, "w") as file:
        pass 
    print("All items have been erased from the file.\n")

# Main program loop
while True:
    print("To-do list manager.📝\n")
    try:
        with open(todo_list_path, "r") as f:
            file_content = f.read()
            if not file_content:
                add_to_empty_list()
                continue
    except FileNotFoundError:
        add_to_empty_list()
        continue

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
            print("Invalid option.")
    elif option == "4":
        update_item_in_todo_list()
    elif option == "5":
        confirm_erase = input("Are you sure you want to erase your list? (yes/no): ")
        if confirm_erase.lower() == "yes":
            erase_all_items()
        else:
            print("Erase canceled.")
    elif option == "6":
        break
    else:
        print("Invalid option. Please choose a valid option (1/2/3/4/5/6).")

    # Before auto-saving, create a backup in the 'backups' folder
    backup_todo_list()
    sleep_and_clear()

```

</details>