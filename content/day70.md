# 👉 Day 70: For Your Eyes Only


**We are back to the good stuff again!**

Sometimes, we need to store sensitive information in our code, like passwords, that we don't want others to see.

When using VSCode, we can handle this by keeping such information outside of our code files. One common method is to store sensitive data in environment variables.

👉 In VSCode, you can create a `.env` file to store your secrets. This file should not be included in version control (e.g., Git). Add the `.env` file to your `.gitignore` file to keep it private. You can use a package like `python-dotenv` to load these variables into your Python script.

<img id="image" src="assets/day70_1.png" alt="day70 image" width="960">

<img id="image" src="assets/day70_2.png" alt="day70 image" width="960">


👉 In VSCode, environment variables are similar to dictionaries in that they have keys used to access values. Let’s set up an environment variable for a password.

<img id="image" src="assets/day70_3.png" alt="day70 image" width="960">

### 👉 This days challenge should be run from Terminal

👉 Now let's use our environment variable to set up a very simple login system.

1. Install `python-dotenv` to load the environment variables into your Python script:

```python
pip install python-dotenv OR USE python3 -m pip install python-dotenv
```

2. Now adjust the code:

```python
import os
from dotenv import load_dotenv

# Provide the explicit path to the .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '../python-dotenv/.env')
load_dotenv(dotenv_path=dotenv_path)

password = os.getenv('PASSWORD', '')

userPass = input("Password > ")

if userPass == password:
    print("Well done")
else:
    print("Better luck next time")
```

The environment variables stored in the .env file are not shared when the project is pushed to version control or shared with others, so your sensitive data remains protected.


## Common Errors
 
 First, delete any other code in your `day70.py` file. Copy each code snippet below into `day70.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.


👉 Why am I am not let in?

 ```python
import os
from dotenv import load_dotenv

# Provide the explicit path to the .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '../python-dotenv/.env')
load_dotenv(dotenv_path=dotenv_path)

password = os.getenv('SECRET')

userPass = input("Password > ")

if userPass == password:
    print("Well done")
else:
    print("Better luck next time")
```

<details>
<summary>👀 Answer</summary>

Nothing wrong with your code here. You just haven't created a secret called 'SECRET'.

</details>


## Fix My Code

👉 Try and fix this code which is *full* of errors.

First, delete any other code in your `day70.py` file. Copy each code snippet below into `day70.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

```python
from dotenv import load_dotenv

# Provide the explicit path to the .env file
dotenv_path = path.join(os.path.dirname(__file__), '../python-dotenv/.env')
load_dotenv(dotenv_path=dotenv_path)

password = getenv('SECRET')

userPass = input("Password > ")

if userPass == password:
    print("Well done")
else:
print("Better luck next time")
```

<details>
<summary>👀 Answer</summary>

```python
import os # No import
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '../python-dotenv/.env') #Missed the os before path join
load_dotenv(dotenv_path=dotenv_path)

password = os.getenv('SECRET') #Missed the os before getenv

userPass = input("Password > ")

if userPass == password:
    print("Well done")
else:
    print("Better luck next time") # Indent error, just to keep you on your toes!
```

</details>


## 👉 Day 70 Challenge: Master the Login System!


Today, you're building a powerful login system that separates the rulers from the commoners! 🏰

⚙️ Your mission:

1. **Create two user types**: 
   - The all-seeing, all-knowing **admin** 🛡️
   - And the regular, hard-working **normie** 👥
   
2. **Unique credentials**: Each user type must have their own username and password—no cheating! 🙅‍♀️

3. **Special greetings**: 
   - When **admin** logs in, they get the royal treatment with a grand "Hello admin" 👑
   - But when a **normie** signs in, they're welcomed with a simple "Hello normie" 🙌

🔧 **Example:**

- **Admin logs in**: "Hello admin"
- **Normie logs in**: "Hello normie"

---

Ready to conquer the login system challenge and put users in their rightful place? Let’s go! 💻✨


<img id="image" src="assets/day70_4.png" alt="day70 image" width="960">

<details>
<summary>💡 Hints</summary>

- Pass the user input into the 'newImage' variable.
- Use `try... except` to load the image or generate the error.

</details>


## Solution (No Peeking!)


<details>
<summary>👀 Answer</summary>

```python
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '../python-dotenv/.env')
load_dotenv(dotenv_path=dotenv_path)

print("🌟Login System🌟")
print()

while True:
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if username == os.getenv('adminUsername') and password == os.getenv('adminPassword'):
        print("Welcome Admin")
        break
    elif username == os.getenv('username') and password == os.getenv('password'):
        print("Welcome Normy")
        break
    else:
        print("Try again")
```

</details>