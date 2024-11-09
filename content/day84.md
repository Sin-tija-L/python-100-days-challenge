# Day 84: Client/Server Logins with VSCode 🚀

Way back when we learned about using dictionaries to store login data, we touched on the concept of a client/server model for storing data in one place and making it accessible to multiple users. Now, let's take that concept to the next level using Flask! We'll set up a server to persistently store login data using SQLite, allowing multiple clients (users) to access it through a web interface. 🌐

This guide will help you build a simple Flask application in VSCode, using SQLite to securely manage user login details. Let's get started! 📝

### Challenge Instructions (Run in VSCode)

---

## Get Started 💡
Previously, we've built basic login systems using Flask & HTML. Today, we're starting with one of those systems, but instead of a dictionary, we're adapting it to store user data in an SQLite database.

👉 Here's how our Flask app works. Read through the comments in the code for an explanation:

```python
from flask import Flask, request, redirect, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static')

# SQLite setup
conn = sqlite3.connect('user_data.db', check_same_thread=False)
cursor = conn.cursor()

# Create a table to store user login data if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)''')
conn.commit()

# Pre-populate database with sample users
cursor.execute("INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)", ("anna", "TechQueen1"))
cursor.execute("INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)", ("maria", "DesignGuru"))
conn.commit()

@app.route('/login', methods=["POST"])
def login():
    form = request.form
    username = form["username"]
    password = form["password"]

    # Check if user exists and password matches
    cursor.execute("SELECT password FROM users WHERE username=?", (username,))
    result = cursor.fetchone()

    if result and result[0] == password:
        return redirect("/yup")
    else:
        return redirect("/nope")

# Login checking code - uses POST because it's dealing with usernames & passwords so we want encryption

# If the user details are correct, they get a lovely success gif, if not, they get a 'nope' gif.

# Try except used to load the 'nope' in case there's an error.

@app.route("/nope")
def nope():
    return render_template("nope.html")

@app.route("/yup")
def yup():
    return render_template("yup.html")

# The two methods above load the relevant gif depending on the result of the '/login' method

@app.route('/')
def index():
    return render_template("login.html")

# Loads the login HTML page that I've built separately on run.

# Run the app
app.run(host='0.0.0.0', port=81, debug=True)
```

### Static Folder 📁
👉 To make things visually interesting, I've also created a 'static' folder that contains images (gifs) used in the app. Make sure you add it to your project structure along with an HTML file for logging in.

<img id="image" src="assets/day84_1.png" alt="day84 image" width="300">

---

### HTML Files 📝
Below are the HTML files required for the application:

**login.html**:

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>
<body>
    <h2>Login</h2>
    <form method="post" action="/login">
      <p>Username: <input type="text" name="username" required></p>
      <p>Password: <input type="password" name="password" required></p>
      <button type="submit">Log in</button>
    </form>
</body>
</html>
```

**change.html**:

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Change Password</title>
</head>
<body>
    <h2>Change Password</h2>
    <form method="post" action="/changePass">
      <p>Username: <input type="text" name="username" required></p>
      <p>New Password: <input type="password" name="newPassword"></p>
      <button type="submit">Change</button>
    </form>
</body>
</html>
```

**nope.html**:

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Failed</title>
</head>
<body>
    <h2>Login Failed</h2>
    <img src="{{ url_for('static', filename='gifs/nerdy.gif') }}" height="100">
    <p>Incorrect username or password. Please try again.</p>
</body>
</html>
```

**yup.html**:

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Successful</title>
</head>
<body>
    <h2>Login Successful</h2>
    <img src="{{ url_for('static', filename='gifs/yup.gif') }}" height="100">
    <p>Welcome! You can now change your password below.</p>
    <form method="post" action="/changePass">
      <p>Username: <input type="text" name="username" required></p>
      <p>New Password: <input type="password" name="newPassword"></p>
      <button type="submit">Change</button>
    </form>
</body>
</html>
```

---

### Why SQLite? 🤔
SQLite is perfect for simple projects like this. It helps us replace the hard-coded dictionary from before with a real database to make user data persistent and accessible across multiple users! No more resetting user data each time we run the app. 📊

---

## Store and Use Data 🔒
👉 Instead of storing login details in a dictionary, we now use an SQLite database. Here's what we changed:

- We import `sqlite3` to connect to our SQLite database.
- We create a table called `users` to store usernames and passwords.
- User data is stored directly in the database rather than in the code.

