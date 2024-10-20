# 👉 Day 71: It's Called Hashing


### 👉 This days challenge should be run from Terminal


One of the big issues with storing usernames and passwords in a database is what happens if we're hacked?

If those passwords are stored as text, our users' security is compromised. Probably across multiple sites because they ignored our advice and used the same password for everything!

## Hashing

In reality, organizations don't store your actual password. They store a **hash** of your password. A hash is produced by turning your password into a sequence of numbers, then passing it through a **hashing algorithm** (a mathematical process that is very difficult to reverse engineer). The data spit out by this hashing algorithm is what's stored instead of your actual password.

We can use Python's built-in `hash()` function to create a numerical hash of the password.

Here's a simple example:

```python
def hash_password(password):
    # Use the built-in hash function to hash the password
    hashed_password = hash(password)
    return hashed_password

# Prompt the user for a password
user_password = input("Enter your password: ")

# Hash the password and display the result
hashed = hash_password(user_password)
print(f"Hashed password: {hashed}")
```

Play around with different strings on line 1 and notice how the hash number completely changes.


### Storing Hashed Passwords in a Database

Once we have hashed the password, the next step is to store that hashed version in our database instead of the actual password. In this example, we'll simulate storing the hashed password using Python and SQLite. SQLite is a lightweight, serverless database that's great for small projects or demonstrations.

```python
import sqlite3

# Create (or connect to) a database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create a users table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password_hash TEXT NOT NULL
)
''')

# Function to hash a password
def hash_password(password):
    return hash(password)

# Function to insert a new user into the database
def store_user(username, password):
    password_hash = hash_password(password)
    cursor.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)', (username, str(password_hash)))
    conn.commit()

# Example usage
username = input("Enter your username: ")
password = input("Enter your password: ")

# Store the username and hashed password in the database
store_user(username, password)

# Close the database connection
conn.close()

print(f"User {username} has been added to the database with a hashed password.")
```


### Printing the Hash

👉 Now I can output the value from the database using `print`. Notice how it outputs the hash. That will be useless to a hacker. They cannot easily reverse engineer the password from the hash.

Let's retrieve the stored hashed password from our database and print it.

```python
import sqlite3

# Function to retrieve the hashed password from the database
def get_user_password_hash(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Retrieve the user's hashed password from the database
    cursor.execute('SELECT password_hash FROM users WHERE username = ?', (username,))
    result = cursor.fetchone()
    
    conn.close()
    
    if result:
        return result[0]
    else:
        return None

# Example usage
username = input("Enter the username to retrieve the password hash: ")

# Retrieve and print the hashed password from the database
hashed_password = get_user_password_hash(username)

if hashed_password:
    print(f"Hashed password for {username}: {hashed_password}")
else:
    print(f"User {username} not found.")
```


### Login System: Checking Hashed Passwords

To log in a user, we get their inputted password, hash it, and compare it to the hash stored in the database. This works because the same password string will always produce the same hashed value.

👉 Let's build a login system that checks the stored hash against a hash of the input.

```python
import sqlite3

# Function to hash a password
def hash_password(password):
    return hash(password)

# Function to retrieve the stored hashed password from the database
def get_user_password_hash(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT password_hash FROM users WHERE username = ?', (username,))
    result = cursor.fetchone()
    
    conn.close()
    
    if result:
        return result[0]
    else:
        return None

# Function to verify user login
def login(username, password):
    stored_hash = get_user_password_hash(username)
    if stored_hash:
        # Hash the input password and compare it with the stored hash
        input_hash = hash_password(password)
        if str(input_hash) == stored_hash:
            print("Login successful!")
        else:
            print("Incorrect password.")
    else:
        print("User not found.")

# Example usage
username = input("Enter your username: ")
password = input("Enter your password: ")

# Attempt to log in
login(username, password)
```

**Try it out!**


## Oooh, Salty!

Hashing is great, but enterprising hackers have created their own databases containing hashes of almost every common word and password. These are called **rainbow tables**, and they allow attackers to quickly look up the hash of common passwords and reverse-engineer them.

