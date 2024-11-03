
# 🎉 Yakkety Yak! Day 79 - Building Forms to Communicate with the Web Server

Today’s mission is all about making your web pages talk back to the web server! 🌐 We're going to build a form that gathers data from the user and packages it up to send to the server. Think of it like passing notes back and forth, but digital! 💌

### Challenge Instructions (Run in VSCode)

---

### 📝 Form Structure

#### form
Create a `<form>` tag in the `<body>` section.

```python
<form>
    
</form>
```

For now, it will be empty when you refresh, but don’t worry – we’ll fill it in soon! 💪

---

### 📬 Method & Action

Next, we’ll add a **POST method** to the form. This is like sealing an envelope with data and sending it to the server. We’ll also specify an **action**, which is the destination for our data. Later, we’ll create a Flask route to process this data, so we'll set the action to point to `/process`.

```python
<form method="post" action="/process">
    
</form>
```

---

### 🖊️ Getting Input

Inside the form, add an `<input>` tag to collect the user’s name. Input tags can gather different types of data depending on the `type` attribute, and every input should have an identifier using the `name` attribute. Here, we'll use `type="text"` to get a text input for the username.

```python
<form method="post" action="/process">
    <p>Name: <input type="text" name="username" required></p>
</form>
```

Notice the `required` attribute here – it makes the field mandatory, so users can’t submit the form without filling it in. 💼

---

### 📋 Different Types of Input Fields

Let’s add a few more input fields with different data types to make our form more versatile:

```python
<form method="post" action="/process">
    <p>Name: <input type="text" name="username" required></p>
    <p>Email: <input type="email" name="email"></p>
    <p>Website: <input type="url" name="website"></p>
    <p>Age: <input type="number" name="age"></p>
    <p><input type="hidden" name="userID" value="232"></p>
</form>
```

- **Hidden** fields, like `userID`, are useful for passing information that’s relevant to processing on the backend but doesn’t need to be visible to the user.

---

### 🪂 Drop-down Menus

To create a drop-down menu, we’ll use the `<select>` tag, which works like an unordered list. Each option is wrapped in `<option>` tags. Here's an example drop-down in our form:

```python
<form method="post" action="/process">
    <p>Name: <input type="text" name="username" required></p>
    <p>Email: <input type="email" name="email"></p>
    <p>Website: <input type="url" name="website"></p>
    <p>Age: <input type="number" name="age"></p>
    <p><input type="hidden" name="userID" value="232"></p>
    
    <p>
        Favorite Woman in Tech: 
        <select name="women_in_tech">
            <option value="ada_lovelace">Ada Lovelace</option>
            <option value="grace_hopper">Grace Hopper</option>
            <option value="katherine_johnson">Katherine Johnson</option>
            <option value="radia_perlman">Radia Perlman</option>
            <option value="margaret_hamilton">Margaret Hamilton</option>
        </select>
    </p>
</form>
```

Each option now has a `value` attribute that identifies the selection for the backend. This makes it easier to handle the user’s choice in Flask. 🎩

---

### 🔘 Buttons

To complete our form, let’s add a submit button so users can send their data. Here’s how to create a basic submit button:

```python
<form method="post" action="/process">
    <p>Name: <input type="text" name="username" required></p>
    <p>Email: <input type="email" name="email"></p>
    <p>Website: <input type="url" name="website"></p>
    <p>Age: <input type="number" name="age"></p>
    <p><input type="hidden" name="userID" value="232"></p>
    
    <p>
        Favorite Woman in Tech: 
        <select name="women_in_tech">
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

The submit button will send all the form data to the specified action when clicked. 🚀

---

### 🌐 Flask Code to Handle Form Data

Let’s create a Flask app that listens for the data from our form. In this example, the form sends data to the `/process` endpoint, so we’ll create a route to handle that.

#### `day79.py`

```python
from flask import Flask, request, render_template

app = Flask(__name__)

# Display the form
@app.route('/')
def index():
    return render_template("day79.html")

# Process form data
@app.route('/process', methods=['POST'])
def process_form():
    username = request.form.get("username")
    email = request.form.get("email")
    website = request.form.get("website")
    age = request.form.get("age")
    user_id = request.form.get("userID")
    woman_in_tech = request.form.get("women_in_tech")
    
    # Print the data to the console (just for debugging)
    print(f"Received data - Username: {username}, Email: {email}, Website: {website}, Age: {age}, User ID: {user_id}, Favorite Baldy: {woman_in_tech}")
    
    return f"Thank you, {username}! Your data has been saved."

