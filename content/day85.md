# Day 85: HTTP & Sessions 🚀

One of the main protocols (rules that govern how computers communicate) on the web is called **HTTP**.

**HTTP** is what we call a **stateless protocol**. This means it doesn't "remember" things. 🐠

It's kind of like having a conversation with a goldfish. You can ask a question and get a reply, but when you ask a follow-up question, the original has already been forgotten — as has who you are and what you were talking about.

So if HTTP is stateless, how does a news site remember to give you the weather for your hometown 🌦️, or how does your favorite online shop remind you when it's time to reorder your favorite item 📦? And how do you keep track of your #100days success streak? 💪

The answer is...

### Sessions 🗂️

**Sessions** are a way of storing data on your computer that allows a website to keep track of previous "conversations" and questions you've asked. By using sessions, we can store user information to access later. This is super useful when creating things like login systems or personalized user experiences. 🖥️✨

By default, a session is active until you close your browser, but we can tweak that to last longer if needed.

👉 Let's get sessions rolling by importing all the classics! We'll start by **importing `session`** and **adding a key to our app definition**. The key is used to encrypt the data stored in the session, ensuring that the user cannot tamper with it.

The key should be something long, hard to guess, and most importantly, **not** stored directly in the source code. Instead, you can use a more secure approach like storing it in an environment variable.

My key is just a random string, but you can make yours whatever you want. Here's how you can do it in VSCode:

1. **Create an environment variable** to store your key securely. You can add this to your `.env` file, for example:
   ```python
   SESSION_SECRET_KEY=your_very_secret_key_here
   ```

2. **Load the key in your application** by using a library like `python-dotenv` to access the value from your environment.

3. **Add the session key** to your code like so:
   ```python
   from flask import Flask, session, request, redirect
   from dotenv import load_dotenv
   import os

   load_dotenv()

   app = Flask(__name__)
   app.secret_key = os.getenv('SESSION_SECRET_KEY')

   @app.route('/')
   def index():
       return 'Hello from Flask!'

   app.run(host='0.0.0.0', port=81)
   ```

### Adding User Input with Flask 🚀

👉 Let's expand on what we learned about sessions by getting some user input! This is a great way to understand how we can make web applications more interactive and user-friendly. We can do this by adding an HTML form to gather information from users.

Here's how you can create a form and import it into your Flask app. This way, we can collect data like a user's name and keep it within a session. This is especially useful for creating personalized experiences!

### HTML Form for User Input ✍️

First, we'll create a simple HTML form that allows users to input their name:

```python
<form method="post" action="/setName">
  <p>Name: <input type="text" name="name"></p>
  <button type="submit">Submit</button>
</form>
```

Save this form in a file called `form.html`. The form will send the user's name to the `/setName` endpoint, which we will define in our Flask app.

### `greet.html` Template 📝

We also need a template to greet the user after they submit their name. Create a new file called `greet.html` inside the `templates` directory:

```python
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Greeting Page</title>
</head>
<body>
    <h1>Hello, {{ name }}! Welcome to our Flask app!</h1>
</body>
</html>
```

This template will display a personalized greeting using the name provided by the user.

### Updating the Flask App to Use the Form and Template 📝

Here's the updated code to import the form and handle the user input:

```python
from flask import Flask, session, request, redirect, render_template
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SESSION_SECRET_KEY')

# Import the form page
@app.route('/')
def index():
    return render_template('form.html')

# Set the user's name in the session
@app.route('/setName', methods=['POST'])
def set_name():
    session['name'] = request.form['name']
    return redirect('/greet')

# Greet the user by name
@app.route('/greet')
def greet():
    name = session.get('name', 'Guest')
    return render_template('greet.html', name=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
```

### Explanation 📚

1. **HTML Form**: We created a simple HTML form that sends the user's name to the `/setName` endpoint.
2. **`greet.html` Template**: We created a template to display a personalized greeting using the name stored in the session.
3. **`/setName` Endpoint**: This route takes the user input from the form and saves it in the session.
4. **`/greet` Endpoint**: This route greets the user using the stored name from the session. If no name is set, it defaults to "Guest".

---

## Adding Reset Functionality for Sessions 🍪