So, if you use a common password or everyday word, there's a good chance its hash is sitting in a database on the internet, just waiting for a reverse lookup.

To help combat this, we can generate a random value and append (or prepend) it to your password before hashing. This random value is called a **salt**. Adding a salt makes it significantly harder for hackers to use rainbow tables, as the salted password will produce a completely different hash.

👉 Let's add a salt to our password hash from before.

```python
import sqlite3
import os

# Function to generate a random salt
def generate_salt():
    return os.urandom(16).hex()  # Generate a random 16-byte salt and convert it to a hexadecimal string

# Function to hash a password with a salt
def hash_password(password, salt):
    salted_password = password + salt
    return hash(salted_password)

# Function to store a user's hashed password and salt in the database
def store_user_with_salt(username, password):
    salt = generate_salt()
    password_hash = hash_password(password, salt)
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    cursor.execute('INSERT INTO users (username, password_hash, salt) VALUES (?, ?, ?)', (username, str(password_hash), salt))
    conn.commit()
    conn.close()

# Example usage
username = input("Enter your username: ")
password = input("Enter your password: ")

# Store the username, hashed password, and salt in the database
store_user_with_salt(username, password)

print(f"User {username} has been added to the database with a salted, hashed password.")
```


### Updating the Database to Include Salt

To store both the hashed password and the salt, we'll need to update the database schema to include a new column for the salt.

```python
import sqlite3

# Connect to the existing database (or create it if it doesn't exist)
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Alter the 'users' table to add a new column 'salt'
# This assumes that the 'users' table already exists and initially didn't have a 'salt' column.
try:
    cursor.execute('ALTER TABLE users ADD COLUMN salt TEXT')
    print("Column 'salt' added successfully.")
except sqlite3.OperationalError:
    print("Column 'salt' already exists or cannot be added.")

# Commit the changes and close the connection
conn.commit()
conn.close()
```


### Login System with Salting

Now, let's update the login system to handle salted passwords. We'll need to retrieve both the salt and the hashed password from the database, use the same salt to hash the input password, and compare the results.

```python
import sqlite3
import os

# Step 1: Generate a random salt
# Salts are random values that are appended or prepended to passwords before hashing.
# This ensures that even if two users have the same password, their hashed passwords will be different.
def generate_salt():
    return os.urandom(16).hex()  # Generate a 16-byte random salt and convert it to a hexadecimal string

# Step 2: Hash the password with the salt
# Here we concatenate the password and the salt before hashing it to ensure that the hash is unique
def hash_password(password, salt):
    salted_password = password + salt  # Append the salt to the password
    password_hash = hash(salted_password)  # Hash the salted password
    print(f"Password: {password}")
    print(f"Salt: {salt}")
    print(f"Salted Password: {salted_password}")
    print(f"Password Hash: {password_hash}\n")
    return password_hash

# Step 3: Store a user's hashed password and salt in the database
def store_user_with_salt(username, password):
    # Generate a random salt for this user
    salt = generate_salt()
    
    # Hash the password with the generated salt
    password_hash = hash_password(password, salt)
    
    # Connect to (or create) the database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Create the users table if it doesn't already exist, with columns for the username, password hash, and salt
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password_hash TEXT NOT NULL,
        salt TEXT NOT NULL
    )
    ''')

    # Insert the username, hashed password, and salt into the users table
    cursor.execute('INSERT INTO users (username, password_hash, salt) VALUES (?, ?, ?)', 
                   (username, str(password_hash), salt))
    
    # Commit the changes and close the database connection
    conn.commit()
    conn.close()

# Step 4: Retrieve the stored hashed password and salt from the database
def get_user_password_hash_and_salt(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # We will use the LOWER() function to ignore case while retrieving the username
    cursor.execute('SELECT password_hash, salt FROM users WHERE LOWER(username) = LOWER(?)', (username.strip(),))
    result = cursor.fetchone()
    
    conn.close()

    # If the user exists, return the password hash and salt, otherwise return None
    if result:
        stored_hash, salt = result
        print(f"Stored Hash: {stored_hash}")
        print(f"Stored Salt: {salt}\n")
        return result
    else:
        return None, None

# Step 5: Login system that verifies a user's password
def login(username, password):
    # Retrieve the stored hash and salt for the given username
    stored_hash, salt = get_user_password_hash_and_salt(username)
    
    # If the username exists, proceed to hash the input password with the stored salt
    if stored_hash and salt:
        # Hash the input password with the stored salt
        input_hash = hash_password(password, salt)
        
        # Compare the input hash with the stored hash
        if str(input_hash) == stored_hash:
            print("Login successful!")
        else:
            print("Incorrect password.")
    else:
        print("User not found.")

# Step 6: Example usage of the system
# Store a new user with a salted password
username = input("Enter your username: ")
password = input("Enter your password: ")

# Store the username, hashed password, and salt in the database
store_user_with_salt(username, password)

# Attempt to log in with the same username and password
username_login = input("Enter your username to log in: ")
password_login = input("Enter your password to log in: ")

# Attempt to log in
login(username_login, password_login)
```

