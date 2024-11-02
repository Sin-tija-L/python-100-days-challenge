# 👉 Day 77: Too. Much. Code. Let's Tidy it Up! 🎨🧹

### Challenge Instructions (Run in VSCode)

As you may have noticed, your Flask files can get long very quickly. No one wants a massive block of code in a single file – it's hard to read, navigate, and maintain. Today, we’ll learn how to **organize** our code using **templating** and **redirecting** to keep everything clean and manageable. Let's streamline! 🌈✨

ℹ️ You already was doing this which is great!!! But now here comes a bit more explanation to it!

---

### 🛠️ Getting Started: Basic Flask Code

Here’s some simple Flask code to get us started. This example sends a custom greeting to the page:

```python
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
  myName = "Alise"
  page = f"""Hi {myName}"""
  return page

app.run(host='0.0.0.0', port=81)
```

This code works for small projects, but as the HTML grows, it’s best to separate the HTML, CSS, and any assets into organized folders. Let’s break it down!

---

### 🌟 Step-by-Step: Moving HTML to Templates and Organizing CSS

**Step 1: Set Up Your Project Structure**
1. Create a `templates` folder in your project directory (where `day77.py` is).
2. Inside `templates`, create an HTML file called `portfolio.html`.
3. Move any HTML code for your portfolio page into `portfolio.html`.

**Step 2: Organize CSS and Static Files**
1. Create a `static` folder in your project directory.
2. Inside `static`, create a `styles` folder.
3. Create a file named `style.css` in the `styles` folder and add the CSS for your portfolio page there.
4. Update `portfolio.html` to link to this CSS file by adding this line in the `<head>` section:

```python
<link href="{{ url_for('static', filename='css/style.css') }}" rel="stylesheet" type="text/css" />
```

**Step 3: Update Image Paths**
Make sure all your images, icons, and other assets are in the correct location within `static`. Update any paths in `portfolio.html` to use the `static` folder structure, for example:

```python
<img src="{{ url_for('static', filename='images/myPicture.png') }}" alt="Portfolio Image">
```

---

### 🧑‍💻 Updating Your Flask Code to Use Templates

Now, let’s adjust our Flask code to render the new `portfolio.html` template. In `day77.py`, update your route to look like this:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    myName = "Alise"
    return render_template('portfolio.html', myName=myName)  # Pass `myName` to the template

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)
```

# 👉 Adding More Pages in Flask – Expanding Our Web App! 🌐✨

Ready to add more pages to your Flask app? Let’s create a new **Home page** alongside the main route so you can expand your site with style! 🌟

---

### Step 1: Define Multiple Routes

👉 Here’s how to create an additional route, `/home`, that serves a different HTML page:

1. **Set up the main Flask route (`/`)** to display a greeting.
2. **Create a new route (`/home`)** that serves a custom HTML page about the world of “Baldies.”

### Code Example

👉 In `home77.html` import html that you used in `home76.html`

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')  # Root route for main page
def index():
    return 'Hello from Flask! 👋'

@app.route('/home')  # Path to our new Home page 🌟
def home():
    return render_template('home77.html')  # Render the HTML template

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)
```

**Try it out!**

---

## Customizing Your Portfolio Page with `render_template` and Jinja2 🌟

Today, we’re enhancing our Flask portfolio by using `render_template` with Jinja2 placeholders. This allows us to create a dynamic, personalized page without manually reading and replacing strings. Let's get started! 🚀

---

### 1. Setting Up `portfolio.html` with Jinja2 Placeholders

In the `templates` folder, create `portfolio.html` and add Jinja2 placeholders using `{{ }}` for each dynamic element.

```python
<!DOCTYPE html>
<html>
<head>
    <title>Portfolio</title>
</head>
<body>
    <h1>{{ name }}'s Portfolio</h1>
    <h2>{{ title }}</h2>
    <p>{{ text }}</p>
    <img src="{{ url_for('static', filename='images/' + image) }}" width="500px">
</body>
</html>
```

- Replace `{name}`, `{title}`, `{text}`, `{link}`, and `{image}` with `{{ name }}`, `{{ title }}`, `{{ text }}`, `{{ link }}`, and `{{ image }}`.
- Flask will fill in these placeholders when using `render_template`.

---

### 2. Updating Flask Code to Use `render_template`

In day77.py, use `render_template` to pass variables to `portfolio.html`:

```python
from flask import Flask, render_template  # Import render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Variables to pass to the template
    myName = "Alise"
    title = "Day 56 Solution"
    text = "Day 56 was all about using CSV reading, file and folder manipulation to create 100 files in dozens of folders based on streaming song names!"
    image = "56.png"
    
    # Use render_template to render the HTML with variables
    return render_template(
        'portfolio.html',
        name=myName,
        title=title,
        text=text,
        image=image
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)
```