# Run the app in debug mode for easier troubleshooting
app.run(host='0.0.0.0', port=81, debug=True)
```

This code will:
- **Display the form** at the root URL (`/`).
- **Process the form data** sent to `/process` and display a simple "Thank you" message.

👉 Our page is now looking a bit like this:

<img id="image" src="assets/day79_1.png" alt="day79 image" width="960">

<img id="image" src="assets/day79_2.png" alt="day79 image" width="960">

---

### 🌈 Summary

By now, you've built a form that:
- Collects data using input fields for various types (text, email, URL, number, hidden, and dropdown).
- Uses the `required` attribute to enforce mandatory fields.
- Submits data with a POST request.
- Uses Flask to handle and process the data on the server side.

Tomorrow, we’ll dive deeper into handling and storing this data – stay tuned! 🌟

--- 

## Common Errors
 
 First, delete any other code in your `day79` files. Copy each code snippet below into `day79` files by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.


### Common Error 1

👉 What's the problem here?

 ```python
<p>Email: <input type="Email"> </p>
```

<details>
<summary>👀 Answer</summary>

We missed the `name` attribute. You won't notice that anything has gone wrong with this type of error. There won't be a crash or a handy error message.

```python
<p>Email: <input type="Email" name="email"> </p>
```

</details>

---

### Common Error 2

👉 What's the problem here?

 ```python
    <p>Name: <input type="text" name="username" required> </p>
    <p>Email: <input type="Email" name="email"> </p>
    <p>Website: <input type="url" name="website"> </p>
    <p>Age: <input type="number" name="age"> </p>
    <input type="hidden" name="userID" value="232"> </p>

    <p>
        Favorite Woman in Tech: 
        <select name="women_in_tech">
            <option value="ada_lovelace">Ada Lovelace</option>
            <option value="grace_hopper">Grace Hopper</option>
            <option value="katherine_johnson">Katherine Johnson</option>
            <option value="radia_perlman">Radia Perlman</option>
            <option value="margaret_hamilton">Margaret Hamilton</option>
        </select>
    </p>

    <button type="submit">Save Data</button>
```

<details>
<summary>👀 Answer</summary>

The form was not inside `<form>` tags. This won't look any different, but saving data just won't work.

```python
<form>
    <p>Name: <input type="text" name="username" required> </p>
    <p>Email: <input type="Email" name="email"> </p>
    <p>Website: <input type="url" name="website"> </p>
    <p>Age: <input type="number" name="age"> </p>
    <input type="hidden" name="userID" value="232"> </p>

    <p>
        Favorite Woman in Tech: 
        <select name="women_in_tech">
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

## Fix My Code

👉 Try and fix this code which is *full* of errors.

First, delete any other code in your `day79` files. Copy each code snippet below into `day79` files by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.


```python
<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>replit</title>
  <link href="style.css" rel="stylesheet" type="text/css" />
</head>

<body>
  
    <p>Name: <input type="text" name="username" required> </p>
    <p>Email: <input type="Email"> </p>
    <p>Website: <input type="url" name="website"> </p>
    <p>Age: <input type="number" name="age"> </p>
    <input type="hidden" name="userID" value="232"> </p>

    <p>
        Favorite Woman in Tech: 
        <select name="women_in_tech">
            <option value="ada_lovelace">Ada Lovelace</option>
            <option value="grace_hopper">Grace Hopper</option>
            <option value="katherine_johnson">Katherine Johnson</option>
            <option value="radia_perlman">Radia Perlman</option>
            <option value="margaret_hamilton">Margaret Hamilton</option>
        </select>
    </p>

    <button type="submit">Save Data</button>
  
</body>

</html>

```

<details>
<summary>👀 Answer</summary>