We've learned how to create and store session data, but sometimes we need a way to delete that data too! Just like cookies in your browser, sessions can store user data temporarily, and we need a way to clear that information when necessary.

Cookies are small pieces of data that websites store on a user's computer. They are often used to remember user preferences, login information, or other small pieces of data that help improve the user experience. Cookies can be either **session cookies** or **persistent cookies**:

- **Session Cookies**: These are temporary cookies that are deleted once the user closes their browser. Sessions in Flask are implemented using session cookies by default, which means the data is only available while the user's browser is open.
- **Persistent Cookies**: These cookies remain on the user's computer even after the browser is closed. They are used to remember information for a longer time, such as login credentials or user settings.

Sessions in Flask are effectively stored using cookies. The server keeps a reference to the user's data using a session ID, and that ID is stored in a cookie on the user's computer. This allows the server to identify the user and retrieve the stored data, providing a consistent experience across different pages of the web app.

### Updated HTML Form with Reset Button ✍️

First, let's update the `form.html` file to include a button that allows users to reset their session:

```python
<form method="post" action="/setName">
  <p>Name: <input type="text" name="name"></p>
  <button type="submit">Submit</button>
  <button type="button" onclick="location.href='/reset'">Reset</button>
</form>
```

This **reset button** will forward the user to the `/reset` endpoint, where we will clear the session data.

### Creating the Reset Route in Flask 📝

Next, we'll add the `/reset` route to our Flask app. This route will clear the session using `session.clear()` and then redirect the user back to the main page.

Here's the updated Flask code:

```python
from flask import Flask, session, request, redirect, render_template
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='python-dotenv/.env')

app = Flask(__name__)
app.secret_key = os.getenv('SESSION_SECRET_KEY')

# Import the form page
@app.route('/')
def index():
    return render_template('form.html')

# Set the user's name in the session
@app.route('/setName', methods=['POST'])
def set_name():
    session['name'] = request.form['name']
    return redirect('/greet')

# Greet the user by name
@app.route('/greet')
def greet():
    name = session.get('name', 'Guest')
    return render_template('greet.html', name=name)

# Reset the session
@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
```

### Explanation 📚

1. **HTML Form**: We've updated `form.html` to include a reset button that forwards the user to the `/reset` route.
2. **`/reset` Endpoint**: This route clears all the data stored in the session using `session.clear()` and then redirects back to the main page (`/`).

This functionality is useful when you want to give users the ability to start over, especially when dealing with forms or personalized data. With the new reset button, users can clear their session data effortlessly, making your web app more user-friendly! 😊

### Cookies and Sessions 🍪

- **Cookies** are used by web applications to store small pieces of data on the client side.
- In Flask, sessions are implemented using cookies, meaning the session data is stored temporarily on the user's computer as a cookie.
- When we create or update a session in Flask, a cookie containing the session ID is created on the user's computer. The actual session data is stored server-side, and Flask uses the session ID to match the user to their data.
- The **secret key** that we set in our application (`app.secret_key`) is used to sign the session cookie, ensuring that the data cannot be tampered with by the user.

### Testing the Reset Functionality 🔄

👉 To test if everything is working as expected, make sure to **open the site in a separate tab** and try submitting and then resetting your data. You should see that the session data is successfully cleared, and you're redirected back to the form page.

---

## Common Errors
 
 First, delete any other code in your `day85` files. Copy each code snippet below into `day85` files by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.


### SSSSHHHHHHHHH

👉 What's the problem here?

 ```python
from flask import Flask, request, redirect, session, render_template
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='python-dotenv/.env')

app = Flask(__name__)
app.secret_key = "secret123"

@app.route('/')
def index():
    myName = session.get("myName", "Guest")
    return render_template('form.html', myName=myName)

@app.route("/setName", methods=["POST"])
def setName():
    name = request.form.get("name")
    if name:
        session["myName"] = name
    return redirect("/")

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)
```

<details>
<summary>👀 Answer</summary>

Yep, you got it! My secret key was hard coded into my source code. Anyone with access to the code can now use the key to decrypt the contents of the session. Nice!

```python
app.secret_key = os.getenv('SESSION_SECRET_KEY')
```

</details>

---

### Informal

