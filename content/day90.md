# Day 90: JSON 🚀

It's day 90, and today we're diving into how to use JSON (JavaScript Object Notation, pronounced *Jason*) to fetch data from websites. This is the first step toward mastering web scraping. 🌐

JSON is a text-based way of representing a nested dictionary (2D dictionary) and is commonly used for communication between websites. When you send a request to a website and get a response, it's often in JSON format. In Python, we interpret this JSON as a dictionary to make sense of it.

---

### Go Get The Data 📡

👉 Let's grab some data from a free website—[randomuser.me](https://randomuser.me)—that generates information about a fictional user.

Here's the code to fetch data and display it in VSCode:

```python
import requests  # Import the required library

# Fetch data from the API
result = requests.get("https://randomuser.me/api/")  

# Print the JSON response
print(result.json())
```

💡 **Run it in VSCode** using the terminal command:  
```python
python3 python_files/day90.py
```

You'll see a lot of data displayed on your terminal! 🎉

---

### Tidy It Up ✨

👉 Let's format the output for better readability. The following code indents the JSON data to make it more visually appealing:

```python
import requests, json  # Import necessary libraries

# Fetch data from the API
result = requests.get("https://randomuser.me/api/")  
user = result.json()  # Store the JSON response as a dictionary

# Print the JSON data with indentation
print(json.dumps(user, indent=2))
```

💡 This will format your output, making it easier to see that the response is a dictionary. The first-level dictionary key is `results`.

<img id="image" src="assets/day90_1.png" alt="day90 image" width="690">

---

### Output Specific Data 🔍

👉 Here's the code to output one piece of data about the user. I'm going to output their first and last names. I've commented out the 'output everything' line of code to focus on the one piece of information output.

```python
import requests, json  

# Fetch data from the API
result = requests.get("https://randomuser.me/api/")  
user = result.json()  

# Extract and format the user's first and last name
name = f"{user['results'][0]['name']['first']} {user['results'][0]['name']['last']}"  

# Print the name
print(name)
```

Every time you run this script, you'll get a new random user with their name displayed. 👩‍💻

---

### Pictures: Everybody Needs Good Pictures 🖼️

If you scrolled down the big json data file, you might have noticed that images were also part of our random user's profile:

<img id="image" src="assets/day90_2.png" alt="day90 image" width="690">

👉 Let's get the image as well and let's store it in a local file. Here's the code in isolation:

```python
import requests, json  

# Fetch data from the API
result = requests.get("https://randomuser.me/api/")  
user = result.json()  

# Extract the user's profile picture URL
image = f"{user['results'][0]['picture']['medium']}"  

# Download the image
picture = requests.get(image)  
with open("python_files/photos/image.jpg", "wb") as f:  # Save the image in the python_files directory
    f.write(picture.content)  

# Print the image URL
print(image)
```

💡 After running this script, you'll find `image.jpg` saved in the `python_files/photos` directory. Change `"medium"` to `"large"` in the code to get a higher-resolution image.

<img id="image" src="assets/day90_3.png" alt="day90 image" width="690">

---

## Complete Example 🎯

Here’s the complete code that fetches a user's name and profile picture:

```python
import requests, json  

# Fetch data from the API
result = requests.get("https://randomuser.me/api/")  
user = result.json()  

# Extract the user's name
name = f"{user['results'][0]['name']['first']} {user['results'][0]['name']['last']}"  

# Extract the profile picture URL
image = f"{user['results'][0]['picture']['medium']}"  

# Download and save the profile picture
picture = requests.get(image)  
with open("python_files/photos/image.jpg", "wb") as f:  
    f.write(picture.content)  

# Print the image URL and the user's name
print(image)  
print(name)
```

Run this in VSCode, and you'll get the user's name and profile picture saved locally. 🎉

---

### Loops: Clean and Efficient Code 🔄

👉 Use loops to simplify the code. This is especially useful if multiple users are returned in the JSON data.

```python
import requests, json  

# Fetch data from the API
result = requests.get("https://randomuser.me/api/")  
user = result.json()  

# Loop through each user in the results and print their name
for person in user["results"]:  
    name = f"{person['name']['first']} {person['name']['last']}"  
    print(name)
```

💡 This code will loop through all users in the JSON response and print their names. Currently, the API returns only one user, but this setup is ready for more. 🚀

---

## Common Errors
 
 First, delete any other code in your `day90` files. Copy each code snippet below into `day90` files by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.


### No Data

👉 What's the problem here?

One of the common problems with json is not getting any data back from the website. This isn't something you can spot in your code. To check for it, you request a 'status code' from the API. A code of 200 means that all is well. Here, I've coded in an if to generate an error message if the status code isn't 200.

 ```python
if result.status_code != 200:
  print("Error, couldn't get API")
```