### 🚀 Benefits of Using `render_template`
- Cleaner Code: No need for manually opening, reading, and replacing strings.
- Dynamic Pages: Easily pass variables to make pages dynamic.
- Maintainability: Your HTML is easier to read and manage with Jinja2 syntax.

--- 

### 🌟 Adding More Routes

Easily add more routes using the same `portfolio.html` template. Here’s an example for "Day 56":

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/56')
def fiftySix():
    myName = "Alise"
    title = "Day 56 Solution"
    text = "Day 56 was all about using CSV reading, file and folder manipulation to create 100 files in dozens of folders based on streaming song names!"
    image = "56.png"
    
    # Use render_template to render the HTML with variables
    return render_template(
        'portfolio.html',
        name=myName,
        title=title,
        text=text,
        image=image
    )

# Continue adding routes for other days or projects!

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)
```

**Try it out!**

--- 


## 👉 Redirecting with Flask 🚀

Redirecting is a powerful tool in Flask, allowing you to send users to another web address with just a short, custom route. It's perfect for when you want to create short, memorable links that forward users to longer, complex URLs.

---

### Why Use Redirects?

Sometimes, URLs can be lengthy or difficult to remember. With redirects, you can create your own **link shortener** using simple routes in Flask! For example, you could set up `/77` to redirect to a specific page, saving users from typing out a long URL.

### Setting Up Redirects in Flask

1. **Add an Import for `redirect`**  
   To enable redirecting, import `redirect` along with Flask at the top of your `day77.py` file:

   ```python
   from flask import Flask, redirect
   ```

2. **Create an App Route for the Redirect**

   Use `redirect()` inside a route function to send users to your desired URL. Here’s how:

   ```python
   from flask import Flask, redirect

   app = Flask(__name__)

   @app.route('/ai-tools')
   def aiTools():
        # Redirects the user to the SheCanDoIT AI tools from 2023 challenge
        return redirect("https://www.shecandoit.lv/ai-advent")

   if __name__ == '__main__':
       app.run(host='0.0.0.0', port=81, debug=True)
   ```

   - This sets up `/ai-tools` to redirect anyone who visits it to SheCanDoIT AI tools from 2023 challenge.
   - `return redirect("URL")` takes the user directly to the specified URL.

---

### 🌟 Why This is Awesome

With this simple setup, you've created your own link shortener! 🎉 Now, anyone who visits `http://127.0.0.1:81/ai-tools` will be forwarded to the specified long URL. This is great for:
- **Sharing**: Make it easier for users to reach important pages.
- **Memorable Links**: Use short, easy-to-remember URLs.
- **Control**: Redirect users to external content without changing your own URL structure.

---

### Try it Out! 🌐

Add a few more redirects to different routes for practice, and watch as your app transforms into a sleek, custom link shortener! 🚀

--- 

## Common Errors
 
 First, delete any other code in your `day77` files. Copy each code snippet below into `day77` files by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.


### Common Error 1

👉 What's the problem here?

 ```python
@app.route('/ai-tools')
   def aiTools():
    redirect("https://www.shecandoit.lv/ai-advent")
```

<details>
<summary>👀 Answer</summary>

I've missed the `return` before `redirect` which will create a TypeError.

```python
@app.route('/ai-tools')
   def aiTools():
        return redirect("https://www.shecandoit.lv/ai-advent")
```

</details>

---

### Common Error 2

👉 What's the problem here?

 ```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/56')
def fifty_six():
    myname = "Alise"
    title = "Day 56 Solution"
    Text = "Day 56 was all about using CSV reading, file and folder manipulation to create 100 files in dozens of folders based on streaming song names!" 
    image = "56.PNG"
    
    return render_template(
        'portfolio.html',
        name=myname,
        title=title,
        text=Text
    )

if __name__ == 'main':
    app.run(host='127.0.0.1', port=80)
```

<details>
<summary>👀 Answer</summary>

I've missed url_for function to generate path

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/56')
def fiftySix(): # Inconsistent naming conventions
    myName = "Alise" # Variable name inconsistency (different case)
    title = "Day 56 Solution"
    text = "Day 56 was all about using CSV reading, file and folder manipulation to create 100 files in dozens of folders based on streaming song names!" # Wrong variable name case
    image = "56.png"  # Different file extension case might cause issues in some environments
    
    # Missing key in render_template
    return render_template(
        'portfolio.html',
        name=myName,
        title=title,
        text=text,
        image=image # Missing the image variable
    )

if __name__ == '__main__': # Mistake in conditional syntax
    app.run(host='0.0.0.0', port=81, debug=True)  # Port change may cause permission issues
```

</details>

---

## Fix My Code

👉 Try and fix this code which is *full* of errors.

First, delete any other code in your `day77` files. Copy each code snippet below into `day77` files by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.


```python
from flask import Flask, redirect, render_template

   app = Flask(__name__)

   @app.route('/56')
