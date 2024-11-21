# Day 93: API? Spotify? Verify! 🎵

The APIs we've been using so far are pretty unusual in that they provide their service for free.

Normally, you have to pay to use an API's data services (at least if you're doing so commercially). This means that you will need to verify your status as an approved user before you can get your hands on all of that sweet, sweet data! 😎

Today, we're learning how to write a program that tells an API that we've got an account before accessing its info.

Don't worry, you won't have to bust out the credit card. We're using a Spotify API that won't charge provided we keep our usage under a certain level.

**Note:** Spotify has reserved this API for production-level apps. To ensure that we can continue using the API to learn and build in 100DoC, please refrain from requesting quota extensions from Spotify for your 100DoC projects.

---

## Get Started 🚀

👉 **Go to the [Spotify developer page](https://developer.spotify.com/)** and log in/create an account.

👉 Then open Dashboard or just go here [Dashboard](https://developer.spotify.com/dashboard)

<img id="image" src="assets/day93_1.png" alt="day93 image" width="690">

👉 **Redirect URI:** While creating the app, Spotify will ask you to provide at least one Redirect URI. This is the URL where Spotify will send users after they authorize your application. For testing purposes, you can use:

   ```python
   http://localhost:8888/callback
   ```

👉 **Next, hit "Create App"** and give it a name and description.

<img id="image" src="assets/day93_2.png" alt="day93 image" width="890">

👉 Copy the `Client ID` that you can find under ***Settings*** button and store it securely in a `.env` file. 

👉 Go back to Spotify and click **"Show Client Secret"**. Copy it and store it as well in your `.env` file.

   ```python
   CLIENT_ID=your_client_id_here
   CLIENT_SECRET=your_client_secret_here
   ```

Now, you have the "username" and "password" that your program needs to talk to Spotify.

---

## Authenticate 🔐

Now we have access to a whole bunch of music-related data. You can find and test all of the different category data on the Spotify API page in the **categories** tab.

---

### Connect to Spotify

👉 First though, we need to connect our program to Spotify. Step 1 is to import a bunch of libraries. Line 2 is a new library that authenticates our Spotify credentials against their API.

```python
import requests, os
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
```

👉 Then bring in our secrets and assign to variables.

```python
import requests, os
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables and configure the app
load_dotenv(dotenv_path='python-dotenv/.env')
clientID = os.getenv("CLIENT_ID")
clientSecret = os.getenv("CLIENT_SECRET")
```

---

### Authenticate

👉 Now to authenticate with Spotify's system. This is tricky the first time, but after that you'll have the code that you can reuse.

Authenticating gives you a **token** (a series of seemingly random numbers & letters) that is the '*I'm allowed in here'* pass for your program.

There's a lot going on here. So, here's the breakdown:

- I've set up variables to store the data needed for authentication.
    - `url` stores the web address to connect to
    - `data` creates a dictionary that communicates with the API in the correct way. It basically says to Spotify *'Send me back the credentials based in my client ID and secret. Here's a dictionary format to put them in'*.
    - `auth` uses the new `HTTPBasicAuth` function to send your client ID and secret to Spotify as pretty much the username and password to log you in.
    - `response` stores the API key that will be returned by the `requests` function that sends Spotify the login info needed.

- After that, I've added some `print` functions to output the info we get back for testing purposes.

```python
# Authenticate with Spotify
url = "https://accounts.spotify.com/api/token"
data = {"grant_type": "client_credentials"}
auth = HTTPBasicAuth(clientID, clientSecret)

response = requests.post(url, data=data, auth=auth)

print(response.ok)
print(response.json())
print(response.status_code)
```

---

### Whole Code So Far 🖥️

Once you've tested the prints and know everything is working, you can remove them and extract the access token. Here's the whole code so far:

```python
import requests, os
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables and configure the app
load_dotenv(dotenv_path='python-dotenv/.env')

clientID = os.getenv("CLIENT_ID")
clientSecret = os.getenv("CLIENT_SECRET")

# Authenticate with Spotify
url = "https://accounts.spotify.com/api/token"
data = {"grant_type": "client_credentials"}
auth = HTTPBasicAuth(clientID, clientSecret)
response = requests.post(url, data=data, auth=auth)
accessToken = response.json()["access_token"]

print("Authentication successful! 🎉")
```

---

## Set Up a Search 🔍

👉 Go to the Spotify API page, select **Documentation > Web API**, and grab the endpoint details.

<img id="image" src="assets/day93_3.png" alt="day93 image" width="890">

👉 Then from the left tab **Reference > Search > Search for Item**, and grab the endpoint details.

<img id="image" src="assets/day93_4.png" alt="day93 image" width="890">

👉 I've inserted it into my code in the `url` variable (I can reuse it because it's done it's job of logging me in earlier). Additionally, I've set up a `headers` variable that will enable communication with the Spotify API using my access token as a pass.

```python
url = "https://api.spotify.com/v1/search"
headers = {'Authorization': f'Bearer {accessToken}'}
```

👉 Let's search for an artist, format the query, and set the search parameters to display five results.

This is example from **Spotify** that we are going to update

<img id="image" src="assets/day93_5.png" alt="day93 image" width="890">

**Updated Code Sample**

```python
import requests, os
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables and configure the app
load_dotenv(dotenv_path='python-dotenv/.env')

clientID = os.getenv("CLIENT_ID")
clientSecret = os.getenv("CLIENT_SECRET")

# Authenticate with Spotify
auth_url = "https://accounts.spotify.com/api/token"
data = {"grant_type": "client_credentials"}
auth = HTTPBasicAuth(clientID, clientSecret)
response = requests.post(auth_url, data=data, auth=auth)

if response.ok:
    accessToken = response.json()["access_token"]
else:
    print("Authentication failed.")
    exit()

# Set up the search query
search_url = "https://api.spotify.com/v1/search"
headers = {'Authorization': f'Bearer {accessToken}'}
search_query = "?q=artist%3Aqueen&type=track&limit=5" # !!HERE!!
full_url = f"{search_url}{search_query}"

# Fetch data from Spotify
response = requests.get(full_url, headers=headers)

if response.ok:
    data = response.json()
    for track in data["tracks"]["items"]:
        print(f"🎶 {track['name']}")
        print(f"🔗 Preview: {track['preview_url']}")
else:
    print("Failed to fetch tracks.")
    print(response.json())
```

---

## Making This Customizable ✨

👉 How about making our search user-customizable? Let’s allow the user to input an artist’s name directly.
- Asked the user to input an artist
- Tidied up their input
- formatted the search URL as an fString that includes the artist

```python
import requests, os
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables and configure the app
load_dotenv(dotenv_path='python-dotenv/.env')

clientID = os.getenv("CLIENT_ID")
clientSecret = os.getenv("CLIENT_SECRET")

# Authenticate with Spotify
auth_url = "https://accounts.spotify.com/api/token"
data = {"grant_type": "client_credentials"}
auth = HTTPBasicAuth(clientID, clientSecret)
response = requests.post(auth_url, data=data, auth=auth)

if response.ok:
    accessToken = response.json()["access_token"]
else:
    print("Authentication failed.")
    exit()

# Get artist input from the user
artist = input("Artist: ").strip().lower().replace(" ", "%20")

# Set up the search query
search_url = "https://api.spotify.com/v1/search"
headers = {'Authorization': f'Bearer {accessToken}'}
search_query = f"?q=artist%3A{artist}&type=track&limit=5"
full_url = f"{search_url}{search_query}"

# Fetch and process results
response = requests.get(full_url, headers=headers)

if response.ok:
    data = response.json()
    for track in data["tracks"]["items"]:
        print(f"🎶 {track['name']}")
        print(f"🔗 Preview: {track['preview_url']}")
else:
    print("Failed to fetch tracks.")
    print(response.json())
```

---

## Common Errors
 
 First, delete any other code in your `day93` files. Copy each code snippet below into `day93` files by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

### Step By Step

Not so much errors in this code. Just advice to build step by step.
- Get your access token and check it.
- Build your queries and check them in the Spotify API console.
- Check the URLs **very very very** carefully.

--- 

## Fix My Code
 
 First, delete any other code in your `day93` files. Copy each code snippet below into `day93` files by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

  ```python
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv(dotenv_path='python-dotenv/.env')

clientID = os.getenv("CLIENT_ID")
clientSecret = os.getenv("CLIENT_SECRET")

auth_url = "https://accounts.spotify.com/api/token"
data = {"grant_type": "client_credentials"}
auth = HTTPBasicAuth(clientID, clientSecret)
response = requests.post(auth_url, data=data, auth=auth)

if response.ok:
    accessToken = response.json()["access_token"]
else:
    print("Authentication failed.")
    exit()

artist = input("Artist: ").strip().lower().replace(" ", "%20")

search_url = "https://api.spotify.com/v1/search"
headers = {'Authorization': f'Bearer {accessToken}'}
search_query = f"?=artist%3A{artist}&type=track&limit=5"
full_url = f"{search_url}{search_query}"

response = requests.get(full_url, headers=headers)

if response.ok:
    data = response.json()
    for track in data["tracks"]["items"]:
        print(f"🎶 {track['name']}")
        print(f"🔗 Preview: {track['preview_url']}")
else:
    print("Failed to fetch tracks.")
    print(response.json())
```

<details>
<summary>👀 Answer</summary>

```python
import requests, os # Missing import
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv(dotenv_path='python-dotenv/.env')

clientID = os.getenv("CLIENT_ID")
clientSecret = os.getenv("CLIENT_SECRET")

auth_url = "https://accounts.spotify.com/api/token"
data = {"grant_type": "client_credentials"}
auth = HTTPBasicAuth(clientID, clientSecret)
response = requests.post(auth_url, data=data, auth=auth)

if response.ok:
    accessToken = response.json()["access_token"]
else:
    print("Authentication failed.")
    exit()

arist = input("Artist: ").strip().lower().replace(" ", "%20") # Variable identifier typo

search_url = "https://api.spotify.com/v1/search"
headers = {'Authorization': f'Bearer {accessToken}'}
search_query = f"?q=artist%3A{artist}&type=track&limit=5"  # Missing 'q' in the URL - yes, this will break the code! Any incorrect URL will
full_url = f"{search_url}{search_query}"

response = requests.get(full_url, headers=headers)

if response.ok:
    data = response.json()
    for track in data["tracks"]["items"]:
        print(f"🎶 {track['name']}")
        print(f"🔗 Preview: {track['preview_url']}")
else:
    print("Failed to fetch tracks.")
    print(response.json())
```

</details>

---

# 🎉 Day 93 Challenge: Build a Music Time Machine! 🎵

Today's challenge is an exciting one! You’ll be combining your skills with **Flask**, **Spotify API**, and a little web design to build something truly interactive and fun! 🚀 Let’s get started!

---

## 🧠 What You'll Build

Create a **Flask web app** that allows users to enter a specific year and explore the top 10 songs from that time! You'll even embed a playable preview for each song directly on the webpage. How cool is that? 🤩

---

## 🛠️ Steps to Complete the Challenge

### 1️⃣ Set Up Your Flask App 🐍

1. Open your **main.py** file in your Flask app.
2. Clear out any previous code to start fresh.
3. Write your Flask app structure, including a route for your homepage and form handling.

### 2️⃣ Build the Website 🌐

- Add a simple **HTML form** where users can input a year.
- Use Flask’s `render_template` to display the results.
- For an extra challenge, make it look stylish using some CSS (or even a framework like Bootstrap).

### 3️⃣ Search Spotify’s API 🔍

- Use the year entered by the user to construct a query.
- Fetch the top 10 songs from that year using the Spotify API.
- Extract song names and their preview URLs.

### 4️⃣ Display the Results 🎶

- Show the song names on your webpage.
- Use this snippet to embed a playable preview of each song:
  ```python
  <audio controls>
    <source src="{url}" type="audio/mpeg">
  </audio>
  ```

### 5️⃣ Add Extra Features 🌟

- Allow users to see more songs by adding an **offset** feature (e.g., show the next 10 songs when searching again).
- Improve the user experience by adding a "loading" message or some fun animations. 💫

---

## 🌟 Extra Challenge

**Add Pagination!**
- Let users explore even more songs by adding an **offset** parameter.
- Update the query dynamically based on the current page (e.g., first 10 songs, next 10 songs, etc.).

---

## 🎯 Goals for This Challenge

1. Build a fully functional Flask app with a form.
2. Fetch data dynamically from the Spotify API.
3. Display embedded music previews on a webpage.
4. Enhance the app with creative design and additional features! ✨

Good luck and have fun! 🚀

<img id="image" src="assets/day93_6.png" alt="day93 image" width="690">

<img id="image" src="assets/day93_7.png" alt="day93 image" width="520">

---

## Solution (No Peeking!)

<details>
<summary>👀 Answer</summary>

### day93.py

```python
from flask import Flask, render_template, request
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import os

# Load environment variables and configure the app
load_dotenv(dotenv_path='python-dotenv/.env')

app = Flask(__name__)

clientID = os.getenv("CLIENT_ID")
clientSecret = os.getenv("CLIENT_SECRET")

# Authenticate with Spotify
def get_access_token():
    url = "https://accounts.spotify.com/api/token"
    data = {"grant_type": "client_credentials"}
    auth = HTTPBasicAuth(clientID, clientSecret)
    response = requests.post(url, data=data, auth=auth)
    return response.json()["access_token"] if response.ok else None

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        year = request.form.get("year")
        access_token = get_access_token()
        if not access_token:
            return "Failed to authenticate with Spotify."
        
        # Spotify search query
        search_url = "https://api.spotify.com/v1/search"
        headers = {"Authorization": f"Bearer {access_token}"}
        query = f"?q=year:{year}&type=track&limit=10"
        response = requests.get(f"{search_url}{query}", headers=headers)
        
        if response.ok:
            songs = response.json()["tracks"]["items"]
            return render_template("results.html", songs=songs, year=year)
        else:
            return "Failed to fetch songs from Spotify."
    
    return render_template("day93.html")

if __name__ == "__main__":
    app.run(debug=True)
```

### `templates/day93.html`

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Music Time Machine 🎵</title>
</head>
<body>
    <h1>🎶 Music Time Machine 🎶</h1>
    <form action="/" method="POST">
        <label for="year">Enter a Year:</label>
        <input type="number" id="year" name="year" placeholder="e.g., 1995" required>
        <button type="submit">Go!</button>
    </form>
</body>
</html>
```

### `templates/results.html`

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Top Songs of {{ year }} 🎶</title>
</head>
<body>
    <h1>Top 10 Songs of {{ year }} 🎵</h1>
    <ul>
        {% for song in songs %}
        <li>
            <p>🎵 {{ song["name"] }} by {{ song["artists"][0]["name"] }}</p>
            <audio controls>
                <source src="{{ song["preview_url"] }}" type="audio/mpeg">
            </audio>
        </li>
        {% endfor %}
    </ul>
    <a href="/">🔙 Search Again</a>
</body>
</html>

```

</details>