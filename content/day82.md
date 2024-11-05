
# 🚀 Day 82: Don't Stop 'Til You Get It! 🎉

Today, let's explore an alternative method for fetching data from forms on the webserver — introducing the `GET` method!

So far, we've been using `POST`, which essentially packages all the form data and sends it over to the server. In this scenario, the form dictates *when* data is sent.

With `GET`, it's the webserver that requests data from the form, saying: "Give me that data!" You might have already seen `GET` in action if you've noticed a URL with a `?` followed by a mix of `=` and `&` symbols — that’s data being sent via `GET`.

### Challenge Instructions (Run in VSCode)

---

## 🌟 What's the Difference? 

Great question! 💡

### **POST Method**
- With `POST`, data in the form isn't visible in the URL. Once sent, it’s like it disappears — so no bookmarking or sharing.
- Trying to share that link to your shopping cart? 🎁 It won’t work with `POST` data since each user gets a unique view.

### **GET Method**
- `GET` encodes the data right in the URL, so it can be bookmarked and shared, preserving the data context in the page!

---

## 🚀 Let's Add Some Code!

Open VSCode and enter the following code into your Flask application to see how `GET` works:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return 'Hello from Flask 🚀'

app.run(host='0.0.0.0', port=81, debug=True)
```

When you run this, you’ll see it works seamlessly with `GET`. However, if you try the same thing with `POST` (without the right configuration), you'll encounter an error.

---

## 🛠 Importing `request`

Next, let's import `request` and modify the response to show any arguments provided in the URL:

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return request.args  # This returns any arguments in the URL

app.run(host='0.0.0.0', port=81, debug=True)
```

When you view the page, you’ll see an empty dictionary initially (`{}`) since no arguments are in the URL.

---

## 🌐 Adding Variables in the URL

👉 Open the page in your browser and add variables to the URL like this:

```python
http://localhost:81/?name=Grace&field=IT
```

Hit enter and observe how the data appears! You're constructing a dictionary in the URL — pretty cool, right?

---

## 💪 Personalization Time!

Let's add some personalization. Here, we’re recognizing contributions of women in IT. Set up your code like this:

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    get = request.args
    if get.get("name", "").lower() == "ada":
        return "Hello, Ada Lovelace! 👩‍💻 Thank you for paving the way in programming!"
    elif get.get("name", "").lower() == "grace":
        return "Hello, Grace Hopper! 🐱 Your contributions to computing are legendary!"
    return "No data provided 🎯"

app.run(host='0.0.0.0', port=81, debug=True)
```

Now, entering:

```python
http://localhost:81/?name=Grace
```

…will greet you with a message celebrating Grace Hopper’s achievements! If no name is provided, it defaults to `"No data provided 🎯"`.

---

## 🔒 Should I Use `POST` or `GET`?

- **`POST`** is the better choice for secure or sensitive information (like usernames and passwords), as it can be encrypted when sent over `https`.
- **`GET`** is perfect for settings or location data that you might want to bookmark or share.

**Try it out in VSCode**, and watch how these methods handle data differently!

---

## Fix My Code

👉 Try and fix this code which is *full* of errors.

First, delete any other code in your `day82` files. Copy each code snippet below into `day82` files by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.


```python
from flask import request

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    if data.get("name", "").lower() == "ada":
        return "Hello, Ada Lovelace! 👩‍💻 Thank you for paving the way in programming!"
    elif get.get("name", "").lower() == "grace":
        return "Hello, Grace Hopper! 🐱 Your contributions to computing are legendary!"

app.run(host='0.0.0.0', port=81, debug=True)
```

<details>
<summary>👀 Answer</summary>

```python
from flask import Flask, request # Didn't import Flask

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    get = request.args # Didn't request the args and assign to a variable
    if get.get("name", "").lower() == "ada": # Wrong variable name used
        return "Hello, Ada Lovelace! 👩‍💻 Thank you for paving the way in programming!"
    elif get.get("name", "").lower() == "grace":
        return "Hello, Grace Hopper! 🐱 Your contributions to computing are legendary!"
    return "No data provided 🎯" # No return for if the page is empty

app.run(host='0.0.0.0', port=81, debug=True)
```

</details>

---

# 👉 Day 82 Challenge: Let's Go Bilingual! 🌍💬

Today's challenge is all about language inclusivity! Get ready to add a bilingual twist to your page using `GET` variables and URL checks. 🌐

### 📝 Challenge Instructions

1. **Create Your Default Page**  
   - Start with a page in **English** that loads by default when accessing your website.

2. **Add a Language-Specific URL**  
   - Set up a unique **/language** ending for the URL that allows users to switch between languages.

3. **Duplicate and Translate**  
   - Duplicate your page and use a translation tool (hello, Google Translate! 🌐) to make a version in another language of your choice.

4. **Detect Language with GET Variables**  
   - Use the `GET` variable to check the URL and determine which language page to display:
     - If the URL ends in **/english**, display the English version.
     - If it ends in **/otherLanguage**, show the translated version instead.

### ✨ Pro Tip: Personalize It!
Add a welcoming message in each language to make users feel at home! The goal is to provide a seamless bilingual experience. 🌍

--- 

Test it out, and see how smoothly you can switch between languages!

<img id="image" src="assets/day82_1.png" alt="day82 image" width="960">

<img id="image" src="assets/day82_2.png" alt="day82 image" width="960">

<img id="image" src="assets/day82_3.png" alt="day82 image" width="960">

<img id="image" src="assets/day82_4.png" alt="day82 image" width="960">

---

## Solution (No Peeking!)

<details>
<summary>👀 Answer</summary>

---

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/language', methods=["GET"])
def language():
    lang = request.args.get('lang')
    if lang:
        if lang.lower() == "en":
            return "Hello Alise"
        elif lang.lower() == "lv":
            return "Čau Alise"
        elif lang.lower() == "ua":
            return "Привіт Аліса"
        elif lang.lower() == "jp":
            return "こんにちは、アリス"
    return "Unknown language"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81, debug=True)
```

</details>