# 🚀 Day 86 Challenge: Build Your Own Blog Engine! 📝

Hey there, code wizard! Ready to create something amazing? Today's challenge is all about building a **fully functional blog engine** – your personal corner of the web! 🌟

## 👉 **What You'll Build**
A simple but powerful blog where you can:
- **Log in** (only you can do this – you're the boss! 👑)
- **Add posts** (share your genius ideas ✨)
- **View posts** (both logged-in and as a guest 🕵️‍♀️)

---

## 🛠️ **Challenge Details**

### **1. Login Page 🔑**
- Create a login page that works for just one user: **you**!
- Add a password field to keep things secure (no need for fancy encryption here, just a basic check will do).

### **2. Logged-In View 🎉**
When you're logged in, you should see:
- ✅ A list of **existing posts** displayed however you like (cards, lists, or even a table!).
- 📝 A way to **add new posts**: include a text box and a submit button. When you submit, your post should be saved (e.g., in a local file or a simple database like SQLite).

### **3. Guest View 👀**
When you're **not logged in**, visitors will see:
- 📜 A feed of **your blog posts**, displayed in reverse chronological order (most recent first).
- 🔓 A 'login' button so you can hop back in and add more posts.

---

## 💡 **Example**
Imagine a cozy little blog:
1. **Login screen:** Enter your credentials to access your blogging tools. 🔐
2. **Blog dashboard:** See all your posts and add new ones with ease! ✍️
3. **Guest view:** Visitors can scroll through your posts but can't mess with your work. 🤫

---

## 🌟 **Bonus Fun Ideas**
- Add **timestamps** to your posts so you know when you wrote them. ⏰
- Let users **delete or edit posts** when logged in (keep it simple for now). 🗑️✏️
- Customize the design with some cool colors or CSS animations. 🎨✨
- Add a logout button for a clean exit. 🚪
- Save your posts in an **SQLite database** or as a **JSON file** to make it more robust.

---

## 🔥 **Why This Challenge is Awesome?**
- You’ll practice **frontend and backend integration** in VS Code.
- You'll explore **user authentication**.
- You'll learn to manage data using local storage solutions (like SQLite or files).
- Plus, you’ll have your very own blog at the end – how cool is that?! 💻✨

When you're done, don’t forget to share your masterpiece with 🍪 in the comments! Let's see those blogs come to life! 🚀


<img id="image" src="assets/day86_1.png" alt="day86 image" width="690">

<img id="image" src="assets/day86_2.png" alt="day86 image" width="690">

<img id="image" src="assets/day86_3.png" alt="day86 image" width="690">

<img id="image" src="assets/day86_4.png" alt="day86 image" width="690">

<img id="image" src="assets/day86_5.png" alt="day86 image" width="690">


---

## Solution (No Peeking!)


<details>
<summary>👀 Answer</summary>

👉 **day86.py**

```python
from flask import Flask, request, redirect, render_template, session, flash
from dotenv import load_dotenv
import sqlite3
import os

# Initialize the app
app = Flask(__name__)

# Load environment variables from .env file
load_dotenv(dotenv_path='python-dotenv/.env')

# Set the secret key for sessions from environment variable or explicitly
app.config['SECRET_KEY'] = os.getenv('SESSION_SECRET_KEY', 'fallback-secret-key')

# Database setup
DATABASE = "blog.db"

def init_db():
    """Initialize the database with tables for users and posts."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    # Create the users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    """)
    # Create the posts table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    # Insert a default user
    cursor.execute("""
        INSERT OR IGNORE INTO users (username, password) 
        VALUES ('alisoons', 'alise123')
    """)
    conn.commit()
    conn.close()

# Initialize the database
init_db()

def query_db(query, args=(), one=False, commit=False):
    """Helper function to query the database."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(query, args)
    if commit:
        conn.commit()
    rv = cursor.fetchall()
    conn.close()
    return (rv[0] if rv else None) if one else rv

def create_user(username, password):
    """Helper function to create a new user."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = query_db("SELECT * FROM users WHERE username = ?", (username,), one=True)
        print("Login attempt for:", username)
        print("User from DB:", user)

        if user:
            if user[2] == password:  # Ensure password matches
                session['username'] = username
                print("Session set for:", session['username'])
                flash("Login successful.", "success")
                return redirect('/feed')
            else:
                flash("Invalid password. Please try again.", "error")
        else:
            flash("User does not exist. Please create an account.", "error")
    
    return render_template('login.html')

@app.route('/feed', methods=["GET", "POST"])
def feed():
    if 'username' in session:
        if request.method == "POST":
            new_title = request.form["title"]
            new_content = request.form["content"]
            query_db("INSERT INTO posts (title, content) VALUES (?, ?)", (new_title, new_content), commit=True)
            flash("New blog entry added.", "success")
        
        posts = query_db("SELECT title, content, timestamp FROM posts ORDER BY timestamp DESC")
        return render_template('feed_logged_in.html', posts=posts)
    else:
        posts = query_db("SELECT title, content, timestamp FROM posts ORDER BY timestamp DESC")
        return render_template('feed_not_logged_in.html', posts=posts)

@app.route('/logout')
def logout():
    session.pop('username', None)  # Clear the session
    flash("Logout successful.", "success")
    return redirect('/login')  # Redirect to the /login route

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)
```

👉 **login.html**

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles/day86.css') }}" type="text/css">
</head>
<body>
    <div class="container">
        <h1>Login</h1>
        
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                <div class="flash-messages">
                    {% for category, message in messages %}
                        <p class="{{ category }}">{{ message }}</p>
                    {% endfor %}
                </div>
            {% endif %}
        {% endwith %}
        
        <form method="POST">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required>
            
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required>
            
            <input type="submit" value="Login">
        </form>
    </div>
</body>
</html>
```

👉 **feed_logged_in.html**

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Blog</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles/day86.css') }}" type="text/css">
</head>
<body>
    <div class="container">
        <h1>Welcome to Your Blog!</h1>
        
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                <div class="flash-messages">
                    {% for category, message in messages %}
                        <p class="{{ category }}">{{ message }}</p>
                    {% endfor %}
                </div>
            {% endif %}
        {% endwith %}
        
        <h2>Your Posts</h2>
        {% if posts %}
            <ul>
                {% for post in posts %}
                    <li>
                        <h3>{{ post[0] }}</h3>
                        <p>{{ post[1] }}</p>
                        <small>Posted on: {{ post[2] }}</small>
                    </li>
                {% endfor %}
            </ul>
        {% else %}
            <p>No posts yet. Start by adding a new post below!</p>
        {% endif %}
        
        <h2>Add a New Post</h2>
        <form method="POST">
            <label for="title">Title:</label>
            <input type="text" id="title" name="title" required>
            <label for="content">Content:</label>
            <textarea id="content" name="content" rows="4" required></textarea>
            <input type="submit" value="Add Post">
        </form>
        
        <a href="/logout" class="logout-button">Logout</a>
    </div>
</body>
</html>
```

👉 **feed_not_logged_in.html**

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Public Blog</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles/day86.css') }}" type="text/css">
</head>
<body>
    <div class="container">
        <h1>Blog Entries</h1>
        
        {% if posts %}
            <ul>
                {% for post in posts %}
                    <li>
                        <h3>{{ post[0] }}</h3>
                        <p>{{ post[1] }}</p>
                        <small>Posted on: {{ post[2] }}</small>
                    </li>
                {% endfor %}
            </ul>
        {% else %}
            <p>No blog posts available. Check back later or <a href="/login">login</a> to add the first post!</p>
        {% endif %}
        
        <a href="/login" class="login-button">Login to Add Posts</a>
    </div>
</body>
</html>
```

👉 **day86.css**

```python
/* Reset and Base Styles */
body {
    margin: 0;
    padding: 0;
    font-family: "Poppins", sans-serif;
    background-color: #fef8f8;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh; /* Full-page height */
}

/* Center Content */
.container {
    text-align: center;
    padding: 20px;
    max-width: 400px;
    width: 90%; /* For responsiveness */
    margin: auto;
    background-color: #fff;
    border-radius: 12px;
    box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.1);
    border: 2px solid #f9c3c8;
}

