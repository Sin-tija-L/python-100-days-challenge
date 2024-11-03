
# 🚀 Day 80: Incoming Data Handling!

Today, we’ll dive into handling form data in Flask! We’re going to retrieve data from a form and add some logic to decide what response the server will give based on user input. Let’s get started! 🌟

### Challenge Instructions (Run in VSCode)

---

## 📝 Challenge Overview

Currently, our `@app.route()` doesn’t have a method to receive the form data. So let’s set up a route that allows us to **receive and handle POST data** from the form submission.

---

## 👩‍💻 Step-by-Step

1. **Import**: First, add `request` from Flask to handle incoming form data.
2. **Set up the Route**: Use `@app.route` to define a route where we’ll handle the form submission. We’ll set the route’s method to `"POST"` so that it receives the data from the form.
3. **Define the `process()` function**: This function will use `request.form` to access the form data and return it as a dictionary.

---

## 🔧 HTML Form in `templates/login.html`

Here’s the HTML form to save in `templates/login.html`:

```python
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width">
  <title>Login Form</title>
  <link href="{{ url_for('static', filename='styles/login.css') }}" rel="stylesheet" type="text/css">
</head>
<body>
  <h1>Login to Your Account</h1>
  
  <form method="post" action="/process">
    <p>Name: <input type="text" name="username" required></p>
    <p>Email: <input type="email" name="email"></p>
    <p>Website: <input type="url" name="website"></p>
    <p>Age: <input type="number" name="age"></p>
    <input type="hidden" name="userID" value="232">
    <p>
      Favorite Woman in Tech:
      <select name="women_in_it">
        <option value="ada_lovelace">Ada Lovelace</option>
        <option value="grace_hopper">Grace Hopper</option>
        <option value="katherine_johnson">Katherine Johnson</option>
        <option value="radia_perlman">Radia Perlman</option>
        <option value="margaret_hamilton">Margaret Hamilton</option>
      </select>
    </p>
    <button type="submit">Save Data</button>
  </form>
</body>
</html>
```

---

## 🌐 Full Flask Code with Templates

Here's the updated Flask code in `day80.py` to display the form and process the data:

```python
from flask import Flask, request, render_template

app = Flask(__name__)

# Home route to display the login form
@app.route('/')
def index():
    return render_template("login.html")

# Process route to handle form data
@app.route('/process', methods=["POST"])
def process():
    page = ""
    form = request.form
    if form["women_in_it"] == "ada_lovelace":
        page += f"You're amazing, {form['username']}! Ada Lovelace is a brilliant choice."  # Personalized message for Ada Lovelace
    else:
        page += f"You’ve made a great choice, {form['username']}! Celebrating all women in tech!"  # Message for other choices
    return page  # Returns the response message

app.run(host='0.0.0.0', port=81, debug=True)
```

### Explanation of Changes

- **Home Route (`/`)**: This route now renders `login.html` from the `templates` folder using `render_template`.
- **Process Route (`/process`)**: Processes the form data and returns a custom message based on the user’s selection.

<img id="image" src="assets/day80_1.png" alt="day80 image" width="960">

---

## 📋 Summary

By completing this challenge, you’ll:

- Organize HTML templates in the `templates` folder.
- Use Flask’s `render_template` to load HTML files.
- Handle form data with `request.form` and return dynamic responses.

Enjoy creating an interactive, organized Flask app in VSCode! 🎉

--- 

## Common Errors
 
 First, delete any other code in your `day80` files. Copy each code snippet below into `day80` files by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.


### If You Don't Ask.....

👉 What's the problem here?

 ```python
from flask import Flask

app = Flask(__name__)

@app.route("/process", methods=["POST"])
```

<details>
<summary>👀 Answer</summary>

I forgot to import the `request` library. This will throw an internal server error with the text 'request is not defined' in there somewhere.

```python
from flask import Flask, request

app = Flask(__name__)

@app.route("/process", methods=["POST"])
```

</details>

---

### Inputs Anonymous

