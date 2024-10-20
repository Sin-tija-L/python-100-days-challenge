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