**Wondering why your code is not working? 😅**

The problem lies in how Python’s `hash()` function works. The built-in `hash()` function in Python is not deterministic across different program runs because it uses a random seed each time the Python process starts. This means the hash for the same input can change between different executions of the program.

To fix this, you should use a cryptographic hash function like **SHA-256**, which will always produce the same hash for the same input. The `hashlib` library in Python provides such functions.

Here's the corrected version of your code, using `hashlib` instead of Python's built-in `hash()`:

```python
import sqlite3
import os
import hashlib

# Step 1: Generate a random salt
def generate_salt():
    return os.urandom(16).hex()  # Generate a 16-byte random salt and convert it to a hexadecimal string

# Step 2: Hash the password with the salt using SHA-256
def hash_password(password, salt):
    salted_password = password + salt  # Append the salt to the password
    password_hash = hashlib.sha256(salted_password.encode()).hexdigest()  # Hash the salted password using SHA-256
    print(f"Password: {password}")
    print(f"Salt: {salt}")
    print(f"Salted Password: {salted_password}")
    print(f"Password Hash: {password_hash}\n")
    return password_hash

# Step 3: Store a user's hashed password and salt in the database
def store_user_with_salt(username, password):
    # Generate a random salt for this user
    salt = generate_salt()
    
    # Hash the password with the generated salt
    password_hash = hash_password(password, salt)
    
    # Connect to (or create) the database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Create the users table if it doesn't already exist, with columns for the username, password hash, and salt
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password_hash TEXT NOT NULL,
        salt TEXT NOT NULL
    )
    ''')

    # Insert the username, hashed password, and salt into the users table
    cursor.execute('INSERT INTO users (username, password_hash, salt) VALUES (?, ?, ?)', 
                   (username, password_hash, salt))
    
    # Commit the changes and close the database connection
    conn.commit()
    conn.close()

# Step 4: Retrieve the stored hashed password and salt from the database
def get_user_password_hash_and_salt(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # We will use the LOWER() function to ignore case while retrieving the username
    cursor.execute('SELECT password_hash, salt FROM users WHERE LOWER(username) = LOWER(?)', (username.strip(),))
    result = cursor.fetchone()
    
    conn.close()

    # If the user exists, return the password hash and salt, otherwise return None
    if result:
        stored_hash, salt = result
        print(f"Stored Hash: {stored_hash}")
        print(f"Stored Salt: {salt}\n")
        return result
    else:
        return None, None

# Step 5: Login system that verifies a user's password
def login(username, password):
    # Retrieve the stored hash and salt for the given username
    stored_hash, salt = get_user_password_hash_and_salt(username)
    
    # If the username exists, proceed to hash the input password with the stored salt
    if stored_hash and salt:
        # Hash the input password with the stored salt
        input_hash = hash_password(password, salt)
        
        # Compare the input hash with the stored hash
        if input_hash == stored_hash:
            print("Login successful!")
        else:
            print("Incorrect password.")
    else:
        print("User not found.")

# Step 6: Example usage of the system
# Store a new user with a salted password
username = input("Enter your username: ")
password = input("Enter your password: ")

# Store the username, hashed password, and salt in the database
store_user_with_salt(username, password)

# Attempt to log in with the same username and password
username_login = input("Enter your username to log in: ")
password_login = input("Enter your password to log in: ")

# Attempt to log in
login(username_login, password_login)
```

