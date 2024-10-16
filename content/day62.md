# 👉 Day 62 Challenge! 🚀


Create Your Own Secret Diary – Just for You! 💖

Hey there! Today is a fun project day where you'll create your own **private diary** to keep your deepest thoughts and secrets safe from prying eyes. This diary will be password-protected, ensuring that only you can access your entries.

**Features:**
1. Set a Password
- When you first set up your diary, you'll be asked to create an **access password**. This will be your key to unlocking your private space.

2. Password Prompt
Each time you open your diary, you'll be asked to **enter your password**. 
- If the password is incorrect, the program will close, keeping your secrets safe.
- If the password is correct, you'll enter the main menu.

3. Main Menu: Add or View Entries
Once you're in, you'll have two main options:
- **Add**: Write a new diary entry.
    - You will be prompted to write your thoughts, and the entry will be saved in a database with a timestamp.
- **View**: Look at your past entries.
    - The most recent entry will be shown first. You can scroll back through your entries one by one, or exit to return to the main menu.

### 🥳 Bonus Feature:
Want to add an extra layer of coolness? Include a feature where you can view a diary entry from a **specific date** by searching for it!

Now, you can express yourself freely, knowing that your private thoughts are locked away safely!


<details>
<summary>💡 Hints</summary>

- Use `if passwordEntered != correctPassword` to verify the user.
- Use `os.clear()` to clear the screen between each entry viewed.
- Extra points - compare the date entered to the timestamp and only show if date entered >= timestamp.

</details>


## Solution (No Peeking!)

<details>
<summary>👀 Answer</summary>

```python
import sqlite3
import datetime, os, time, random, sys

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('diary.db')
cursor = conn.cursor()

# Create a table to store diary entries if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS diary_entries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    entry TEXT
)
''')
conn.commit()

def sleep(sec):
    time.sleep(sec)
    os.system("clear")

def viewEntry(current_index):
    sleep(1)
    # Fetch all diary entries ordered by timestamp
    cursor.execute('SELECT timestamp, entry FROM diary_entries ORDER BY id')
    entries = cursor.fetchall()

    if not entries:
        print("Your diary is empty.")
        return

    if current_index < 0:
        current_index = 0
    elif current_index >= len(entries):
        current_index = len(entries) - 1

    timestamp, entry = entries[current_index]
    print("Diary Entry:\n")
    print(f"Date: {timestamp}, Entry: {entry}\n")
    sleep(5)

    while True:
        print("Do you want to see:")
        print("1. Next entry")
        print("2. Previous entry")
        print("3. Exit")
        answer = input("> ")
        if answer == "1":
            current_index = viewEntry(current_index + 1)
        elif answer == "2":
            current_index = viewEntry(current_index - 1)
        elif answer == "3":
            return
        else:
            print("Invalid input.")
    return

def addEntry():
    entry = input("Write something: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('''
    INSERT INTO diary_entries (timestamp, entry)
    VALUES (?, ?)
    ''', (timestamp, entry))
    conn.commit()
    sleep(1)

while True:
    print("Write a password to access the diary. 📔")
    print()
    passwords = ["KnockKnockWhosThere", "PasswordHaiku", "HahaHa1rball!", "GiggleP@ssw0rd", "LOLSecurity"]
    randomPass = random.choice(passwords)
    inputPass = input("Enter your password: ")
    
    if inputPass == randomPass:
        print("Access granted! 🎉")
        sleep(1)
        current_index = -1
        while True:
            print("Your Diary. 📝")
            print()
            print("Do you want to:")
            print("1. Add entry")
            print("2. View entries")
            print("3. Exit?")
            answer = input("> ")
            if answer == "1":
                addEntry()
            elif answer == "2":
                viewEntry(current_index)
            elif answer == "3":
                conn.close()  # Close the database connection before exiting
                break
            else:
                print("Invalid choice. Please choose a valid option.")
        sleep(5)
        break
    else:
        print("Access denied.")
        break
```

</details>