👉 What's the problem here?

 ```python
    <form method = "post" action="/process">
    <p>Name: <input type="text" required> </p>
    <p>Email: <input type="Email"> </p>
    <input type="hidden" name="userID" value="232"> </p>
    <p>
          Favorite Woman in Tech:
          <select name="women_in_it">
            <option value="ada_lovelace">Ada Lovelace</option>
            <option value="grace_hopper">Grace Hopper</option>
            <option value="katherine_johnson">Katherine Johnson</option>
            <option value="radia_perlman">Radia Perlman</option>
            <option value="margaret_hamilton">Margaret Hamilton</option>
          </select>
        </p>
    <button type="submit">Save Data</button>
  </form>
```

<details>
<summary>👀 Answer</summary>

I've not given each of my options the `name` attribute. The data input doesn't get stored anywhere so it can't be passed on. This will throw a 'Bad Request'.


```python
<form method="post" action="/process">
        <p>Name: <input type="text" name="username" required></p>
        <p>Email: <input type="email" name="email"></p>
        <p>Website: <input type="url" name="website"></p>
        <p>Age: <input type="number" name="age"></p>
        <input type="hidden" name="userID" value="232">
        <p>
          Favorite Woman in Tech:
          <select name="women_in_it">
            <option value="ada_lovelace">Ada Lovelace</option>
            <option value="grace_hopper">Grace Hopper</option>
            <option value="katherine_johnson">Katherine Johnson</option>
            <option value="radia_perlman">Radia Perlman</option>
            <option value="margaret_hamilton">Margaret Hamilton</option>
          </select>
        </p>
        <button type="submit">Save Data</button>
</form>
```

</details>

---


# 👉 Day 80 Challenge: Authenticating Users in Flask! 🚀

Today, we’re transforming yesterday’s login form into a fully functioning login system! You’ll connect the form to Flask, create a welcome page for valid users, and a “naughty step” page for unsuccessful login attempts. 😈

---

## 🛠️ Challenge Overview

In this challenge, you’ll:

1. **Set up valid credentials**: Define three valid username-password combinations.
2. **Build routes for success and failure**: 
   - A welcoming page for successful logins 🌟
   - A “naughty step” page for invalid logins 👹
3. **Authenticate Users**: Check user credentials when they submit the form and redirect them to the appropriate page.

---

## 🔧 Steps to Complete the Challenge

1. **Set Up Valid Credentials**: In `day80.py`, define three username-password pairs as a dictionary or list of tuples for easy lookup.

2. **Create Login Logic**: Use `request.form` to retrieve the login data from the form, check it against your valid credentials, and decide where to direct the user.

3. **Create Routes for Success and Failure**:
    - **Success Route** (`/welcome`): This route will display a friendly welcome page to users with correct credentials.
    - **Failure Route** (`/naughty-step`): This route will display a “naughty step” page to users with incorrect credentials or attempted unauthorized access.

---

## 🌐 Flask Code Structure

Here’s how to structure your Flask code to handle the authentication process:

1. **Home Route** (`/`): Displays the login form.
2. **Process Route** (`/login`): Handles form submission, checks credentials, and redirects users based on success or failure.
3. **Welcome Route** (`/welcome`): Displays a “nice” page for valid users.
4. **Naughty Step Route** (`/naughty-step`): Displays a “hideous” page for invalid users.

---

## ✨ Example Flask Code Outline

1. **Define Credentials**: Use a dictionary to store valid username-password pairs.
2. **Authentication Logic in `process()`**: Check if the submitted credentials match any in your valid list.
3. **Redirect Users Based on Validation**:
    - If valid, redirect to `/welcome`.
    - If invalid, redirect to `/naughty-step`.

---

## 📝 Code Outline

1. **Define Valid Credentials**:
   - Store three username-password pairs in `day80.py` for validation.
2. **Home Route** (`/`):
   - Renders the login form.
3. **Login Process Route** (`/login`):
   - Checks submitted credentials and redirects accordingly.
