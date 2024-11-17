# Day 87: Authentication 🚀🔐

Efficient code often has the drawback of being hard to understand at first. It’s often dense, with many things happening in just a single line. 🧩  

That’s why teachers often choose to take “the long way around” when explaining new concepts. It’s all about building a strong foundation so you can understand what’s happening behind the scenes. And trust us, that knowledge is priceless. 💎

With all that in mind, don’t be mad at us when we say this: there *is* an easier way to create a login system than manually managing sessions. But the work you’ve done over the past few days? Totally worth it. You’ve built a rock-solid understanding of the inner workings of authentication, which will help you so much down the road. 💪✨

---

### **Authentication in VS Code** 💻🔑

In VS Code, you have the freedom to set up your own authentication system—no pre-built shortcuts here. And while that might sound like extra work, it’s actually a great opportunity to learn real-world implementation. 🌍

Here’s how authentication works in your project:  
1. You’ve set up **sessions** to track whether a user is logged in or not.  
2. When a user logs in, their data (like their username) is stored securely, making their experience seamless across multiple pages.  
3. And when they log out? Everything is cleared, keeping their information safe. 🛡️

---

### **Accessing User Information** 💻🔑

In VS Code, you can access user-related information dynamically using the `request` object from Flask. This data is often passed as part of the request headers. By extracting and using it, you can personalize responses for each user. 🌍✨

Here’s an example of how to fetch and display a username from the headers:

### **Code Example**

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    # Simulate retrieving a username from request headers
    username = request.headers.get("X-User-Name", "Guest")  # Default to "Guest" if header is missing
    return f"Hello, {username}!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)
```

---

### How This Works
1. `request.headers`:
This is a dictionary-like object that contains all the headers sent with the HTTP request.

2. `X-User-Name`:
This is a custom header that your client (browser or API) sends. If it’s missing, the code defaults to `Guest` to avoid errors.

3. `Dynamic Response`:
The app uses the username to generate a personalized response, enhancing the user experience.

---

### **Why This Matters** 🤔✨

Understanding how sessions and authentication work behind the scenes gives you a competitive edge. Instead of just clicking “enable authentication” in some tool, you now know how the entire process works. From securely storing session data to managing logins and logouts, you’ve tackled one of the most important aspects of web development. 💼🔥

Sure, it may have been a bit tricky at times (looking at you, sessions 😅), but that’s part of the learning journey. Every struggle makes you a better developer, and trust us—you’ve got this! 💪🌟

---

## Common Errors
 
 First, delete any other code in your `day87` files. Copy each code snippet below into `day87` files by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.


### Headers Up!

👉 What's the problem here?

 ```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    username = request.header.get("X-User-Name")
    return f"Hello, {username}!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)
```

<details>
<summary>👀 Answer</summary>

- This is a mistake I make all the time, it's `headers` not `header`. This will throw an 'Internal Server Error'.
- Default to `Guest` should be added or you will `None` 


```python
username = request.headers.get("X-User-Name", "Guest")
```

</details>

---

# 👉 Day 87 Challenge 🚀

Today’s challenge is to enhance and streamline your **blog engine login system** from yesterday. By the end of this challenge, your code should be cleaner and more efficient. ✂️✨

### Your program should:

1. 🔄 **Change the Login Button**:  
   Update the login button functionality to forward the user directly to the **edit page** after logging in.

2. ✅ **Validate the User**:  
   On the edit page, verify that the user is authorized (it’s you!). If the user isn’t you, redirect them back to the **main page**—no unauthorized edits allowed! 🛡️

This challenge is all about making your application smarter, safer, and simpler. Let’s see how clean and efficient you can make your code! 💪

<img id="image" src="assets/day87_1.png" alt="day87 image" width="690">

<img id="image" src="assets/day87_2.png" alt="day87 image" width="690">

<img id="image" src="assets/day87_3.png" alt="day87 image" width="690">

<img id="image" src="assets/day87_5.png" alt="day87 image" width="690">

---

## Solution (No Peeking!)


<details>
<summary>👀 Answer</summary>

👉 **day87.py**

```python
from flask import Flask, request, redirect, render_template, flash, session
from dotenv import load_dotenv
import sqlite3
import os

app = Flask(__name__)

# Load environment variables and configure the app
load_dotenv(dotenv_path='python-dotenv/.env')
app.config['SECRET_KEY'] = os.getenv('SESSION_SECRET_KEY', 'fallback-secret-key')

DATABASE = "blog.db"

