# 👉 Day 89 Challenge: Build Your Own Community Chat App! 💬🚀

Get ready to create an engaging and dynamic **Community Chat App** that connects users in real-time. Today's challenge takes your skills up a notch by blending authentication, user interaction, and admin controls. Let's dive in! 🌟

---

## **Your Mission** 🎯

1. **Create a Login Screen** 🔑  
   - Allow users to log in using **Google Authentication** (or any method of your choice).  
   - Once logged in, users will be welcomed into the chat room with their username and profile picture displayed.

2. **Build the Chat Room** 🗨️  
   - Display the **last 5 messages** for all users to see upon entry.  
   - Users can send new messages, which will appear with their **username** and **profile picture** for a personalized experience.  

3. **Admin Privileges** 🎩  
   Only **your username** will have special admin powers!  
   - **Admin Button**: Exclusive access to an admin panel or button for extra controls.  
   - **Delete Messages**: Ability to remove any message from the chat with a delete button next to each message.  

---

## **What to Focus On** 🔍  

- **Simple and Clean UI** 🎨  
  Make your chat room visually appealing and easy to navigate. No one likes a cluttered app!  

- **Authentication and Access Control** 🔐  
  Ensure that only authenticated users can access the chat room. Admin privileges should work exclusively for your username.  

- **User Interaction** 🧑‍🤝‍🧑  
  Focus on creating a fun and welcoming environment where users can easily communicate and see their messages in real-time.

---

## **What to Skip (For Now)** ⏳  
- **Auto-refreshing the chat**: We'll avoid JavaScript for now and keep this challenge focused on Python and Flask.

---

## **Why This Matters** 🌍  
This challenge mirrors real-world applications like Discord or Slack. You'll learn how to:  
- Manage user authentication and roles (users vs. admins).  
- Create dynamic features like adding and displaying messages.  
- Practice designing a user-friendly experience.  

---

<img id="image" src="assets/day89_1.png" alt="day89 image" width="550">

<img id="image" src="assets/day89_2.png" alt="day89 image" width="550">

<img id="image" src="assets/day89_3.png" alt="day89 image" width="550">

<img id="image" src="assets/day89_4.png" alt="day89 image" width="550">

<img id="image" src="assets/day89_5.png" alt="day89 image" width="550">

Ready to build your chat room and be the ultimate admin? 💬🎩  
Let’s get chatting! If it works, share a screenshot and drop a 🐙! 🎉

---

## Solution (No Peeking!)


<details>
<summary>👀 Answer</summary>

👉 **day89.py**

```python
 from flask import Flask, request, redirect, render_template, flash, session
import requests
import os
from flask_session import Session
import datetime
from dotenv import load_dotenv

# Initialize app and load environment variables
app = Flask(__name__)
load_dotenv(dotenv_path='python-dotenv/.env')
app.secret_key = os.getenv('SESSION_SECRET_KEY', 'fallback-secret-key')

# Google OAuth 2.0 credentials
CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
REDIRECT_URI = "http://127.0.0.1:5000/google/callback"
AUTHORIZED_EMAIL = "example@gmail.com"  # Replace with your admin email

# Messages storage
MESSAGES = []

def getMessages():
    """Return the last 5 messages."""
    return MESSAGES[-5:]

def addMessage(message):
    """Add a new message to the storage."""
    MESSAGES.append(message)

def deleteMessage(index):
    """Delete a message by its index."""
    if 0 <= index < len(MESSAGES):
        MESSAGES.pop(index)

# Configure Flask-Session
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route('/')
def index():
    """Landing page."""
    return render_template('login.html')

@app.route('/google/login')
def google_login():
    """Redirect to Google for authentication."""
    auth_url = (
        "https://accounts.google.com/o/oauth2/auth"
        "?response_type=code"
        f"&client_id={CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}"
        "&scope=email%20profile"
        "&prompt=select_account"
    )
    return redirect(auth_url)

@app.route('/google/callback')
def google_callback():
    """Handle Google OAuth callback."""
    code = request.args.get('code')
    if not code:
        flash("Authorization code not found. Please try again.", "error")
        return redirect('/')

    # Exchange authorization code for access token
    token_url = "https://oauth2.googleapis.com/token"
    token_data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    }
    token_response = requests.post(token_url, data=token_data, verify=False)
    token_json = token_response.json()
    access_token = token_json.get('access_token')

    if not access_token:
        flash("Failed to log in with Google. Please try again.", "error")
        return redirect('/')

    # Fetch user profile
    profile_url = "https://www.googleapis.com/oauth2/v2/userinfo"
    headers = {'Authorization': f'Bearer {access_token}'}
    profile_response = requests.get(profile_url, headers=headers, verify=False)
    profile_data = profile_response.json()

    email = profile_data.get('email', 'Unknown')
    name = profile_data.get('name', 'Unknown')

    # Check if the user is authorized
    session['username'] = name
    session['email'] = email
    if email == AUTHORIZED_EMAIL:
        session['admin'] = True
        flash(f"Welcome back, {name}! You are logged in as admin.", "success")
        return redirect('/chat')
    else:
        session['admin'] = False
        flash(f"Welcome, {name}! You are logged in.", "success")
        return redirect('/chat')

@app.route('/chat', methods=["GET", "POST"])
def chat():
    """Chat room."""
    if 'username' not in session:
        flash("Please log in to access the chat.", "error")
        return redirect('/')
    if request.method == "POST":
        new_message = {
            "username": session["username"],
            "content": request.form["message"],
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        addMessage(new_message)
        return redirect('/chat')

    messages = getMessages()
    return render_template('chat.html', messages=messages, display=session.get('admin', False))

@app.route('/admin', methods=["GET", "POST"])
def admin():
    """Admin page."""
    if not session.get('admin'):
        flash("Unauthorized access.", "error")
        return redirect('/chat')

    if request.method == "POST" and "delete" in request.form:
        deleteMessage(int(request.form["delete"]))
        flash("Message deleted.", "success")

    messages = getMessages()
    return render_template('admin.html', messages=messages)

@app.route('/logout')
def logout():
    """Logout user."""
    session.clear()
    flash("You have been logged out.", "info")
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
```