4. **Welcome Route** (`/welcome`):
   - Renders a friendly page for valid users.
5. **Naughty Step Route** (`/naughty-step`):
   - Renders a warning page for invalid login attempts.

---

## 🎉 Summary

By completing this challenge, you’ll create a basic authentication system that:

- Validates user credentials from a predefined list.
- Redirects users to success or failure pages based on their input.
- Adds interactivity to your Flask app with conditional redirects.

Enjoy creating a secure, interactive login system! Try it out with different combinations to see how the server responds. 🔒🌟

---

## Solution (No Peeking!)


<details>
<summary>👀 Answer</summary>

---

## `day80.py` (Python Code)

```python
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Define valid username-password combinations
valid_credentials = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3"
}

# Home route to display the login form
@app.route('/')
def index():
    return render_template("login.html")

# Process route to handle form data
@app.route('/login', methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    
    # Check if the username and password match any valid credentials
    if username in valid_credentials and valid_credentials[username] == password:
        return redirect(url_for('welcome'))
    else:
        return redirect(url_for('naughty_step'))

# Welcome route for valid users
@app.route('/welcome')
def welcome():
    return render_template("welcome.html")

# Naughty step route for invalid users
@app.route('/naughty-step')
def naughty_step():
    return render_template("naughty_step.html")

# Run the app
app.run(host='0.0.0.0', port=81, debug=True)
```

---

## `templates/login.html` (Login Form HTML)

```python
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width">
  <title>Login</title>
  <link href="{{ url_for('static', filename='styles/login.css') }}" rel="stylesheet" type="text/css">
</head>
<body>
  <div class="form-container">
    <h1>Login to Your Account</h1>
    <form method="post" action="/login">
      <p>Username: <input type="text" name="username" required></p>
      <p>Password: <input type="password" name="password" required></p>
      <button type="submit">Login</button>
    </form>
  </div>
</body>
</html>
```

---

## `templates/welcome.html` (Welcome Page HTML)

```python
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width">
  <title>Welcome</title>
  <link href="{{ url_for('static', filename='styles/login.css') }}" rel="stylesheet" type="text/css">
</head>
<body>
  <div class="welcome-container">
    <h1>Welcome!</h1>
    <p>You have successfully logged in. 🎉</p>
  </div>
</body>
</html>
```

---

## `templates/naughty_step.html` (Naughty Step Page HTML)

```python
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width">
  <title>Access Denied</title>
  <link href="{{ url_for('static', filename='styles/login.css') }}" rel="stylesheet" type="text/css">
</head>
<body>
  <div class="naughty-container">
    <h1>Access Denied</h1>
    <p>Uh-oh! Invalid credentials. Please try again. 😈</p>
  </div>
</body>
</html>
```

---

## `static/styles/login.css` (CSS for Styling)

```python
/* General body styling */
body {
    font-family: Arial, sans-serif;
    background-color: #f0f4f8;
    color: #333;
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    margin: 0;
}

/* Form container styling */
.form-container, .welcome-container, .naughty-container {
    background-color: #ffffff;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    padding: 40px;
    max-width: 400px;
    width: 100%;
    text-align: center;
}

/* Title styling */
h1 {
    color: #4a90e2;
    margin-bottom: 20px;
}

/* Form input fields */
form p {
    margin: 15px 0;
}

input[type="text"], input[type="password"] {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
    margin-top: 5px;
    font-size: 1em;
}

/* Button styling */
button[type="submit"] {
    background-color: #4a90e2;
    color: #fff;
    border: none;
    border-radius: 4px;
    padding: 10px 20px;
    font-size: 1em;
    cursor: pointer;
    margin-top: 15px;
    width: 100%;
    transition: background-color 0.3s ease;
}

button[type="submit"]:hover {
    background-color: #357abd;
}

/* Special styling for success and failure messages */
.welcome-container p {
    font-size: 1.2em;
    color: #4a90e2;
}

.naughty-container p {
    font-size: 1.2em;
    color: #d9534f;
}
```

</details>