---

## Fix My Code
 
 First, delete any other code in your `day90` files. Copy each code snippet below into `day90` files by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

  ```python
import requests,

result = requests.get("randomuser.me/api/")
user = result.json() 

for person in user['results']: 
  name = f"""{person["name"]["first"]} {person["name"]["last"]}""" 

  print(name)
```

<details>
<summary>👀 Answer</summary>

```python
import requests

result = requests.get("https://randomuser.me/api/") # missed the full URL
if result.status_code != 200: # No status check
  print("Error, couldn't get API")

user = result.json() 

for person in user['results']: 
  name = f"""{person["name"]["first"]} {person["name"]["last"]}""" 

  print(name)
```

</details>

---

# 👉 Day 90 Challenge: Building Your Own User Gallery 🖼️

Today’s challenge is an exciting step forward in your JSON journey! 🌟 You'll be pulling in data for **10 users** from the [randomuser.me API](https://randomuser.me) and building a mini-profile gallery on your local machine. 🎉

Your mission, should you choose to accept it, involves downloading and saving user profile pictures dynamically based on their names.

---

## 📝 **Challenge Requirements**

1. **Fetch Data for 10 Users:**  
   Use the `randomuser.me` API to grab data for 10 unique users.

2. **Save Profile Pictures Locally:**  
   - Extract the **medium-quality profile picture** for each user.
   - Save each picture locally with the format:  
     **`{firstName} {lastName}.jpg`**  
     For example, if the user is "Jane Doe," the file should be named `Jane Doe.jpg`.

3. **Unique Files:**  
   Each user’s profile picture should be saved as a **separate file**—no overwriting allowed! 🚫

---

## 🛠️ **Hints and Tips**

- **API Call Adjustments:**  
  The API can return multiple users in a single response. Adjust your request URL to get data for 10 users by appending `?results=10` to the API endpoint:  
  ```python
  https://randomuser.me/api/?results=10
  ```

- **Dynamic Filenames:**  
  Use Python’s `f-strings` to create the filename dynamically based on the user’s first and last names.  
  ```python
  filename = f"{first_name} {last_name}.jpg"
  ```

- **Save Images:**  
  Remember to open your files in binary mode (`"wb"`) for writing image data:
  ```python
  with open(filename, "wb") as file:
      file.write(picture.content)
  ```

---

## 🎯 **Stretch Goals (Optional, but Fun!)**

If you’re feeling adventurous, try these bonus challenges:

1. **Add Logging:**  
   Create a log file (`log.txt`) that records the names of all users whose pictures were downloaded, along with timestamps. 🕒

2. **High-Quality Images:**  
   Update the code to fetch **high-quality** profile pictures instead of medium-quality. Replace `"medium"` with `"large"` in the image URL.

3. **Organize by Gender:**  
   Save the profile pictures into folders named `Male` and `Female` based on the user's gender. 📁

4. **Create a Mini-Gallery:**  
   Use a Python library like `Pillow` to display the downloaded pictures in a grid format. 🖼️

---

## 🥳 **What You’ll Learn**

By completing this challenge, you’ll reinforce key concepts such as:

- Fetching and handling JSON data from APIs 📡
- Working with Python’s file I/O for saving content locally 📝
- Using dynamic variables for better code organization 📂
- Applying loops to handle repetitive tasks efficiently ♻️

---

Take on the challenge and see your gallery come to life! 💪✨ Good luck! 🚀

<img id="image" src="assets/day90_4.png" alt="day90 image" width="690">

---

## Solution (No Peeking!)


<details>
<summary>👀 Answer</summary>

```python
import requests
import os

# API endpoint to fetch data for 10 users
API_URL = "https://randomuser.me/api/?results=10"

# Fetch data from the API
result = requests.get(API_URL)
if result.status_code != 200:
    print("Error: Couldn't get data from the API.")
    exit()

# Parse the JSON response
data = result.json()
users = data.get("results", [])

# Ensure a directory for storing images
output_dir = "python_files/photos"
os.makedirs(output_dir, exist_ok=True)

# Process each user
for person in users:
    # Extract the user's details
    first_name = person["name"]["first"]
    last_name = person["name"]["last"]
    image_url = person["picture"]["medium"]
    
    # Dynamic filename
    file_name = f"{first_name} {last_name}.jpg"
    file_path = os.path.join(output_dir, file_name)

    # Download and save the profile picture
    image_response = requests.get(image_url)
    if image_response.status_code == 200:
        with open(file_path, "wb") as image_file:
            image_file.write(image_response.content)
        print(f"Saved: {file_path}")
    else:
        print(f"Error: Couldn't download image for {first_name} {last_name}.")
```

</details>