def init_db():
    """Set up the database with required tables and a default user."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        cursor.execute("""
            INSERT OR IGNORE INTO users (username, password) 
            VALUES ('alisoons', 'alise123')
        """)
        conn.commit()

init_db()

def query_db(query, args=(), one=False, commit=False):
    """Execute a database query and return results."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(query, args)
        if commit:
            conn.commit()
        results = cursor.fetchall()
        return (results[0] if results else None) if one else results

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = query_db("SELECT * FROM users WHERE username = ? AND password = ?", (username, password), one=True)
        if user:
            session['username'] = username
            flash("Login successful!", "success")
            return redirect('/edit')
        flash("Invalid username or password. Redirecting to feed.", "error")
        return redirect('/feed')
    return render_template('login.html')

@app.route('/logout')
def logout():
    username = session.pop('username', None)
    flash(f"User '{username}' has been logged out successfully." if username else "No user is currently logged in.", "info")
    return redirect('/login')

@app.route('/edit', methods=["GET", "POST"])
def edit():
    username = session.get("username")
    if not username:
        flash("Unauthorized access. Redirecting to the main page.", "error")
        return redirect('/feed')
    
    if request.method == "POST":
        query_db("INSERT INTO posts (title, content) VALUES (?, ?)", 
                 (request.form["title"], request.form["content"]), commit=True)
        flash("New blog entry added.", "success")
    
    posts = query_db("SELECT title, content, timestamp FROM posts ORDER BY timestamp DESC")
    return render_template('edit.html', posts=posts)

@app.route('/feed')
def feed():
    posts = query_db("SELECT title, content, timestamp FROM posts ORDER BY timestamp DESC")
    return render_template('feed.html', posts=posts)

@app.after_request
def add_global_user_header(response):
    if 'username' in session:
        response.headers['X-User-Name'] = session['username']
    return response

if __name__ == "__main__":
    app.run(debug=True)
```

👉 **login.html**

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles/day87.css') }}" type="text/css">
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

👉 **feed.html**

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog Feed</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles/day87.css') }}" type="text/css">
</head>
<body>
    <div class="container">
        <h1>Blog Feed</h1>

        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                <div class="flash-messages">
                    {% for category, message in messages %}
                        <p class="{{ category }}">{{ message }}</p>
                    {% endfor %}
                </div>
            {% endif %}
        {% endwith %}

        {% if posts %}
            <ul>
                {% for post in posts %}
                    <li>
                        <h2>{{ post[0] }}</h2>
                        <p>{{ post[1] }}</p>
                        <small>Posted on: {{ post[2] }}</small>
                    </li>
                {% endfor %}
            </ul>
        {% else %}
            <p>No blog posts available yet. Check back later!</p>
        {% endif %}

        <div class="navigation">
            <a href="/login">Login to Add or Edit Posts</a>
        </div>
    </div>
</body>
</html>
```

👉 **edit.html**

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit Posts</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles/day87.css') }}" type="text/css">
</head>
<body>
    <div class="container">
        <h1>Edit Blog Posts</h1>

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
            <label for="title">Title:</label>
            <input type="text" id="title" name="title" required>
            
            <label for="content">Content:</label>
            <textarea id="content" name="content" rows="4" required></textarea>
            
            <input type="submit" value="Add Post">
        </form>

        {% if posts %}
            <h2>Existing Posts</h2>
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
            <p>No posts available. Add your first post above!</p>
        {% endif %}

        <!-- Logout Button -->
        <form action="/logout" method="GET">
            <button type="submit">Logout</button>
        </form>
    </div>
</body>
</html>
```

👉 **day87.css**

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
    max-width: 600px;
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
    font-size: 2.5em;
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
input[type="password"],
textarea {
    width: 90%;
    max-width: 400px;
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 8px;
    font-size: 1em;
    outline: none;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

textarea {
    resize: none;
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

    input[type="text"], input[type="password"], textarea {
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

.navigation a {
    display: inline-block;
    margin-top: 20px;
    padding: 10px 20px;
    background-color: #6f42c1;
    color: white;
    text-decoration: none;
    border-radius: 8px;
    font-weight: bold;
    transition: background-color 0.3s ease-in-out, transform 0.2s;
}

.navigation a:hover {
    background-color: #563d7c;
    transform: scale(1.05);
}
```

</details>


# **Understanding Sessions and Headers in Flask** 🚀

### 👉 This is for you to understand solution

This documentation explains the concepts of **sessions** and **headers** using the provided Flask application. The focus is on helping beginners understand **why** and **how** these mechanisms are used, along with a step-by-step breakdown of the application.

---

## **What are Sessions?** 🛡️

A **session** is a way to store information about a user across multiple requests. Flask sessions use cookies to save data securely, such as a user’s login status, while keeping the data on the server.

### **Why Use Sessions?**