/* Header Styles */
h1 {
    color: #d63384;
    font-size: 2em;
    font-weight: bold;
    margin-bottom: 20px;
}

/* Flash Messages */
.flash-messages {
    background-color: #fff8e6;
    border: 1px solid #f5c6cb;
    color: #e74c3c;
    padding: 10px;
    border-radius: 8px;
    margin-bottom: 20px;
    text-align: left;
}

/* Form Styles */
form {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
}

label {
    margin-bottom: 5px;
    font-weight: bold;
    color: #d63384;
    text-align: left;
    width: 100%;
}

input[type="text"],
input[type="password"] {
    width: 90%; /* Ensure reasonable width */
    max-width: 300px; /* Limit maximum size */
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 8px;
    font-size: 1em;
    outline: none;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

input[type="submit"] {
    background-color: #6f42c1;
    color: #fff;
    border: none;
    border-radius: 8px;
    padding: 10px 20px;
    cursor: pointer;
    transition: background-color 0.3s ease-in-out, transform 0.2s;
    font-size: 1em;
    font-weight: bold;
}

input[type="submit"]:hover {
    background-color: #563d7c;
    transform: scale(1.05);
}

/* Responsive Design */
@media (max-width: 768px) {
    .container {
        padding: 15px;
        max-width: 90%;
    }

    input[type="text"], input[type="password"] {
        max-width: 100%;
    }

    input[type="submit"] {
        font-size: 0.9em;
        padding: 8px 15px;
    }

    h1 {
        font-size: 1.8em;
    }
}

ul li small {
    display: block;
    font-size: 0.8em;
    color: #999;
    margin-top: 5px;
}
```

</details>