### If you are getting message 'User not found' then try this!

It will delete all rows where Salt in Null. Then run your code again!

```python
import sqlite3

# Connect to the database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Delete rows where the salt is NULL or the password hash seems incorrect
# For example, we expect the password hash to be a 64-character string when using SHA-256
cursor.execute('DELETE FROM users WHERE salt IS NULL OR LENGTH(password_hash) != 64')

conn.commit()
conn.close()

print("Deleted invalid rows from the database.")
```


### Second User

👉 If we have a second user with the same password, the uniquely generated salt will produce a completely different hash. This is because even though the password is the same, the salt (which is randomly generated for each user) ensures that the resulting hashed value will be unique.

This is one of the key advantages of salting: even if two users choose the same password, the stored hashed values in the database will be completely different due to the unique salts.

For example:

- **User 1:**
  - Password: `pass123`
  - Salt: `05d2236f8ef8ca4635acec1d7301b7f8`
  - Hash: `75fa31e5bb143fd431600525e41dc1cd8255706d2adc40e579ef3c0e00979492`

- **User 2:**
  - Password: `pass123`
  - Salt: `3bbb553d3b0c0c0a0b3dac821f5ab151`
  - Hash: `3489cfff1883be91a55225e14107c96b9ab561bb5eb6fdcba222a352598af014`

As you can see, even though both users have chosen the same password (`pass123`), their stored password hashes are completely different because each user has a unique salt. This ensures that even if an attacker gains access to the database, they cannot easily infer common passwords across multiple users.

Salting enhances security by adding uniqueness to each stored password, making it significantly harder to break.


### Storing Hashed Password and Salt in a Dictionary

👉 To deal with storing both the hashed password and the salt, we can use a dictionary to store these values together. The dictionary will hold the username as the key, and a dictionary of the hashed password and salt as the value.

This allows us to easily retrieve the salt and hashed password for each user when needed. Here's how we can implement it in Python.

**Example Code**

```python
import hashlib
import os

# Step 1: Generate a random salt
def generate_salt():
    return os.urandom(16).hex()  # Generate a 16-byte random salt and convert it to a hexadecimal string

# Step 2: Hash the password with the salt using SHA-256
def hash_password(password, salt):
    salted_password = password + salt  # Append the salt to the password
    password_hash = hashlib.sha256(salted_password.encode()).hexdigest()  # Hash the salted password using SHA-256
    return password_hash

# Step 3: Create a dictionary to store user information (hashed password and salt)
users_db = {}

# Step 4: Function to store a user's hashed password and salt in the dictionary
def store_user(username, password):
    salt = generate_salt()  # Generate a random salt for this user
    password_hash = hash_password(password, salt)  # Hash the password with the generated salt
    users_db[username] = {'password_hash': password_hash, 'salt': salt}  # Store the hashed password and salt in the dictionary
    print(f"User '{username}' added with hashed password and salt.\n")

# Step 5: Function to verify a user's login by comparing the hash
def verify_user(username, password):
    if username in users_db:
        stored_hash = users_db[username]['password_hash']
        stored_salt = users_db[username]['salt']
        input_hash = hash_password(password, stored_salt)  # Hash the input password with the stored salt
        if input_hash == stored_hash:
            print(f"Login successful for user '{username}'!")
        else:
            print("Incorrect password.")
    else:
        print("User not found.")

# Example usage
# Storing users in the dictionary
store_user("Alise", "pass123")
store_user("Bob", "mypassword")

# Verifying users' login
verify_user("Alise", "pass123")  # Should succeed
verify_user("Bob", "wrongpassword")  # Should fail
```


### Updating the Login System

👉 Now let's update the login system to pull the salt from the database (or dictionary in this case), append it to the password entered by the user, and then hash the combination. After hashing the input, we can compare the result with the stored hash of the password and salt from the previous example.

