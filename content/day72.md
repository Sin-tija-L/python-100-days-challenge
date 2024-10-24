# 🛡️ Day 72 Challenge: Secure Your Diary!

Now that you've mastered secure password management, it's time to protect your personal diary with proper encryption.

### 💡 Your Mission:
Take your diary code from Day 62 and upgrade it to include **user authentication** using **salted and hashed passwords**.

### 🔒 Features to Add:

1. **User Setup**:
   - The **first time** the program runs, the user must create a **username** and **password**.
   - The password should be **salted** and **hashed** using a secure algorithm.
   - Store the **username**, **salt**, and **hashed password** in the "database."

2. **User Authentication**:
   - On subsequent program runs, prompt the user for their **username** and **password**.
   - Only allow access to the diary if the provided credentials are **correct**.
   - Use the stored salt to hash the input password and compare it to the stored hash for validation.

3. **Diary Access**:
   - Once authenticated, allow the user to add, view, or delete diary entries.
   - **Exclude** the **username**, **password**, and **salt** from any diary entry outputs for security reasons.

### 🏆 Bonus Objective:
- Ensure that only authenticated users can access or modify the diary entries.

### Example Output:

1. **First Time Run (User Setup)**:
   - `Enter a new username: coder123`
   - `Enter a new password: secretpass`
   - 🎉 `"User created successfully!"`

2. **Subsequent Run (User Authentication)**:
   - `Enter username: coder123`
   - `Enter password: secretpass`
   - 🎉 `"Access Granted!"`

3. **Diary Menu**:
   - `1: Add Entry`
   - `2: View Entries`
   - `3: Delete Entry`
   - `4: Exit`

---

Ready to lock down your diary with high-level security? Let’s do it! 🔐📔


<details>
<summary>💡 Hints</summary>

- Figure out if it's the first time by counting the keys in the diary. If there are none, it's the first time.
- The username and password will be the **first** key entry in the database. Think about where you start outputting diary entries and adjust your loops.

</details>


## Solution (No Peeking!)


<details>
<summary>👀 Answer</summary>

```python
import hashlib
import os

# Simulated database for storing users and diary entries
users_db = {}
diary_entries = {}

# Function to generate a random salt
def generate_salt():
    return os.urandom(16).hex()

# Function to hash the password with a salt
def hash_password(password, salt):
    return hashlib.sha256((password + salt).encode()).hexdigest()

# Function to create a new user
def create_user():
    username = input("Enter a new username: ")
    
    # Check if username already exists
    if username in users_db:
        print("Username already exists. Try logging in.")
        return
    
    password = input("Enter a new password: ")
    salt = generate_salt()  # Generate unique salt
    password_hash = hash_password(password, salt)  # Hash the password
    
    # Store the user with hashed password and salt in the "database"
    users_db[username] = {"password_hash": password_hash, "salt": salt}
    print("🎉 User created successfully!\n")

# Function to authenticate user
def authenticate_user():
    username = input("Enter username: ")
    
    # Check if the user exists
    if username not in users_db:
        print("User not found. Please create an account.")
        return False
    
    password = input("Enter password: ")
    stored_hash = users_db[username]["password_hash"]
    stored_salt = users_db[username]["salt"]
    
    # Hash the input password with the stored salt
    input_hash = hash_password(password, stored_salt)
    
    if input_hash == stored_hash:
        print("🎉 Access Granted!\n")
        return True
    else:
        print("🚫 Invalid credentials.")
        return False

# Function to add a diary entry
def add_entry(username):
    entry = input("Enter your diary entry: ")
    
    # If the user has no entries, create an empty list
    if username not in diary_entries:
        diary_entries[username] = []
    
    diary_entries[username].append(entry)
    print("📝 Entry added successfully!\n")

# Function to view diary entries
def view_entries(username):
    if username in diary_entries and diary_entries[username]:
        print("\nYour diary entries:")
        for idx, entry in enumerate(diary_entries[username], 1):
            print(f"{idx}. {entry}")
        print()
    else:
        print("You have no diary entries.\n")

# Function to delete a diary entry
def delete_entry(username):
    if username in diary_entries and diary_entries[username]:
        view_entries(username)
        try:
            entry_num = int(input("Enter the number of the entry to delete: "))
            if 1 <= entry_num <= len(diary_entries[username]):
                deleted = diary_entries[username].pop(entry_num - 1)
                print(f"🗑️ Deleted entry: {deleted}\n")
            else:
                print("Invalid entry number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("You have no entries to delete.\n")

# Diary menu after authentication
def diary_menu(username):
    while True:
        print("1: Add Entry")
        print("2: View Entries")
        print("3: Delete Entry")
        print("4: Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_entry(username)
        elif choice == "2":
            view_entries(username)
        elif choice == "3":
            delete_entry(username)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")

# Main function to run the diary system
def main():
    # Check if it's the first run (no users exist)
    if not users_db:
        print("Welcome! Let's create your account.")
        create_user()
    
    # Authenticate the user
    if authenticate_user():
        username = input("Enter your username again to proceed: ")
        diary_menu(username)

# Start the program
main()
```

</details>