def fifty_Six():  
    myname = "Alise" 
    title = "Day 56 Solution"
    text = "Day 56 was all about using CSV reading, file and folder manipulation to create 100 files in dozens of folders based on streaming song names!"
    image = "56.PNG"
    
    # Use render_template to render the HTML with variables
    return render_template(
        'portfolio.html',
        name=myName,  # Misspelled variable name (`myName` instead of `myname`)
        title=title,
        text=text,
        image=image
    )

   @app.route('/ai-tools')
   def ai_Tools():
        return redirect("https://www.shecandoit.lv/ai-advent")

   if __name__ == 'main':
       app.run(host='0.0.0.0', port="81")
```

<details>
<summary>👀 Answer</summary>

```python
from flask import Flask, redirect # Unused import (render_template, should be used)

   app = Flask(__name__)   # Incorrect indentation; will cause SyntaxError

   @app.route('/56')
def fiftySix(): # Inconsistent function naming convention (camelCase instead of snake_case)
    myName = "Alise" # Inconsistent variable naming (lowercase here, camelCase elsewhere)
    title = "Day 56 Solution"
    text = "Day 56 was all about using CSV reading, file and folder manipulation to create 100 files in dozens of folders based on streaming song names!"
    image = "56.png"  # Different case for file extension
    
    return render_template(
        'portfolio.html',
        name=myName,
        title=title,
        text=text,
        image=image
    )

   @app.route('/ai-tools')
   def aiTools():  # Inconsistent function naming convention
        return redirect("https://www.shecandoit.lv/ai-advent")  # Missing HTTP method specification

   if __name__ == '__main__':  # Syntax error: incorrect main check
       app.run(host='0.0.0.0', port=81, debug=True)  # Port number should be an integer, not a string
```

</details>


# 👉 Day 77 Challenge

## Objective
Today's challenge is to set up a simple template for a blog using Flask.

## Requirements

1. **Create a Blog Template**

   Your blog template should include:
   - A **heading** section for the title of the blog post.
   - A **date** section to display the current date.
   - A **content** section for the main text of the blog post.

2. **Add Blog Entries**

   - Write **two different blog entries**.
   - Each entry should be served on a **separate endpoint**.

3. **Implement URL Shortening**

   - Set up **shortened URLs** for each blog entry using redirects.
   - Ensure both entries use the **same template** for a consistent look and feel.

## Task Summary

- **Template**: Design a reusable HTML template with placeholders for the heading, date, and content.
- **Endpoints**: Set up individual routes for each blog entry.
- **Shortened URLs**: Add shorter, more accessible URLs that redirect to each blog entry's route.

Good luck, and happy coding!


## Solution (No Peeking!)


<details>
<summary>👀 Answer</summary>

---

👉 **day77.py**

```python
from flask import Flask, render_template, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Template for blog entries
@app.route('/blog1')
def blog1():
    return render_template('blog_template.html', 
                           heading="Celebrating Latvia's Birthday - A Nation's Journey", 
                           date=datetime.now().strftime("%Y-%m-%d"), 
                           content="""
                           On November 18th, Latvia proudly celebrated its 105th birthday, marking a significant milestone in the nation's history. This Baltic gem has a rich and vibrant culture, and its journey from independence to occupation and back to sovereignty is a testament to the resilience of its people.

    In this blog post, we delve into Latvia's fascinating history, exploring its cultural heritage, traditions, and the struggles it has overcome. From the beautiful landscapes of the Latvian countryside to the bustling streets of Riga, we'll take you on a virtual journey to this enchanting nation.

    Join us as we raise a toast to Latvia's enduring spirit and celebrate its remarkable 105 years of independence.
                           """)

@app.route('/blog2')
def blog2():
    return render_template('blog_template.html', 
                           heading="Python: The Swiss Army Knife of Programming Languages", 
                           date=datetime.now().strftime("%Y-%m-%d"), 
                           content="""
                           Python, often referred to as the "Swiss Army Knife" of programming languages, has become an indispensable tool for developers and data scientists worldwide. Its simplicity, versatility, and an extensive library ecosystem make it a powerhouse in the modern tech landscape.

    In this blog post, we dive into the world of Python, exploring its origins, growth, and practical applications. Whether you're a beginner looking to learn your first programming language or a seasoned developer seeking a powerful tool for web development, data analysis, or machine learning, Python has got you covered.

    Join us as we unravel the mysteries of Python and discover why it has earned a place as one of the most popular and beloved programming languages on the planet.
                           """)

# Shortened redirects
@app.route('/first-post')
def first_post():
    return redirect(url_for('blog1'))

@app.route('/second-post')
def second_post():
    return redirect(url_for('blog2'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)
```

👉 **blog_template.html**

```python
<html>
    <head><title>{{ title }}</title></head>
    <body>
        <h1>{{ heading }}</h1>
        <p><strong>Date:</strong> {{ date }}</p>
        <p>{{ content }}</p>
    </body>
</html>
```

</details>