### Change User Data ✨
Once logged in successfully, users should have the option to change their password. Let's create a simple form for this:

**change.html** (already shown above):

```python
<form method="post" action="/changePass">
  <p>Username: <input type="text" name="username" required></p>
  <p>New Password: <input type="password" name="newPassword"></p>
  <button type="submit">Change</button>
</form>
```

### Update Password Logic 🔄
Now we add logic to update the user password in the database:

```python
@app.route('/changePass', methods=["POST"])
def change_password():
    form = request.form
    username = form["username"]
    new_password = form["newPassword"]

    cursor.execute("UPDATE users SET password = ? WHERE username = ?", (new_password, username))
    conn.commit()

    return redirect("/")
```

<img id="image" src="assets/day84_2.png" alt="day84 image" width="400">

---

## Ready to Level Up? 💪
Now that you have a working login system using Flask and SQLite, you can think of other cool features to add! Maybe try adding:

- User registration 🔏
- Password hashing for better security 🔐
- Error messages for incorrect login details ❌

Keep experimenting and remember, every line of code is a step toward mastering the magic of tech! ✨👩‍💻👩‍🎓

---

## Common Errors
 
 First, delete any other code in your `day84` files. Copy each code snippet below into `day84` files by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.


### Key Error

👉 What's the problem here?

 ```python
@app.route('/changePass', methods=["POST"])
def change_password():
    form = request.form
    username = form["username"]
    new_password = form["newPassword"]

    cursor.execute("UPDATE test SET password = ? WHERE username = ?", (new_password, username))
    conn.commit()

    return redirect("/")
```

<details>
<summary>👀 Answer</summary>

I was trying to access the database key `test`, which doesn't exist.

This is where `try... except` comes in really handy, because the error messages thrown by an error like this are really horrible.

```python
@app.route('/changePass', methods=["POST"])
def change_password():
    form = request.form
    username = form["username"]
    new_password = form["newPassword"]

    cursor.execute("UPDATE users SET password = ? WHERE username = ?", (new_password, username))
    conn.commit()

    return redirect("/")
```

</details>

---

### Informal

👉 What's the problem here?

 ```python
<body>
    <h2>Login Successful</h2>
    <img src="{{ url_for('static', filename='gifs/yup.gif') }}" height="100">
    <p>Welcome! You can now change your password below.</p>
    <p>Username: <input type="text" name="username" required></p>
    <p>New Password: <input type="password" name="newPassword"></p>
    <button type="submit">Change</button>
</body>
```

<details>
<summary>👀 Answer</summary>

The form was not inside `<form>` tags. This won't look any different, but saving data just won't work.

```python
<body>
    <h2>Login Successful</h2>
    <img src="{{ url_for('static', filename='gifs/yup.gif') }}" height="100">
    <p>Welcome! You can now change your password below.</p>
    <form method="post" action="/changePass">
      <p>Username: <input type="text" name="username" required></p>
      <p>New Password: <input type="password" name="newPassword"></p>
      <button type="submit">Change</button>
    </form>
</body>
```

</details>

---

## Fix My Code

👉 Try and fix this code which is *full* of errors.

First, delete any other code in your `day84` files. Copy each code snippet below into `day84` files by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.


```python
from flask import Flask, request, redirect, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static')

conn = sqlite3.connect('user_data.db', check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)''')
conn.commit()

cursor.execute("INSERT OR IGNORE INTO users (username password) VALUES (?, ?)", ("anna", "TechQueen1"))
cursor.exectue("INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)", ("maria", "DesignGuru"))
conn.commit()

def login():
    form = request.form
    username = form["username"]
    password = form["password"]

    cursor.execute("SELECT password FROM users WHERE username=?", (username))
    result = cursor.fetchone()

    if result and result[0] == password:
        return redirect("/yup")
    else:
        return redirect("/nope")

@app.route('/changePass', methods=["POST"])
def change_password():
    form = request.form
    username = form["username"]
    new_password = form["newPassword"]

    cursor.execute("UPDATE user SET password = ? WHERE username = ?", (new_password, username))
    conn.commit()

    return redirect("/")

@app.route("/nope")
def nope():
    render_template("nope.html")

@app.route("/yup")
def yup():
    return render_template("yup.html")

@app.route('index')
def index():
    return render_template("login.html")

app.run(host='0.0.0.0', port=81, debug=True)

```

