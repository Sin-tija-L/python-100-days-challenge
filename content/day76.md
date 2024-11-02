# 👉 Day 76: Flask in VSCode! 🚀🐍

### Challenge Instructions (Run in VSCode)

Ready to take HTML & CSS to the next level? Today, we’re adding **Python** to the mix with **Flask**! 🎉

**Flask** allows us to build a mini web server that runs continuously, serving up custom web pages that adapt to each user’s actions. This means we’re no longer limited to static HTML & CSS – we’re stepping into the world of **dynamic web apps**! 🔄✨

Why run Flask in **VSCode**? Great question! Running Flask here lets us:
1. 👀 View real-time logs, so we can watch what’s happening with our server as it responds to requests.
2. 🛠 Debug and test directly in VSCode, making the development process super smooth and interactive.
3. 🌐 Access the app locally (and even share with others on your network if you want!).

---

## How Is Flask Code Different?

👉 Let's dig into the boilerplate code that you get when you start a Flask repl. Read the comments for explanations:

```python
from flask import Flask # Imports the flask library

app = Flask(__name__) # Starts the Flask application. The 'app' variable is very important. We'll be using that later.


@app.route('/') # Tells the code what to do if we've gone to our web address with just a / after the URL
def index(): # Tells the code which webpage to show. This subroutine will display the 'Hello from Flask' page
    return 'Hello from Flask!'


app.run(host='0.0.0.0', port=81) # This line should ALWAYS come last. It's the line that turns on the Flask server.
```

Once running, Flask will display a local web address. Paste that link into your browser, and voilà! 🎉 You’ll be able to interact with your app in real-time.

<img id="image" src="assets/day76_1.png" alt="day76 image" width="960">

ℹ️ Whenever you make changes now, refreshing the page won't update it. You need to stop and run the program to view any changes.

With Flask, you’re creating your own mini internet 🕸️ where you can serve up content, react to user input, and make each page unique. The best part? You get to choose whether to keep it private or share it with the world! 🌍🔐

Ready to make some magic? 🪄 Let’s get coding with Flask in VSCode! 💻🚀

---

### ✨ Adding More Pages in Flask - Let’s Make It Happen! 🎉

Ready to expand your Flask app? Today, we’re creating an additional page – a whole new layer to your web experience! 🌐

👉 Here’s how we’ll add a “Home” page to our Flask app. Just add the following code to your project, and watch it work its magic!

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')  # Root route, the first page users see
def index():
    return 'Hello from Flask! 👋'

@app.route('/home')  # Path to our new Home page 🌟
def home():
    return render_template('home76.html')  # Render the HTML template

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)
```

### 👉 And your home76.html

```python
<!DOCTYPE html>
<html>
<head>
    <title>These ladies know how to code! 🚀</title>
</head>
<body>
    <h1>These ladies know how to code! 🚀</h1>
    <h2>Welcome to our website!</h2>

    <p>We all know that throughout history, some of the greatest minds in IT have been women. Let’s celebrate the brilliance and impact they have had on the tech world.</p>

    <h2>Let's meet IT professions!</h2>
    <img src="{{ url_for('static', filename='images/shecandoit.png') }}" alt="Day 76 project image">
    <p><a href="https://www.shecandoit.lv/profesijas-un-lomas">Here you can meet IT professions</a></p>

    <h2>Here are three facts about women in IT:</h2>
    <ul>
        <li>Ada Lovelace was the first computer programmer.</li>
        <li>Women pioneered software development during World War II.</li>
        <li>Women make up only 26% of the tech workforce today.</li>
    </ul>

    <p><a href="page2.html">Go to page 2 ➡️</a></p>