👉 **login.html**

```python
<!DOCTYPE html>
<html>
  <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width">
      <title>Login</title>
      <link rel="stylesheet" href="{{ url_for('static', filename='styles/day89.css') }}">
  </head>
<body>
    <div class="container">
        <h1>Login</h1>
        
        <a href="/google/login" class="google-login-btn">
            <img src="{{ url_for('static', filename='images/google-icon.png') }}" alt="Google Icon" />
            Login with Google
        </a>
    </div>
</body>
</html>
```

👉 **admin.html**

```python
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>Admin</title>
    <link href="{{ url_for('static', filename='styles/day89.css') }}" rel="stylesheet" type="text/css">
</head>
<body>
    <div class="container">
        <h1>Admin Panel</h1>
        
        <div class="admin-form">
            <form method="POST" action="/admin">
                <ul>
                    {% for message in messages %}
                        <li>
                            <label>
                                <input type="checkbox" name="delete" value="{{ loop.index0 }}">
                                <strong>{{ message.username }}</strong>: {{ message.content }}
                            </label>
                        </li>
                    {% endfor %}
                </ul>
                <button type="submit">Delete Selected</button>
            </form>
        </div>
        
        <a href="/chat">Chat Room</a>
        <a href="/logout">Logout</a>
    </div>    
</body>
</html>
```

👉 **chat.html**

```python
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>Chat</title>
    <link href="{{ url_for('static', filename='styles/day89.css') }}" rel="stylesheet" type="text/css">
</head>
<body>
    <div class="container">
        <h1>Chat Room</h1>
        
        <div class="chat-box">
            <ul>
                {% for message in messages %}
                    <li><strong>{{ message.username }}</strong>: {{ message.content }}</li>
                {% endfor %}
            </ul>
        </div>
        
        <div class="chat-input">
            <form method="POST" action="/chat">
                <input type="text" name="message" placeholder="Type your message..." required>
                <button type="submit">Send</button>
            </form>
        </div>
        
        <a href="/admin">Admin</a>
        <a href="/logout">Logout</a>
    </div>
</body>
</html>
```

👉 **day89.css**