👉 What's the problem here?

 ```python
from flask import Flask, session, request, redirect, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/setName', methods=['POST'])
def set_name():
    session['name'] = request.form['name']
    return redirect('/greet')

@app.route('/greet')
def greet():
    name = session.get('name', 'Guest')
    return render_template('greet.html', name=name)

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
```

<details>
<summary>👀 Answer</summary>

In this one, I've forgotten to set a secret key entirely. This will throw an **internal server error**.

</details>

---

## Fix My Code

👉 Try and fix this code which is *full* of errors.

First, delete any other code in your `day85` files. Copy each code snippet below into `day85` files by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.


```python
from flask import Flask, request, redirect, session, render_template
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='python-dotenv/.env')

app = Flask(__name__)
app.secret_key = "secret123"

app.route('/')
def index():
   myName = session.get("myName", "Guest")
   return render_template('form.html', myName=myName)

@app.route("/setName", methods=["POST"])
def setName():
   name = request.form.get("name")
   if name: 
       session["myName"] = name
   return redirect("/")

@app.route("/reset")
def reset():
   session.clear()
   return redirect("/")

if __name__ == "__main__": 
   app.run(host='0.0.0.0', port=81)
```

<details>
<summary>👀 Answer</summary>

Again, my secret key is hard coded. But did you spot the other error?
I forgot the `@` before the `app.route`.

</details>

---

# 👉 Day 85 Challenge: Extending Your Login System 🚀

Today's challenge is all about enhancing your login system by leveraging **sessions** to create a more secure and user-friendly experience. The goal is to use sessions to store login information and enforce access control across multiple pages in your web application.

### Challenge Objectives:

1. **Store Login Information in Sessions** 🗂️
   - Use the `session` object to store login information. This means storing user data, such as the username, in the session so that the server can recognize whether a user is logged in.

2. **Check Login Status on Every Page** 🔒
   - Add a check to every page of your app to ensure that the session data contains a valid username.
   - If a user attempts to visit a page without being logged in, they should be **redirected to the login page**.

3. **Logout Button Implementation** ⏏️
   - Create a **logout button** that allows users to clear the session data and log out of the application.
   - When the user clicks the logout button, they should be **redirected back to the login page**.

4. **Restrict Access to Protected Pages** 🚫
   - Ensure that users can only access protected pages (e.g., dashboard, profile, settings) if they are logged in.
   - The only page that should be accessible without logging in is the **login page** itself.

#### Example Flow:
1. The user visits the **login page** and logs in by entering their username and password.
2. The user's login information is stored in the **session** and they are redirected to the **home page**.
3. Any time the user visits a page, the application checks if their session is valid:
   - **If logged in**: They can continue to access protected content.
   - **If not logged in**: They are kicked back to the login page.
4. The user can click a **logout button**, which will clear the session and redirect them back to the **login page**.

#### Tips for Success 💡
- Use **Flask sessions** to handle login state effectively and securely.
- Remember to **set the session key** properly so the data is encrypted.
- Think about **user experience**: make sure that login redirects are smooth and that unauthorized access is handled gracefully.
- Add messages to inform users when they have been logged out or when they need to log in.

Good luck, and have fun extending your login system! This challenge will help you create a more robust and user-friendly application, reinforcing the importance of authentication and access control in web development. 🔐✨

<img id="image" src="assets/day85_1.png" alt="day85 image" width="800">

<img id="image" src="assets/day85_2.png" alt="day85 image" width="700">

<img id="image" src="assets/day85_3.png" alt="day85 image" width="700">

<img id="image" src="assets/day85_4.png" alt="day85 image" width="700">

---

## Solution (No Peeking!)

<details>
<summary>👀 Answer</summary>