</body>
</html>
```

✨ Pro Tip: After running your Flask app, go to **http://127.0.0.1:81/home** in your browser to see your new “Home” page come to life!

---

### Images With Flask

To get images with Flask, we have to:
1. Create a folder in the `python_files`. By default, it's called `static`.
2. Upload any files you want your webpages to access - images, audio, video etc. (You can create subfolder structures in the static folder to help you stay organized).

I've added an 'images' subfolder and uploaded my SheCanDoIT image to there.

<img id="image" src="assets/day76_2.png" alt="day76 image" width="960">

Now I've updated the `<a href>` tag to reference the 'static' folder:

```python
<img src="{{ url_for('static', filename='images/shecandoit.png') }}" alt="Day 76 project image">
```

**Try it out!**

---

## fStrings With Flask

Using **fStrings** in Flask lets you easily format dynamic content right inside your HTML. This is great for adding personalized or up-to-date info to your pages, like today’s date or custom messages.

### Example: Display Today’s Date on the Homepage

👉 Here’s how we can add today’s date to a Flask app
1. **Set up the date** inside the `home` function and assign to a variable.
2. Use **Jinja2** syntax (`{{ }}`) in the HTML file to specify where the variable should appear.
3. Pass the variable from your Flask route to the template using `render_template`.

Here's the code with comments to show the changes.

```python
from flask import Flask, render_template
import datetime


app = Flask(__name__)

@app.route('/')  # Root route, the first page users see
def index():
    return 'Hello from Flask! 👋'

@app.route('/home')
def home():
    today = datetime.date.today()  # Get today's date
    return render_template('home76.html', today=today)  # Pass `today` to the template

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)
```

👉 home76.html

```python
<!DOCTYPE html>
<html>
<head>
    <title>These ladies know how to code! 🚀</title>
</head>
<body>
    <h1>These ladies know how to code! 🚀</h1>
    <h2>Welcome to our website!</h2>
    <h2>{{ today }}</h2> <!-- This is where Flask will insert the date -->

    <p>We all know that throughout history, some of the greatest minds in IT have been women. Let’s celebrate the brilliance and impact they have had on the tech world.</p>

    <h2>Let's meet IT professions!</h2>
    <img src="{{ url_for('static', filename='images/shecandoit.png') }}" alt="Day 76 project image">
    <p><a href="https://www.shecandoit.lv/profesijas-un-lomas">Here you can meet IT professions</a></p>

    <h2>Here are three facts about women in IT:</h2>
    <ul>
        <li>Ada Lovelace - First computer programmer</li>
        <li>Grace Hopper - Developed first compiler</li>
        <li>Margaret Hamilton - NASA software pioneer</li>
    </ul>

    <p><a href="page2.html">Go to page 2 ➡️</a></p>
</body>
</html>
```

---

### Linking With Flask

👉 Here’s how to add a link from the `index` page to the `home` page in Flask. We’ll use the `url_for` function to generate the correct URL for the `home` route, keeping things flexible and avoiding hardcoding URLs.

1. **day76.html** (Landing page with a link to `/home`)

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Welcome to Flask!</title>
</head>
<body>
    <h1>Hello from Flask! 👋</h1>
    <p>Welcome to the index page. Click below to visit the home page:</p>
    <p><a href="{{ url_for('home') }}">Go to Home Page ➡️</a></p> <!-- Link to home page -->
</body>
</html>
```

2. **home76.html** (The target page for the link)

```python
<!DOCTYPE html>
<html>
<head>
    <title>These ladies know how to code! 🚀</title>
</head>
<body>
    <h1>These ladies know how to code! 🚀</h1>
    <h2>Welcome to our website!</h2>
    <h2>{{ today }}</h2>

    <p>We all know that throughout history, some of the greatest minds in IT have been women. Let’s celebrate the brilliance and impact they have had on the tech world.</p>

    <h2>Let's meet IT professions!</h2>
    <img src="{{ url_for('static', filename='images/shecandoit.png') }}" alt="Day 76 project image">
    <p><a href="https://www.shecandoit.lv/profesijas-un-lomas">Here you can meet IT professions</a></p>

    <h2>Here are three facts about women in IT:</h2>
    <ul>
        <li>Ada Lovelace - First computer programmer</li>
        <li>Grace Hopper - Developed first compiler</li>
        <li>Margaret Hamilton - NASA software pioneer</li>
    </ul>

    <p><a href="page2.html">Go to page 2 ➡️</a></p>
    <p><a href="{{ url_for('index') }}">Back to Index</a></p> <!-- Link back to index -->

</body>
</html>
```