```python
/* General styling */
body {
    background: linear-gradient(135deg, #ff69b4, #ffec40); /* Gradient Pink to Yellow */
    font-family: 'Poppins', sans-serif; /* Modern and clean font */
    color: #333; /* Dark gray for better contrast */
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
}

/* Centered container */
.container {
    max-width: 800px;
    width: 90%;
    margin: auto;
    padding: 30px;
    background-color: #fff;
    border-radius: 15px;
    box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.15);
    text-align: center;
}

/* Headings */
h1 {
    color: #ff69b4; /* Bright Pink */
    font-size: 2.5rem;
    margin-bottom: 20px;
}

/* Chat-specific styling */
.chat-box {
    background-color: #fef9e7; /* Soft pastel yellow */
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.1);
    margin: 20px 0;
    max-height: 400px;
    overflow-y: auto; /* Scrollable for longer chat history */
}

/* Login-specific styling */
.login-form {
    background-color: #f9f9f9; /* Subtle light gray */
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0px 6px 20px rgba(0, 0, 0, 0.1);
    color: #333; /* Dark gray text */
}

.login-form input[type="text"],
.login-form input[type="password"] {
    width: 90%;
    padding: 12px;
    margin: 15px 0;
    border: 1px solid #ddd;
    border-radius: 8px;
    font-size: 1rem;
    outline: none;
    transition: border 0.3s ease;
}

.login-form input[type="text"]:focus,
.login-form input[type="password"]:focus {
    border-color: #ff69b4;
}

/* Google Login Button */
.google-login-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    max-width: 300px;
    margin: 20px auto;
    padding: 12px 20px;
    font-size: 1.2rem;
    font-weight: bold;
    text-decoration: none;
    color: #fff;
    background-color: #4285f4; /* Google Blue */
    border-radius: 8px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    transition: background-color 0.3s ease, transform 0.2s;
}

.google-login-btn img {
    height: 20px;
    margin-right: 10px; /* Space between icon and text */
}

.google-login-btn:hover {
    background-color: #3367d6; /* Darker Google Blue */
    transform: scale(1.05); /* Slight zoom-in effect */
}

.google-login-btn:active {
    background-color: #2851a3; /* Even darker Google Blue */
    transform: scale(0.98); /* Slight shrink effect */
}

/* Error message styling */
.error-message {
    color: #ff4d4d; /* Red with better contrast */
    background-color: #ffe6e6; /* Light red background */
    padding: 10px;
    border-radius: 8px;
    margin-bottom: 20px;
    font-weight: bold;
}

.chat-message {
    background-color: #ff69b4; /* Bright Pink */
    color: white;
    padding: 15px;
    margin: 10px 0;
    border-radius: 10px;
    font-size: 1rem;
    box-shadow: 0px 3px 10px rgba(0, 0, 0, 0.1);
    text-align: left;
}

/* Input field and send button styling */
.chat-input {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 20px;
}

.chat-input input[type="text"] {
    flex-grow: 1;
    padding: 12px 15px;
    border: 1px solid #ddd;
    border-radius: 8px;
    font-size: 1rem;
    margin-right: 10px;
    outline: none;
    transition: border 0.3s ease;
}

.chat-input input[type="text"]:focus {
    border-color: #ff69b4; /* Pink focus */
    box-shadow: 0 0 5px rgba(255, 105, 180, 0.5);
}

.chat-input button {
    background-color: #ff69b4; /* Bright Pink */
    color: white;
    padding: 12px 20px;
    border: none;
    border-radius: 8px;
    font-size: 1.2rem;
    font-weight: bold;
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.2s;
}

.chat-input button:hover {
    background-color: #ff3385; /* Darker Pink */
    transform: scale(1.05);
}

.chat-input button:active {
    background-color: #cc005f; /* Even darker Pink */
    transform: scale(0.98);
}

/* Admin-specific styling */
.admin-message {
    background-color: #6c63ff; /* Soothing Purple */
    color: white;
    padding: 15px;
    margin: 10px 0;
    border-radius: 10px;
    font-size: 1rem;
    font-weight: bold;
    text-align: left;
    box-shadow: 0px 3px 10px rgba(0, 0, 0, 0.1);
}

.admin-form button {
    background-color: #6c63ff; /* Purple */
    color: white;
    padding: 12px 20px;
    border: none;
    border-radius: 8px;
    font-size: 1.2rem;
    font-weight: bold;
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.2s;
}

.admin-form button:hover {
    background-color: #4b44c0; /* Darker Purple */
    transform: scale(1.05);
}

.admin-form button:active {
    background-color: #352c8f; /* Even darker Purple */
    transform: scale(0.98);
}

/* Navigation buttons */
a {
    display: inline-block;
    margin: 10px 5px;
    padding: 10px 20px;
    background-color: #6c63ff; /* Purple */
    color: white;
    text-decoration: none;
    border-radius: 8px;
    font-weight: bold;
    transition: background-color 0.3s ease, transform 0.2s;
}

a:hover {
    background-color: #4b44c0; /* Darker Purple */
    transform: scale(1.05);
}

/* Responsive Design */
@media (max-width: 768px) {
    .container {
        padding: 20px;
    }

    h1 {
        font-size: 2rem;
    }

    .chat-input input[type="text"] {
        font-size: 0.9rem;
    }

    .chat-input button,
    .admin-form button {
        font-size: 1rem;
        padding: 10px 15px;
    }
}
```

</details>