```python
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>Form Example</title>
  <!-- Adjusted stylesheet link to reference the "static" folder as commonly used in Flask projects -->
  <link href="{{ url_for('static', filename='style.css') }}" rel="stylesheet" type="text/css">
</head>

<body>

  <!-- Added a form tag around the input fields so the data can be submitted to the server -->
  <form method="post" action="/process">
    
    <p>Name: <input type="text" name="username" required> </p>
    
    <!-- Added 'name' attribute to the email input so the form can capture the email data -->
    <p>Email: <input type="email" name="email"> </p>
    
    <p>Website: <input type="url" name="website"> </p>
    
    <p>Age: <input type="number" name="age"> </p>
    
    <!-- Removed the unnecessary closing </p> tag after the hidden input -->
    <input type="hidden" name="userID" value="232">

    <p>
      Favorite Woman in Tech: 
      <!-- Added value attributes for each option to store consistent data for backend processing -->
      <select name="women_in_tech">
        <option value="ada_lovelace">Ada Lovelace</option>
        <option value="grace_hopper">Grace Hopper</option>
        <option value="katherine_johnson">Katherine Johnson</option>
        <option value="radia_perlman">Radia Perlman</option>
        <option value="margaret_hamilton">Margaret Hamilton</option>
      </select>
    </p>

    <!-- Moved the submit button inside the form so it triggers form submission -->
    <button type="submit">Save Data</button>
  
  </form>

</body>

</html>
```

</details>

---

# 👉 Day 79 Challenge: Building a Login Form for Your Webpage 🚀

Today’s challenge is to create a login form for a webpage! This form will capture a username, email address, and password from the user, sending the data securely to the server. Let’s jump in and create a polished, user-friendly login form. 📝✨

---

## 🛠️ Challenge Overview

In this challenge, you’ll:

1. **Create a login form** with fields for the username, email, and password.
2. **Add a submit button** labeled “Login” that users will click to submit their data.
3. **Configure the form action** to send data to the `/login` route when the submit button is clicked.

---

## 🔧 HTML Structure

In your HTML file, set up a structure for capturing login details. Here are the essentials:

- **Form Tag**: Use a form with the `method` attribute set to `post` to send the data securely to the server.
- **Action Attribute**: Set `action="/login"` so that the form data posts directly to the `/login` route.
- **Input Fields**: Add fields for the username, email, and password, each with `required` attributes to ensure users can’t skip any fields.
- **Submit Button**: Add a submit button labeled “Login” to initiate the form submission.

Ensure the page links to your CSS file for styling by referencing it through Flask's static folder (e.g., `url_for('static', filename='style.css')`).

---

## 🌐 Flask Code for Handling the Login Form

To process the form data, set up a `/login` route in your Flask app:

1. **Home Route**: Create a route to display the login form.
2. **Login Route**: Set up the `/login` route to receive and handle the POST request from the form submission.
3. **Data Processing**: Capture the `username`, `email`, and `password` from the form, and send back a welcome message to the user.

By using Flask’s route structure, the login form data will be securely processed, and the server will display a custom response based on the input.

---

## 📋 Summary

By completing this challenge, you’ll create a form that:

- Collects essential login details from users.
- Posts data securely to a server route.
- Processes and acknowledges the login data on the server.

This essential component will enhance your web app’s interactivity and security, adding a new layer of functionality to your Flask projects! 🔒💻

---

## Solution (No Peeking!)


<details>
<summary>👀 Answer</summary>

---

👉 **day79.py**

```python
from flask import Flask, request, render_template

app = Flask(__name__)

# Display the login form
@app.route('/')
def index():
    return render_template("day79.html")

# Process login data
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")
    
    # For now, just print the data to the console for debugging
    print(f"Received login data - Username: {username}, Email: {email}, Password: [hidden]")

    # Respond with a simple message for now
    return f"Welcome, {username}! You are now logged in."

# Run the app in debug mode for easier troubleshooting
app.run(host='0.0.0.0', port=81, debug=True)
```

👉 **day79.html**

```python
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width">
  <title>Login Form</title>
  <link href="{{ url_for('static', filename='styles/day79.css') }}" rel="stylesheet" type="text/css">
</head>

<body>
  <div class="form-container">
    <h1>Login to Your Account</h1>
    
    <form method="post" action="/login">
      <p>Username: <input type="text" name="username" required></p>
      <p>Email: <input type="email" name="email" required></p>
      <p>Password: <input type="password" name="password" required></p>
      <button type="submit">Login</button>
    </form>
  </div>
</body>

</html>
```

👉 **day79.css**

```python
/* General styling */
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

.form-container {
    text-align: center;
}

h1 {
    color: #007acc;
    margin-bottom: 20px;
    font-size: 1.8em;
}

/* Form container */
form {
    background-color: #ffffff;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    padding: 40px;
    max-width: 400px;
    width: 100%;
    margin: 0 auto;
    text-align: left;
}

/* Label and input styling */
form p {
    margin: 15px 0;
    font-size: 1em;
}

input[type="text"],
input[type="email"],
input[type="password"] {
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
    background-color: #007acc;
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
    background-color: #005f99;
}
```

</details>