This ensures that even if two users have the same password, the unique salt for each user will lead to a different hash, thus providing secure authentication.

**Example Code**

```python
import hashlib
import os

# Step 1: Generate a random salt
def generate_salt():
    return os.urandom(16).hex()  # Generate a 16-byte random salt and convert it to a hexadecimal string

# Step 2: Hash the password with the salt using SHA-256
def hash_password(password, salt):
    salted_password = password + salt  # Append the salt to the password
    password_hash = hashlib.sha256(salted_password.encode()).hexdigest()  # Hash the salted password using SHA-256
    return password_hash

# Step 3: Create a dictionary to store user information (hashed password and salt)
users_db = {}

# Step 4: Function to store a user's hashed password and salt in the dictionary (simulating a database)
def store_user(username, password):
    salt = generate_salt()  # Generate a random salt for this user
    password_hash = hash_password(password, salt)  # Hash the password with the generated salt
    users_db[username] = {'password_hash': password_hash, 'salt': salt}  # Store the hashed password and salt in the dictionary
    print(f"User '{username}' added with hashed password and salt.\n")

# Step 5: Updated login system to pull salt from the "database" and verify login
def verify_user(username, password):
    if username in users_db:
        stored_hash = users_db[username]['password_hash']  # Retrieve the stored hash
        stored_salt = users_db[username]['salt']  # Retrieve the stored salt
        
        # Hash the input password with the stored salt
        input_hash = hash_password(password, stored_salt)
        
        # Compare the input hash with the stored hash
        if input_hash == stored_hash:
            print(f"Login successful for user '{username}'!")
        else:
            print("Incorrect password.")
    else:
        print("User not found.")

# Example usage
# Storing users in the dictionary
store_user("Alise", "pass123")
store_user("Bob", "mypassword")

# Verifying users' login by pulling the salt from the dictionary and hashing the input
verify_user("Alise", "pass123")  # Should succeed
verify_user("Bob", "wrongpassword")  # Should fail
verify_user("Bob", "mypassword")  # Should succeed
```


**Try it out!**


## Common Errors
 
 First, delete any other code in your `day71.py` file. Copy each code snippet below into `day71.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.


### It's Not Logging Me In

👉 What's the problem here?

 ```python
import hashlib
import os

def generate_salt():
    return os.urandom(16).hex()

def hash_password(password, salt):
    salted_password = password + salt
    password_hash = hashlib.sha256(salted_password.encode()).hexdigest()
    return password_hash

users_db = {}

def store_user(username, password):
    salt = generate_salt()
    password_hash = hash_password(password, salt)
    users_db[username] = {'password_hash': password_hash, 'salt': salt}
    print(f"User '{username}' added.\n")

def verify_user(username, password):
    if username in users_db:
        stored_hash = users_db[username]['password_hash']
        stored_salt = users_db[username]['salt']
        
        input_hash = hash_password(password, generate_salt()) 
        
        if input_hash == stored_hash:
            print(f"Login successful for user '{username}'!")
        else:
            print("Incorrect password.")
    else:
        print("User not found.")

store_user("Alise", "pass123")
store_user("Bob", "mypassword")

verify_user("Alise", "pass123")  # Should succeed but will fail
verify_user("Bob", "mypassword")  # Should succeed but will fail
```

<details>
<summary>👀 Answer</summary>

The problem in this falsy code lies in the line where the `verify_user` function hashes the input password. Instead of using the stored salt to hash the password, a new salt is generated during the login attempt (`generate_salt()`), which makes the hashed password incorrect every time.

Even though the password is correct, the input hash never matches the stored hash because the salt used to generate it is different.

👉 To fix this, the code should use the stored salt during the login process, not generate a new one.

```python
import hashlib
import os

def generate_salt():
    return os.urandom(16).hex()

def hash_password(password, salt):
    salted_password = password + salt
    password_hash = hashlib.sha256(salted_password.encode()).hexdigest()
    return password_hash

users_db = {}