<details>
<summary>👀 Answer</summary>

```python
from flask import Flask, request, redirect, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static')

conn = sqlite3.connect('user_data.db', check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)''')
conn.commit()

# Syntax error: missing comma
cursor.execute("INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)", ("anna", "TechQueen1"))
# Wrong function call: misspelled 'execute'
cursor.execute("INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)", ("maria", "DesignGuru"))
conn.commit()

# Incorrect route method: missing route decorator
@app.route('/login', methods=["POST"])
def login():
    form = request.form
    username = form["username"]
    password = form["password"]

    cursor.execute("SELECT password FROM users WHERE username=?", (username,)) # Missing comma in parameter tuple
    result = cursor.fetchone()

    if result and result[0] == password:
        return redirect("/yup")
    else:
        return redirect("/nope")
    
@app.route('/changePass', methods=["POST"])
def change_password():
    form = request.form
    username = form["username"]
    new_password = form["newPassword"]

    # SQL syntax error: invalid table name
    cursor.execute("UPDATE users SET password = ? WHERE username = ?", (new_password, username))
    conn.commit()

    return redirect("/")

@app.route("/nope")
def nope():
    # Missing return statement
    return render_template("nope.html")

@app.route("/yup")
def yup():
    return render_template("yup.html")

# Wrong route name
@app.route('/')
def index():
    return render_template("login.html")

app.run(host='0.0.0.0', port=81, debug=True)
```

</details>

---

# 🚀 Day 84 Challenge: Build Your Own Flask Signup Website!

Hey there, future web developer! 👩‍💻👨‍💻 Ready to dive into an exciting challenge? Today, we're going to create a dynamic Flask website that features a signup and login system. Let's put your coding skills to work! 💪✨

## 🌟 What You'll Build:

A simple but powerful signup form that allows users to register and log in. You'll be creating a Flask-based web application that interacts with an SQLite database to store user information securely. Let’s break it down step by step! 📝

## ✨ Your Signup Form Should:

- 📝 **Collect User Information**: The form should ask for the user's **name**, **username**, and **password**.
- 🗄️ **Create a User Account**: Store the user information (name, username, password) in an **SQLite database** to keep the data persistent and secure.
- 🔄 **Redirect to Login**: After successfully signing up, direct the user to a **login form**, where they can enter their **username** and **password** to access their account.
- 👋 **Greet the User**: If the login details are correct, show a friendly message like **'Hello, [User's Name]!'** to make them feel welcome! 😊

## 🌐 Why This Challenge?

- You'll learn to **handle user input** and work with forms in Flask, one of the most popular Python frameworks for web development. 🐍
- Practice working with **databases** (in this case, SQLite) to store and manage user data. 💾
- Gain a better understanding of **client-server interaction**, authentication, and web forms.

## 🚀 Tips to Get Started:

1. **Build the HTML Forms**: Design your signup and login forms with fields for **name**, **username**, and **password**. Keep it simple and functional! 💻
2. **Create Your Routes**: Use Flask to create routes for the signup (`/signup`) and login (`/login`) pages, and handle form submissions with the `POST` method. 🔄
3. **Add User Validation**: Ensure that all fields are filled out and that usernames are unique. You don’t want multiple users with the same username, right? 🚫👥
4. **Greet the User**: Once the user logs in, display a personal message that makes them feel at home. **"Hello, [Name]!"** is perfect for a warm welcome! 🤗

## ⚠️ Remember:

- **Validation** is key! Make sure users provide all necessary details, and handle incorrect logins gracefully (e.g., "Incorrect username or password, please try again.").
- Keep your **database connection secure** and avoid hardcoding sensitive data. 🔒

Are you ready to take on this challenge? Let’s go! 🚀🌟

<img id="image" src="assets/day84_3.png" alt="day84 image" width="800">

<img id="image" src="assets/day84_4.png" alt="day84 image" width="700">

<img id="image" src="assets/day84_5.png" alt="day84 image" width="700">

---

## Solution (No Peeking!)

<details>
<summary>👀 Answer</summary>