### day85.py
```python
from flask import Flask, request, redirect, render_template, session, flash
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv(dotenv_path='python-dotenv/.env')

app = Flask(__name__)

# Set the secret key for sessions from environment variable or set it explicitly
app.config['SESSION_SECRET_KEY'] = os.getenv('SESSION_SECRET_KEY')

# Temporary dictionary for user storage (instead of db)
users = {}

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        form = request.form
        username = form["username"]
        password = form["password"]
        name = form["name"]

        if username not in users:
            users[username] = {"password": password, "name": name}
            flash("Registration successful. Please log in.", "success")
            return redirect('/login')
        else:
            flash("Username already exists. Please choose another username.", "error")

    return render_template('register.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        form = request.form
        username = form["username"]
        password = form["password"]

        if username in users and users[username]["password"] == password:
            session['username'] = username  # Store username in the session
            flash("Login successful.", "success")
            return redirect('/dashboard')
        else:
            flash("Invalid username or password. Please try again.", "error")

    return render_template('login.html')

@app.route('/change_password', methods=["GET", "POST"])
def change_password():
    if 'username' not in session:
        return redirect('/login')

    if request.method == "POST":
        form = request.form
        username = session['username']
        old_password = form["old_password"]
        new_password = form["new_password"]

        if users[username]["password"] == old_password:
            users[username]["password"] = new_password
            flash("Password changed successfully.", "success")
        else:
            flash("Invalid old password. Password change failed.", "error")

    return render_template('change.html')

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect('/login')

    return f'Hello, {users[session["username"]]["name"]}! <a href="/logout">Logout</a>'

@app.route('/logout')
def logout():
    session.pop('username', None)  # Clear the session
    flash("Logout successful.", "success")
    return redirect('/login')

@app.route('/')
def index():
    if 'username' not in session:
        return redirect('/login')

    return render_template("day85.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
```

### HTML Files
**register.html**
```python
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>Register</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles/day85.css') }}" type="text/css">
</head>
<body>
    <header>
        <h1>Register</h1>
    </header>
    <main>
        <form method="POST" action="/register">
            <p>Name: <input type="text" name="name" required></p>
            <p>Username: <input type="text" name="username" required></p>
            <p>Password: <input type="password" name="password" required></p>
            <button type="submit">Register</button>
        </form>
        <p>Already have an account? <a href="/login">Login here</a></p>
    </main>
</body>
</html>
```

**login.html**
```python
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>Login</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles/day85.css') }}" type="text/css">
</head>
<body>
    <header>
        <h1>Login</h1>
    </header>
    <main>
        <form method="POST" action="/login">
            <p>Username: <input type="text" name="username" required></p>
            <p>Password: <input type="password" name="password" required></p>
            <button type="submit">Login</button>
        </form>
        <p>Don't have an account? <a href="/register">Register here</a></p>
    </main>
</body>
</html>
```

**change.html**
```python
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>Change Password</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles/day85.css') }}" type="text/css">
</head>
<body>
    <header>
        <h1>Change Password</h1>
    </header>
    <main>
        <form method="POST" action="/change_password">
            <p>Username: <input type="text" name="username" required></p>
            <p>Old Password: <input type="password" name="old_password" required></p>
            <p>New Password: <input type="password" name="new_password" required></p>
            <button type="submit">Change Password</button>
        </form>
        <p><a href="/dashboard">Go back to Dashboard</a></p>
    </main>
</body>
</html>
```

**day85.html**
```python
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>My Blog</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles/day85.css') }}" type="text/css">
</head>
<body>
    <header>
        <h1>Welcome to My Blog</h1>
    </header>
    <main>
        <div class="buttons">
            <a href="/register" class="button">Register</a>
            <a href="/login" class="button">Login</a>
        </div>
    </main>
</body>
</html>
```

**day85.css** (Optional styling for better visuals)
```python
/* Reset CSS */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* General styling */
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(to right, #e0eafc, #cfdef3);
    color: #333;
    margin: 0;
    padding: 0;
    line-height: 1.6;
}

header {
    background-color: #4a90e2;
    color: #fff;
    padding: 30px;
    text-align: center;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

header h1 {
    font-size: 40px;
    margin-bottom: 10px;
}

main {
    padding: 40px;
    text-align: center;
}

.buttons {
    margin-top: 30px;
}

.button {
    display: inline-block;
    padding: 15px 30px;
    margin: 15px;
    background-color: #28a745;
    color: #fff;
    font-size: 20px;
    text-decoration: none;
    border-radius: 50px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    transition: all 0.3s ease;
}

.button:hover {
    background-color: #218838;
    transform: translateY(-3px);
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
}

footer {
    background-color: #4a90e2;
    color: #fff;
    text-align: center;
    padding: 20px;
    position: fixed;
    bottom: 0;
    width: 100%;
    box-shadow: 0 -4px 8px rgba(0, 0, 0, 0.1);
}
```

</details>