- **Persist Data Across Requests**: Sessions ensure user-specific data (like login information) persists between requests.
- **Security**: Session data is stored on the server, so sensitive information (like passwords) isn’t exposed to the client.
- **User Identification**: You can track whether a user is logged in, what pages they’ve accessed, and more.

---

## **What are Headers?** 📩

**Headers** are metadata sent with every HTTP request and response. They carry information like content type, cookies, and custom data (e.g., usernames).

### **Why Use Headers?**

- **Custom Metadata**: Headers allow the server to send additional data (like the logged-in username) with every response.
- **Debugging**: Developers can use custom headers to check server-side behavior (e.g., ensuring a user is logged in).
- **Stateless Communication**: Headers complement sessions by providing information about the current user.

---

## **Code Walkthrough**

### **1. Login System with Sessions**

#### **Login Route: `/login`**
- **What It Does**:
  - Validates the username and password against the database.
  - If valid:
    - Stores the `username` in the session.
    - Redirects the user to the `/edit` page.
  - If invalid:
    - Redirects to `/feed` with an error message.

- **Why Use Sessions?**
  - After logging in, the user’s session stores their `username`, allowing the server to identify them without requiring them to log in repeatedly.

```python
session['username'] = username  # Store the username in the session
```

#### Example Flow:
1. User submits valid credentials:
   - Session stores the username.
   - User is redirected to `/edit`.

2. User submits invalid credentials:
   - No session is created.
   - User is redirected to `/feed` with an error flash message.

---

### **2. Securing Pages with Sessions**

#### **Edit Route: `/edit`**
- **What It Does**:
  - Checks if the user is logged in (via session).
  - If logged in:
    - Displays the edit page.
    - Allows adding new blog posts.
  - If not logged in:
    - Redirects to `/feed` with an error message.

- **Why Use Sessions?**
  - Sessions ensure only authorized users can access restricted pages like `/edit`.

```python
username = session.get("username")
if not username:
    flash("Unauthorized access. Redirecting to the main page.", "error")
    return redirect('/feed')
```

#### Example Flow:
1. User accesses `/edit` while logged in:
   - Session is valid; page loads successfully.
2. User accesses `/edit` without logging in:
   - Session is invalid; user is redirected to `/feed`.

---

### **3. Logging Out**

#### **Logout Route: `/logout`**
- **What It Does**:
  - Clears the session (removing the `username`).
  - Redirects the user to the `/login` page.

- **Why Use Sessions?**
  - Clearing the session ensures the user’s data is no longer available, preventing unauthorized access.

```python
session.pop('username', None)  # Remove username from session
```

#### Example Flow:
1. User logs out:
   - Session is cleared.
   - User is redirected to `/login`.

---

### **4. Sending Custom Headers**

#### **Adding `X-User-Name` Header**
- **What It Does**:
  - Adds a custom header (`X-User-Name`) to all responses for logged-in users.
  - If no user is logged in, the header is not included.

- **Why Use Headers?**
  - Provides a convenient way to debug or verify the logged-in user during development.

```python
@app.after_request
def add_global_user_header(response):
    username = session.get('username')
    if username:
        response.headers['X-User-Name'] = username
    return response
```

#### Example Flow:
1. User is logged in:
   - All server responses include `X-User-Name: <username>` in the headers.
2. User is not logged in:
   - The header is omitted.

---

## **How the Routes Work Together**

### **Open Routes**
- `/login`: Allows users to log in.
- `/feed`: Displays all public blog posts (no login required).

### **Restricted Routes**
- `/edit`: Accessible only to logged-in users.
- `/logout`: Logs out the current user and clears the session.

---

## **Test Scenarios**

1. **Login with Valid Credentials**:
   - Expected: Redirect to `/edit`, session stores the username.

2. **Login with Invalid Credentials**:
   - Expected: Redirect to `/feed` with an error message, no session created.

3. **Access `/edit` Without Logging In**:
   - Expected: Redirect to `/feed` with an error message.

4. **Logout**:
   - Expected: Session cleared, redirected to `/login`.

5. **Check Headers**:
   - Logged-in user: `X-User-Name` header is present.
   - Not logged in: `X-User-Name` header is absent.

---

## **Why This Approach is Beginner-Friendly**

1. **Sessions Simplified**:
   - Sessions are used only when needed, keeping the implementation straightforward.

2. **Headers for Debugging**:
   - Custom headers make it easy to understand server behavior without altering the application logic.

3. **Error Handling**:
   - Flash messages provide clear feedback for both valid and invalid actions.

4. **Clean Routing**:
   - Routes are organized, with restricted routes (like `/edit`) protected by session checks.
