# Day 88: Authentication Finesse 🚀

So far, we've learned to use authentication in our web apps, but we've been a bit pushy. Forcing users to authenticate on every page can be frustrating—especially for a blog engine where readers just want to enjoy your literary genius without constant logins. 😅

Today's task? Finessing the authentication process so it's smooth, professional, and user-friendly. Let's empower women in IT 🌟 by building a platform that feels polished!

Today we will practice with **Google Login**!

---

### Custom Buttons 🎨

To get started, ensure you're using **Google Login** for authentication. Google provides an easy-to-use API to integrate login buttons into your app.

👉 **Step 1:** Set up a Google Cloud Project (you'll need to create one in the [Google Cloud Console](https://console.cloud.google.com/)).  
👉 **Step 2:** Copy your **Client ID** and **Client Secret** for use in the code.

---

### 1. Create a Google Cloud Project 🛠️
To integrate Google Login into your app, follow these steps:

### Go to the Google Cloud Console
- Visit [Google Cloud Console](https://console.cloud.google.com/).
- If you don't have a Google Cloud account, follow the prompts to create one.

### Create a New Project
1. Click on the **Select a Project** dropdown in the top-left corner.
2. Click on **New Project** and fill in the required details:
   - **Project Name**: Choose a name for your project.
   - **Organization**: Select your organization or leave it as "No organization."
3. Click **Create** to finish setting up the project.

### Enable Google APIs
1. Go to **APIs & Services > Library**.
2. Search for **Cloud Identity API** and enable it for your project.
3. Once enabled, you’ll be redirected to the **API & Services > Dashboard page**, where you’ll see **Google Identity Services API** listed as active.

<img id="image" src="assets/day88_1.png" alt="day88 image" width="450">

### Configure OAuth Consent Screen
1. Navigate to **APIs & Services > OAuth Consent Screen**.
2. Select **External** as the user type.
3. Fill in the required information:
   - **App Name**
   - **User Support Email**
   - **Authorized Domains**: Add the domains where your app will run (e.g., `127.0.0.1` or `localhost` for local testing) or just wite **example.com**.
4. Save the configuration.

<img id="image" src="assets/day88_2.png" alt="day88 image" width="450">

### Create OAuth 2.0 Credentials
1. Navigate to **APIs & Services > Credentials**.
2. Click **Create Credentials > OAuth Client ID**.
3. Select **Web Application** as the application type.
4. Add your redirect URIs:
   - For local development:
     ```python
     http://127.0.0.1:5000/google/callback
     ```
5. Save and copy your **Client ID** and **Client Secret**.

<img id="image" src="assets/day88_3.png" alt="day88 image" width="450">

---

### 2. Install the `requests` Library 📦

The `requests` library is required to handle Google API calls. Follow these steps to install it:

1. Open your terminal or command prompt.
2. Run the following command:
   ```python
   pip3 install requests
   ```

3. Verify the installation by running:
   ```python
   pip3 show requests
   ```

---

### 3. HTML Template: Your Landing Page

Here’s a simple `page.html` file where we'll add the Google login button:

```python
<!DOCTYPE html>
<html>
  <head>
    <title>My Amazing Blog</title>
  </head>
  <body>
    <h1>Welcome to Women in IT Blogs 💻</h1>
    <p>Read stories of inspiring women who broke barriers in technology. 🚀</p>
    <!-- Login Button -->
    <a href="/google/login">
      <button id="login-btn">Login with Google</button>
    </a>
  </body>
</html>
```

---

### 4. Backend Logic: Flask Authentication 🧠

Use Python and Flask to handle the Google authentication logic. Update your Flask app to include OAuth 2.0 flow with Google:

```python
from flask import Flask, request, redirect, render_template
import requests
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='python-dotenv/.env')

app = Flask(__name__)
app.secret_key = os.getenv('SESSION_SECRET_KEY')

# Google OAuth 2.0 credentials
CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
REDIRECT_URI = "http://127.0.0.1:5000/google/callback"

# Step 0: Landing page with Google login button
@app.route('/')
def index():
    return render_template('page.html')

# Step 1: Redirect user to Google for login
@app.route('/google/login')
def google_login():
    auth_url = (
        "https://accounts.google.com/o/oauth2/auth"
        "?response_type=code"
        f"&client_id={CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}"
        "&scope=email%20profile"
    )
    return redirect(auth_url)

# Step 2: Handle Google callback
@app.route('/google/callback')
def google_callback():
    code = request.args.get('code')
    if not code:
        return "Error: No code provided", 400

    # Exchange code for access token
    token_url = "https://oauth2.googleapis.com/token"
    token_data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    }
    # Disable SSL verification
    token_response = requests.post(token_url, data=token_data, verify=False)
    token_json = token_response.json()

    print(token_response.text)  # Debugging token response

    access_token = token_json.get('access_token')
    if not access_token:
        return "Error: Unable to retrieve access token", 400

    # Fetch user profile
    profile_url = "https://www.googleapis.com/oauth2/v2/userinfo"
    headers = {'Authorization': f'Bearer {access_token}'}

    # Disable SSL verification
    profile_response = requests.get(profile_url, headers=headers, verify=False)
    print(profile_response.text)  # Debugging profile response

    profile_data = profile_response.json()

    name = profile_data.get('name', 'Unknown')
    email = profile_data.get('email', 'No email found')
    picture = profile_data.get('picture', '')

    return f"""
    <h1>Welcome, {name}!</h1>
    <p>Email: {email}</p>
    <img src="{picture}" width="200" alt="Profile Picture">
    """

if __name__ == "__main__":
    app.run(debug=True)
```

---

### 5. Start the Application 🏃‍♀️

To run your Flask application:

1. Open your terminal or command prompt in the directory where your Python file is located.
2. Run the following command:
   ```python
   python3 python_files/day88.py
   ```

3. Open your browser and go to:
   ```python
   http://127.0.0.1:5000
   ```

4. Click on the **Login with Google** button and test the authentication flow.

<img id="image" src="assets/day88_4.png" alt="day88 image" width="450">

---

### What's the Best Key? 🔑

Usernames might not be the best piece of info to use to identify a user because the user can change this. The unique and permanent key for every user is their **user ID**, which is guaranteed to never change. This makes it an ideal choice for identifying users in your application.

In addition to the user ID, Google provides other useful information about the user, such as:
- **Email**: The user's verified email address.
- **Profile Picture**: A URL to the user's profile picture.

---

### Display the Profile Picture 📸

Let’s enhance our app to display the user’s profile picture along with their name. This is already implemented in the `google_callback` function. The key code is:

```python
    profile_url = "https://www.googleapis.com/oauth2/v2/userinfo"
    headers = {'Authorization': f'Bearer {access_token}'}

    profile_response = requests.get(profile_url, headers=headers)
    profile_data = profile_response.json()

    name = profile_data.get('name', 'Unknown')
    email = profile_data.get('email', 'No email found')
    picture = profile_data.get('picture', '')
```

<img id="image" src="assets/day88_5.png" alt="day88 image" width="450">

---

### Explanation of Changes
1. **User ID**: While not displayed, you should use the user ID internally for identifying users uniquely in your database or session.
2. **Profile Picture**: The new API call retrieves the user's profile picture from Google.
3. **Dynamic Display**: The user’s name, email, and profile picture are now displayed dynamically on the `/google/callback` page.

With these enhancements, your app becomes more personalized and user-friendly! 🚀

---

## Resolving the `NotOpenSSLWarning` Error by Downgrading `urllib3`

When using Python libraries like `requests` and `urllib3` with macOS's system Python, you might encounter this warning:

```python
NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'.
```

This happens because macOS's Python is linked to **LibreSSL 2.8.3**, which is not fully compatible with `urllib3 v2` and newer.

---

## **Solution: Downgrade to `urllib3` v1.26.x**
`urllib3` v1.26.x is compatible with LibreSSL and works seamlessly with the macOS system Python. Here's how to uninstall the incompatible version and install a compatible one.

### **Steps to Downgrade `urllib3`**
1. **Uninstall the Current `urllib3` Version**
   Run the following command to remove the existing `urllib3` package:
   ```python
   pip3 uninstall urllib3
   ```

2. **Install `urllib3` v1.26.x**
   Install a compatible version of `urllib3` (v1.26.15 is recommended):
   ```python
   pip3 install urllib3==1.26.15
   ```

3. **Verify the Installed Version**
   Check that the correct version of `urllib3` is installed:
   ```python
   pip3 show urllib3
   ```
   Expected output:
   ```python
   Name: urllib3
   Version: 1.26.15
   ```

---

## **Why This Works**
`urllib3` v1.26.x does not require OpenSSL 1.1.1+, making it compatible with the macOS system Python linked to LibreSSL 2.8.3. This solution allows you to continue using macOS Python without modifying or replacing it.

---

## **Important Notes**
- Downgrading `urllib3` is a safe and effective workaround for local development.
- If you need the latest `urllib3` features, consider switching to a Python version linked to OpenSSL (e.g., using Homebrew or `pyenv`).

---

By following these steps, you can resolve the error and ensure your application runs smoothly with macOS's default Python.

---

## Common Errors
 
 First, delete any other code in your `day88` files. Copy each code snippet below into `day88` files by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.


### What's My Line?

👉 What's the problem here?

 ```python
<!DOCTYPE html>
<html>
  <body>
    <a>
      <button id="login-btn">Login with Google</button>
    </a>
  </body>
</html>
```

<details>
<summary>👀 Answer</summary>

- The `/google/login` must be included to login with Google

```python
<!DOCTYPE html>
<html>
  <body>
    <a href="/google/login">
      <button id="login-btn">Login with Google</button>
    </a>
  </body>
</html>

```

</details>

---

## Fix My Code
 
 First, delete any other code in your `day88` files. Copy each code snippet below into `day88` files by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

 ```python
from flask import Flask, request, redirect 
import requests
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='python-dotenv/.env')

app = Flask(__name__)
app.secret_key = os.getenv('SESSION_SECRET_KEY')

CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
REDIRECT_URI = "http://127.0.0.1:5000/google/callback"

@app.route('/')
def index():
    return render_template('google_login.html')

@app.route('/google/login')
def google_login():
    auth_url = (
        "https://accounts.google.com/o/oauth2/auth"
        "?response_type=code"
        f"&client_id={CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}"
        "&scope=email%20profile"
    )
    return redirect(auth_url)

@app.route('/google/callback')
def google_callback():
    code = request.args.get('code')
    if not code:
        return "Error: No code provided", 400

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

    print(token_response.text)

    access_token = token_json.get('access_token')
    if not access_token:
        return "Error: Unable to retrieve access token", 400

    profile_url = "https://www.googleapis.com/oauth2/v2/userinfo"
    headers = {'Authorization': f'Bearer {access_token}'}

    profile_response = requests.get(profile_url, headers=headers, verify=False)
    print(profile_response.text)

    profile_data = profile_response.json()

    name = profile_data.get('fullname', 'Unknown')
    email = profile_data.get('email', 'No email found')
    picture = profile_data.get('picture', '')

    return f"""
    <h1>Welcome, {name}!</h1>
    <p>Email: {email}</p>
    <img src="{picture}" width="200" alt="Profile Picture">
    """

if __name__ == "__main__":
    app.run(debug=True)
```

<details>
<summary>👀 Answer</summary>

```python
from flask import Flask, request, redirect, render_template # Mistake 1: Forgot to import render_template
import requests
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='python-dotenv/.env')

app = Flask(__name__)
app.secret_key = os.getenv('SESSION_SECRET_KEY')

CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
REDIRECT_URI = "http://127.0.0.1:5000/google/callback"

@app.route('/')
def index():
    # Mistake 2: Incorrect file path for the template
    return render_template('page.html')

@app.route('/google/login')
def google_login():
    auth_url = (
        "https://accounts.google.com/o/oauth2/auth"
        "?response_type=code"
        f"&client_id={CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}"
        "&scope=email%20profile"
    )
    return redirect(auth_url)

@app.route('/google/callback')
def google_callback():
    code = request.args.get('code')
    if not code:
        return "Error: No code provided", 400

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

    print(token_response.text)

    access_token = token_json.get('access_token')
    if not access_token:
        return "Error: Unable to retrieve access token", 400

    profile_url = "https://www.googleapis.com/oauth2/v2/userinfo"
    headers = {'Authorization': f'Bearer {access_token}'}

    profile_response = requests.get(profile_url, headers=headers, verify=False)
    print(profile_response.text)

    profile_data = profile_response.json()

    name = profile_data.get('name', 'Unknown') # Mistake 3: Using a wrong key in profile_data
    email = profile_data.get('email', 'No email found')
    picture = profile_data.get('picture', '')

    return f"""
    <h1>Welcome, {name}!</h1>
    <p>Email: {email}</p>
    <img src="{picture}" width="200" alt="Profile Picture">
    """

if __name__ == "__main__":
    app.run(debug=True)
```

</details>

---

# 👉 Day 88 Challenge: Enhancing Your Blog Engine with Smarter Logic 🚀

Today’s challenge focuses on adding intelligent login functionality to your blog engine. Your goal is to create a system that dynamically adjusts user experiences based on their login status and identity. Let’s make it more interactive and exciting! 💡

---

## **Requirements:**

1. **Public Blog Page** 📰  
   - Ensure your blog page remains accessible to everyone, whether they are logged in or not.  
   - This page should display your awesome content to all users without any login barriers.

2. **Admin Access for Yourself** 🛠️  
   - If a logged-in user matches your credentials (e.g., email address or username), they should be redirected to a **special admin page**.  
   - This page can display tools and controls only you, the admin, have access to. 🎩✨

3. **Warning for Unauthorized Users** 🚫  
   - If a logged-in user does not match your credentials, display a **“naughty user”** warning.  
   - Inform them they are trying to access a restricted area, and redirect them back to the public blog page.

---

## **Implementation Tips:**
- Use **conditional logic** to determine user access levels based on their identity.  
- Customize your responses to create a fun, engaging, and dynamic user experience.  
- Test thoroughly to ensure all routes and conditions are handled gracefully.

---

## **What You'll Practice:**
- Building access-controlled pages in Flask 🔐  
- Handling conditional redirects based on user credentials ↪️  
- Designing a multi-user experience with dynamic content 🎨  

---

💻 **Your mission:** Make your blog engine smarter and more welcoming, while ensuring restricted areas are secure and admin-exclusive. Let's see how creative you can get! 🚀


<img id="image" src="assets/day88_6.png" alt="day88 image" width="450">

<img id="image" src="assets/day88_7.png" alt="day88 image" width="450">

<img id="image" src="assets/day88_8.png" alt="day88 image" width="450">

<img id="image" src="assets/day88_9.png" alt="day88 image" width="450">

---

## Solution (No Peeking!)


<details>
<summary>👀 Answer</summary>

👉 **day88.py**

```python
from flask import Flask, request, redirect, render_template, flash, session
import requests
from dotenv import load_dotenv
import sqlite3
import os

# Initialize app and load environment variables
app = Flask(__name__)
load_dotenv(dotenv_path='python-dotenv/.env')
app.secret_key = os.getenv('SESSION_SECRET_KEY', 'fallback-secret-key')

DATABASE = "blog.db"

# Google OAuth 2.0 credentials
CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
REDIRECT_URI = "http://127.0.0.1:5000/google/callback"
AUTHORIZED_EMAIL = "example@gmail.com"  # Replace with your Google account email

# Initialize the database
def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
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

@app.route('/')
def index():
    """Landing page with Google login button."""
    posts = query_db("SELECT title, content, timestamp FROM posts ORDER BY timestamp DESC")
    return render_template('login.html', posts=posts)

@app.route('/google/login')
def google_login():
    """Redirect to Google for login."""
    auth_url = (
        "https://accounts.google.com/o/oauth2/auth"
        "?response_type=code"
        f"&client_id={CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}"
        "&scope=email%20profile"
    )
    return redirect(auth_url)

@app.route('/google/callback')
def google_callback():
    """Handle Google OAuth callback."""
    code = request.args.get('code')
    if not code:
        flash("Error: No authorization code provided.", "error")
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
        flash("Error: Unable to retrieve access token.", "error")
        return redirect('/')

    # Fetch user profile
    profile_url = "https://www.googleapis.com/oauth2/v2/userinfo"
    headers = {'Authorization': f'Bearer {access_token}'}
    profile_response = requests.get(profile_url, headers=headers, verify=False)
    profile_data = profile_response.json()

    email = profile_data.get('email', 'Unknown')

    # Check if the user is authorized
    if email == AUTHORIZED_EMAIL:
        session['admin'] = True
        flash(f"Welcome back, {profile_data.get('name')}! You are logged in as admin.", "success")
        return redirect('/edit')
    else:
        return redirect('/')

@app.route('/edit', methods=["GET", "POST"])
def edit():
    """Admin page for editing blog posts."""
    if not session.get('admin'):
        flash("Unauthorized access. Redirecting to the feed.", "error")
        return redirect('/')

    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        query_db("INSERT INTO posts (title, content) VALUES (?, ?)", (title, content), commit=True)
        flash("New blog entry added.", "success")

    posts = query_db("SELECT title, content, timestamp FROM posts ORDER BY timestamp DESC")
    return render_template('edit.html', posts=posts)

@app.route('/logout')
def logout():
    """Logout the admin."""
    session.clear()
    return redirect('/')

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
    <title>Blog Feed</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles/day87.css') }}" type="text/css">
</head>
<body>
    <div class="container">
        <h1>Welcome to the Blog</h1>
        <p>Read inspiring posts or log in to manage the blog:</p>

        <a href="/google/login">
            <button>Login with Google</button>
        </a>

        <h2>Blog Feed</h2>
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
            <p>No blog posts available yet. Check back later!</p>
        {% endif %}
    </div>
</body>
</html>
```

👉 **Other html's and css you can use from day 87.**

</details>