def store_user(username, password):
    salt = generate_salt()
    password_hash = hash_password(password, salt)
    users_db[username] = {'password_hash': password_hash, 'salt': salt}
    print(f"User '{username}' added.\n")

def verify_user(username, password):
    if username in users_db:
        stored_hash = users_db[username]['password_hash']
        stored_salt = users_db[username]['salt']
        
        input_hash = hash_password(password, stored_salt)
        
        if input_hash == stored_hash:
            print(f"Login successful for user '{username}'!")
        else:
            print("Incorrect password.")
    else:
        print("User not found.")

store_user("Alise", "pass123")
store_user("Bob", "mypassword")

verify_user("Alise", "pass123")  # Should succeed
verify_user("Bob", "mypassword")  # Should succeed
```

</details>


## 🛡️ **Day 71 Challenge: Build a Secure Login System!**

Today, you'll become a cyber guardian as you build a *fortress-like* login system! 🔒💻

### 💡 Your Mission:
Create a program that can *protect* users' credentials with **encryption magic** and give them access to their own personal vault!

### 🔧 **System Features:**
1. **Main Menu**:
   - Show a menu with two options:
     1. **Add** a new user ➕
     2. **Login** to an existing account 🔑

2. **Adding a New User**:
   - Ask for a **username** and **password** ✍️.
   - **Generate a unique 4-digit salt** for each user (e.g., `8521`).
   - Combine the salt with the password and **hash** it using a *secure hashing algorithm* 🔏.
   - **Store** the **username**, **hash**, and **salt** in a Replit database 🔐.

3. **Logging In**:
   - Ask for **username** and **password** inputs 🧑‍💻.
   - Retrieve the stored salt, re-hash the password, and **validate** if the credentials match 🗝️.
   - If they match, display a triumphant **"Access Granted!"** 🎉.
   - If not, show **"Invalid credentials"**. 🚫

### 🏆 **Bonus Objectives**:
- The system should **support multiple users** without overlap.
- Try adding **feedback** like:
  - "Username already exists, please choose another."
  - "User successfully created!"

---

### **Example Output:**

<img id="image" src="assets/day71_1.png" alt="day70 image" width="960">

---

### Ready to step up your security game and build a vault-worthy login system? Let’s do this! 🛡️🚀


<details>
<summary>💡 Hints</summary>

- For each menu option create a function

</details>


## Solution (No Peeking!)


<details>
<summary>👀 Answer</summary>

```python
import hashlib
import random

# Dictionary to simulate Replit database
users_db = {}

# Function to generate a random 4-digit salt
def generate_salt():
    return str(random.randint(1000, 9999))  # Generate a 4-digit numeric salt

# Function to hash the password with salt using SHA-256
def hash_password(password, salt):
    salted_password = password + salt
    password_hash = hashlib.sha256(salted_password.encode()).hexdigest()  # Secure hashing using SHA-256
    return password_hash

# Function to add a new user
def add_user():
    username = input("Enter username: ")
    
    # Check if username already exists
    if username in users_db:
        print("Username already exists, please choose another.")
        return
    
    password = input("Enter password: ")
    salt = generate_salt()  # Generate unique salt
    password_hash = hash_password(password, salt)  # Hash password with salt

    # Store user credentials in "database"
    users_db[username] = {"password_hash": password_hash, "salt": salt}
    print(f"🎉 User {username} successfully created!\n")

# Function to login a user
def login():
    username = input("Enter username: ")
    
    # Check if user exists
    if username not in users_db:
        print("Invalid credentials.")
        return
    
    password = input("Enter password: ")
    stored_hash = users_db[username]["password_hash"]  # Get stored password hash
    stored_salt = users_db[username]["salt"]  # Get stored salt

    # Hash the input password with the stored salt
    input_hash = hash_password(password, stored_salt)

    # Compare the input hash with the stored hash
    if input_hash == stored_hash:
        print("🎉 Access Granted!\n")
    else:
        print("🚫 Invalid credentials.\n")

# Main Menu
def main_menu():
    while True:
        print("1: Add User")
        print("2: Login")
        print("3: Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_user()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please select again.\n")

# Start the system
main_menu()
```

</details>