3. Set up the routes for both the `index` and `home` pages and use `render_template` to serve the HTML files.

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('day76.html')  # Render day76.html for the root route

@app.route('/home')
def home():
    return render_template('home76.html')  # Render home76.html for the /home route

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)
```

**Try it out!**


## Common Errors
 
 First, delete any other code in your `day76` files. Copy each code snippet below into `day76` files by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.


### Copy, Paste and EDIT

👉 What's the problem here?

 ```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('day76.html') 

@app.route('/home')
def index():
    return render_template('home76.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)
```

<details>
<summary>👀 Answer</summary>

I've copied the code from `@app.route('/')` to create `@app.route('/home')`, but I now have two **functions called index**. This is what is creating the error. We can't have two functions with the same name.

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('day76.html')

@app.route('/home')
def home():
    return render_template('home76.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)
```

</details>


### Directionless

👉 What's the problem here?

 ```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Welcome to Flask!</title>
</head>
<body>
    <h1>Hello from Flask! 👋</h1>
    <p>Welcome to the index page. Click below to visit the home page:</p>
    <p><a href="/'home'">Go to Home Page ➡️</a></p>
</body>
</html>
```

<details>
<summary>👀 Answer</summary>

I've missed url_for function to generate path

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Welcome to Flask!</title>
</head>
<body>
    <h1>Hello from Flask! 👋</h1>
    <p>Welcome to the index page. Click below to visit the home page:</p>
    <p><a href="{{ url_for('home') }}">Go to Home Page ➡️</a></p>
</body>
</html>
```

</details>

---

## Fix My Code

👉 Try and fix this code which is *full* of errors.

First, delete any other code in your `day76` files. Copy each code snippet below into `day76` files by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

1. **day76.html**

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Welcome to Flask!</title>
</head>
<body>
    <h1>Hello from Flask! 👋</h1>
    <p>Welcome to the index page. Click below to visit the home page:</p>
    <p><a href="/'home'">Go to Home Page ➡️</a></p>
</body>
</html>
```

2. **home76.html** 

```python
<!DOCTYPE html>
<html>
<head>
    <title>These ladies know how to code! 🚀</title>
</head>
<body>
    <h1>These ladies know how to code! 🚀</h1>
    <h2>Welcome to our website!</h2>
    <h2>{{ today }}</h2>

    <p>We all know that throughout history, some of the greatest minds in IT have been women. Let’s celebrate the brilliance and impact they have had on the tech world.</p>

    <h2>Let's meet IT professions!</h2>
    <img src="{{ url_for('static', filename='images/shecandoit.png') }}" alt="Day 76 project image">
    <p><a href="https://www.shecandoit.lv/profesijas-un-lomas">Here you can meet IT professions</a></p>

    <h2>Here are three facts about women in IT:</h2>
    <ul>
        <li>Ada Lovelace - First computer programmer</li>
        <li>Grace Hopper - Developed first compiler</li>
        <li>Margaret Hamilton - NASA software pioneer</li>
    </ul>

    <p><a href="page2.html">Go to page 2 ➡️</a></p>
    <p><a href="/'index'">Back to Index</a></p>

</body>
</html>
```

3. **day76.py** 

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('day76.html')

@app.route('/home')
def index():
    return render_template('home76.html')
```

<details>
<summary>👀 Answer</summary>

1. **day76.html**

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Welcome to Flask!</title>
</head>
<body>
    <h1>Hello from Flask! 👋</h1>
    <p>Welcome to the index page. Click below to visit the home page:</p>
    <p><a href="{{ url_for('home') }}">Go to Home Page ➡️</a></p> <!-- Missed url_for function to generate path -->
</body>
</html>
```

2. **home76.html**

```python
<!DOCTYPE html>
<html>
<head>
    <title>These ladies know how to code! 🚀</title>
</head>
<body>
    <h1>These ladies know how to code! 🚀</h1>
    <h2>Welcome to our website!</h2>
    <h2>{{ today }}</h2>

    <p>We all know that throughout history, some of the greatest minds in IT have been women. Let’s celebrate the brilliance and impact they have had on the tech world.</p>

    <h2>Let's meet IT professions!</h2>
    <img src="{{ url_for('static', filename='images/shecandoit.png') }}" alt="Day 76 project image">
    <p><a href="https://www.shecandoit.lv/profesijas-un-lomas">Here you can meet IT professions</a></p>

    <h2>Here are three facts about women in IT:</h2>
    <ul>
        <li>Ada Lovelace - First computer programmer</li>
        <li>Grace Hopper - Developed first compiler</li>
        <li>Margaret Hamilton - NASA software pioneer</li>
    </ul>

    <p><a href="page2.html">Go to page 2 ➡️</a></p>
    <p><a href="{{ url_for('index') }}">Back to Index</a></p> <!-- Missed url_for function to generate path -->

</body>
</html>
```

3. **day76.py**

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('day76.html') 

@app.route('/home')
def home(): #Two subroutines with the same name. 
    return render_template('home76.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True) # Missed the run command
```

</details>


# 🌟 Day 76 Challenge: Create Your Own Web Space with Flask! 💻✨

Ladies, it's time to take your coding journey to the next level! Today, we're diving into the world of Flask to create a personal web server that highlights your skills and connects the digital dots of your professional presence. 🌐💼

---

👉 Here’s what you’ll be building today:

1. **/portfolio** – A page dedicated to your amazing projects. Think of this as your personal showcase – all the awesome work you’ve done in one spot. Share your coding achievements, link to your GitHub projects, and let the world know how talented you are. 🌟

2. **/linktree** – A page where people can easily find all your social and professional profiles. It's your **Linktree-style page**, with links to your Twitter, LinkedIn, GitHub, or any other profiles you want to highlight. This page makes it easy for anyone to stay connected with you across platforms! 🌐

### 💪 Your Mission:

- **Step 1**: Set up a **Flask web server**.
- **Step 2**: Create two unique endpoints:
  - `/portfolio` for your **project showcase**.
  - `/linktree` for your **social media and professional links**.
- **Step 3**: Add some style, personality, and flair! 🦋 This is YOUR space, so make it fun, creative, and **100% you**.

### 💡 Why This is Awesome:

This challenge helps you:
- Learn how to create **multiple pages** using Flask.
- Build a **personal portfolio** that you can actually use in the future.
- Create a **central hub** for your social and professional profiles to share with potential employers, collaborators, or your community. 🔗

---

### Example:

- **Portfolio Page**:
  Show off your best work! Add links to your GitHub repos, describe your projects, and highlight what makes them special.
  
- **Linktree Page**:
  Gather all your social profiles in one place so people can easily find and follow you. Whether it’s Twitter, LinkedIn, or your personal blog – it’s all about making YOU accessible and visible in the tech space.

---

This is more than just a coding challenge – it's a step toward building your **professional online presence**. So, let's get creative, have fun, and **make something that shows the world who you are!** 💖🚀


<details>
<summary>💡 Hints</summary>

### Inspiration Resources

- Make sure you have a 'static' folder for all of your media and CSS files.
- You may need to rename one CSS file to avoid having two with the same name.
- Use what you already have! Take html from `day74` and `day75` challenge!

</details>


## Solution (No Peeking!)


<details>
<summary>👀 Answer</summary>

👉 day76.py

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('day76.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/linktree')
def linktree():
    return render_template('linktree.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)
```

👉 HTML and CSS look in my day74 and day75 challenge solutions!

</details>