### Python Code for Flask Signup/Login System with SQLite
```python
from flask import Flask, request, redirect, render_template
import sqlite3

app = Flask(__name__)

# Initialize the SQLite database
conn = sqlite3.connect('user_data.db', check_same_thread=False)
cursor = conn.cursor()

# Create users table if it does not exist
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT,
    name TEXT
)''')
conn.commit()

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        form = request.form
        username = form["username"]
        password = form["password"]
        name = form["name"]

        # Insert the user into the SQLite database if username is unique
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        existing_user = cursor.fetchone()

        if not existing_user:
            cursor.execute("INSERT INTO users (username, password, name) VALUES (?, ?, ?)", (username, password, name))
            conn.commit()
            return redirect('/login')
        else:
            return "Username already exists. Please choose another username."

    return render_template('register.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        form = request.form
        username = form["username"]
        password = form["password"]

        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()

        if user:
            return f'Hello, {user[2]}!'
        else:
            return "Invalid username or password. Please try again."

    return render_template('login.html')

@app.route('/change_password', methods=["GET", "POST"])
def change_password():
    if request.method == "POST":
        form = request.form
        username = form["username"]
        old_password = form["old_password"]
        new_password = form["new_password"]

        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, old_password))
        user = cursor.fetchone()

        if user:
            cursor.execute("UPDATE users SET password=? WHERE username=?", (new_password, username))
            conn.commit()
            return f'Password changed for {username}'
        else:
            return "Invalid username or old password. Password change failed."

    return render_template('change.html')

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81, debug=True)
```

### HTML Files
**register.html**
```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='styles/day84.css') }}">
    <title>Register</title>
</head>
<body>
    <h2>Register</h2>
    <form method="post" action="/register">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br>

        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required><br>

        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br>

        <button type="submit">Register</button>
    </form>
</body>
</html>
```

**login.html**
```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='styles/day84.css') }}">
    <title>Login</title>
</head>
<body>
    <h2>Login</h2>
    <form method="post" action="/login">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required><br>

        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br>

        <button type="submit">Login</button>
    </form>
</body>
</html>
```

**change.html**
```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='styles/day84.css') }}">
    <title>Change Password</title>
</head>
<body>
    <h2>Change Password</h2>
    <form method="post" action="/change_password">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required><br>

        <label for="old_password">Old Password:</label>
        <input type="password" id="old_password" name="old_password" required><br>

        <label for="new_password">New Password:</label>
        <input type="password" id="new_password" name="new_password" required><br>

        <button type="submit">Change Password</button>
    </form>
</body>
</html>
```

**day85.html**
```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='styles/day84.css') }}">
    <title>Home</title>
</head>
<body>
    <h2>Welcome to the Flask Signup/Login System!</h2>
    <a href="/register">Register</a> | <a href="/login">Login</a> | <a href="/change_password">Change Password</a>
</body>
</html>
```

**day84.css** (Optional styling for better visuals)
```python
body {
    font-family: 'Poppins', sans-serif;
    background-color: #fdf4f9;
    color: #4a4a4a;
    text-align: center;
    margin: 0;
    padding: 20px;
}

h2 {
    color: #e91e63;
    margin-bottom: 20px;
    font-weight: 600;
}

form {
    display: inline-block;
    background-color: #ffffff;
    padding: 40px;
    border-radius: 15px;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
    max-width: 400px;
    width: 100%;
    border: 2px solid #f8bbd0;
}

label {
    display: block;
    text-align: left;
    margin-top: 15px;
    margin-bottom: 5px;
    font-weight: 500;
    color: #d81b60;
}

input {
    margin-bottom: 20px;
    padding: 12px;
    width: calc(100% - 24px);
    box-sizing: border-box;
    border: 1px solid #d81b60;
    border-radius: 8px;
    background-color: #fce4ec;
    transition: border-color 0.3s;
}

input:focus {
    border-color: #e91e63;
    outline: none;
}

button {
    background-color: #e91e63;
    color: white;
    border: none;
    padding: 12px 24px;
    border-radius: 8px;
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.2s ease;
    font-weight: bold;
}

button:hover {
    background-color: #c2185b;
    transform: translateY(-2px);
}

button:active {
    transform: translateY(0);
}

a {
    color: #e91e63;
    text-decoration: none;
    font-weight: bold;
    margin: 10px;
}

a:hover {
    text-decoration: underline;
}

/* Additional styles for a polished look */
.container {
    max-width: 600px;
    margin: auto;
    padding: 20px;
}

footer {
    margin-top: 40px;
    font-size: 0.9em;
    color: #888;
}
```

</details>