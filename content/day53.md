# 👉 Day 53 Challenge: Video Game Inventory

<a href="https://youtu.be/n7Ot7Yi6xDw?si=_CXPz7JpvSwSawrV" target="_blank">📹 Dāvida video</a>

Oh yes! It's classic RPG inventory system time.

Chug a 'stamina potion' and head to the challenge page for full details.

**To run this day's code use terminal and run the file 😎**

---

Your video game inventory system should:

1. Have a menu that allows the user to:
   - i. Add
   - ii. View
   - iii. Remove
2. Adding an item saves it to a file using capitalize mode. Duplicates are allowed.
3. Removing an item deletes it from the file.
4. View is trickier. It should output the name of the item and tell you **how many** of each item you have.
5. Use auto-save and auto-load with `try...except`.

**Example:**

<img id="image" src="assets/day53_1.png" alt="Replit Workspace Overview" width="960">

<details>
<summary>💡 Hints</summary>

- Use the `count()` function when viewing an item.

</details>


## Solution (No Peeking!)

<a href="https://youtu.be/vKiPT8UGv4A" target="_blank">Solution video</a>

<details>
<summary>👀 Answer</summary>

```python
import os
import time

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the 'files/inventory.txt' file
file_path = os.path.join(script_dir, "files", "inventory.txt")

# Ensure the 'files' directory exists
os.makedirs(os.path.dirname(file_path), exist_ok=True)

def sleep():
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

def addInventory():
    item = input("What item would you like to add to your inventory? ")
    f = open(file_path, "a")
    f.write(item.capitalize() + "\n")  
    f.close()
    print("You have added", item, "to your inventory.")

def loadInventory():
    f = open(file_path, "r")
    for line in f:
        print(line.strip())
    f.close()

def removeInventory():
    item = input("What item would you like to remove from your inventory? ")
    f = open(file_path, "r")
    lines = f.readlines()
    f.close()
    f = open(file_path, "w")
    for line in lines:
        if item.capitalize() not in line:
            f.write(line)
    f.close()
    print("You have removed", item, "from your inventory.")

def addToEmptyInventory():
    print("\nYour game inventory is empty.")
    addInventory()
    sleep()

def getOption():
    print("\nMenu:")
    print("1: Add inventory")
    print("2: Remove inventory")
    print("3: View game inventory list")
    return input("Select an option (1/2/3): ")

while True:
    print("\n🌟RPG Inventory🌟")
    try:
        f = open(file_path, "r")
        fileContent = f.read()
        f.close()
        if not fileContent:
            addToEmptyInventory()
            continue
    except FileNotFoundError:
        addToEmptyInventory()
        continue

    option = getOption()
    if option == "1":
        addInventory()
    elif option == "2":
        removeInventory()
    elif option == "3":
        loadInventory()
    else:
        print("Invalid option. Please choose a valid option (1/2/3).")

    sleep()
```

</details>