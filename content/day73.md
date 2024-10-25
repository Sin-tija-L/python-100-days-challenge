
# 👉 Day 73: Hyper Text Markup Language (HTML)

### Challenge Instructions (Run in VSCode)

In this challenge, we will be taking a crash course in **HTML** (Hyper Text Markup Language). We'll create a simple webpage using HTML tags, headings, paragraphs, images, lists, and links. To run this code locally in VSCode, we will also use **Flask** to serve the HTML.
About **Flask** in more details we are going to talk on **day 76**!

---

### 💻 Setup Instructions

Before we begin, you need to install **Flask** to run the HTML files using Python:

1. **Install Flask**:
   Open the terminal in VSCode and run the following command to install Flask:
   
   ```python
   pip install Flask 

   or

   pip3 install Flask
   ```

2. **Use a Python File**:
   In VSCode, use a Python file (e.g., `day73.py`) to serve the HTML page using Flask.

3. **Create HTML Files**:
   Create an HTML file (e.g., `day73.html`) in a folder named `templates` for Flask to find it.

---

### 🔧 Code to Run in VSCode

**Flask Python Code (day73.py)**:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('day73.html')

if __name__ == '__main__':
    app.run(debug=True)
```

---

### HTML Basics

Over the next couple of days, we'll be taking a crash course in **HTML**. HTML is a **markup language** that is used to tell browsers how to render elements on a webpage (i.e., how they should appear). HTML is made up of a series of instructions in `<tags>` that surround text, images, etc., and define how they should be displayed.

<img id="image" src="assets/day73_1.png" alt="day73 image" width="960">


---

### 🚀 Start Creating a Webpage: Basic HTML Structure

👉 **Step 1**: The **first** and **last** tags in any HTML file are the `<html>` tags. These indicate the start and end of an HTML document.

```python
<html>

</html>
```

---

### 💡 Head Section

The `<head>` tag contains metadata (invisible information) about the page. The most important tag for now is the `<title>`, which defines the text that will appear in the tab of the webpage.

```python
<html>
  <head>
    <title>These ladies know how to code! 🚀</title>
  </head>
</html>
```

---

### 🖼️ Body Section

The `<body>` tag contains all the visible content on the page, such as text, headings, images, and more.

```python
<html>
  <head>
    <title>These ladies know how to code! 🚀</title>
  </head>
  <body>
  
  </body>
</html>
```

---

### 📝 Headings

The `<h>` tags create headings, with `<h1>` being the largest and `<h6>` being the smallest. Let's add some headings to our page:

```python
<body>
  <h1>These ladies know how to code! 🚀</h1>
  <h2>Welcome to our website!</h2>
</body>
```

---

### 📜 Paragraphs

The `<p>` tag creates paragraphs of text:

```python
<body>
  <h1>These ladies know how to code! 🚀</h1>
  <p>We all know that throughout history, some of the greatest minds in IT have been women. Let’s celebrate the brilliance and impact they have had on the tech world.</p>
</body>
```

---

### 🖼️ Images

To insert an image, use the `<img>` tag with the `src` attribute pointing to the image file location. Also, define the width of the image in percentages or pixels.

1. **Upload your image to the project folder**.

<img id="image" src="assets/day73_2.png" alt="day73 image" width="960">

2. Add the image using the following HTML code:

```python
<body>
  <h1>These ladies know how to code! 🚀</h1>
  <p>Lets go to the work! 💼 </p>
  <img src="{{ url_for('static', filename='images/1.png') }}" width="30%">
</body>
```

---

### 📋 Lists

Use the `<ul>` tag for unordered (bullet-point) lists, and `<ol>` for ordered (numbered) lists. Each item in the list is enclosed in `<li>` tags.

```python
<body>
  <h2>Here are three facts about women in IT:</h2>
  <ul>
    <li>Ada Lovelace was the first computer programmer.</li>
    <li>Women pioneered software development during World War II.</li>
    <li>Women make up only 26% of the tech workforce today.</li>
  </ul>
</body>
```

---

### 🔗 Links

To link between pages, use the `<a>` tag with the `href` attribute pointing to the URL or file location.

```python
<body>
  <h1>These ladies know how to code! 🚀</h1>
  <p><a href="https://www.example.com">Click here to learn more!</a></p>
</body>
```

---

### 🏁 Running the Code in VSCode

1. **Run the Flask App**:
   After writing the `day73.py` file and the HTML file in the `templates` folder, open the terminal in VSCode and run the Python app:

   ```python
   python3 python_files/day73.py
   ```

2. **Open the Webpage**:
   - Flask will run the server at `http://127.0.0.1:5000/`.
   - Open this URL in your browser to see your HTML page in action.

---

### 🏆 Summary

You've just created a basic HTML webpage that includes headings, paragraphs, images, lists, and links, and served it locally using Flask in VSCode. You're on your way to mastering web development!



## Common Errors
 
 First, delete any other code in your `day73.py` file. Copy each code snippet below into `day73.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.


### Broken Links

👉 What's the problem here?

 ```python
<p><a href = "www.shecandoit.lv/profesijas-un-lomas">Here you can meet IT professions</a></p>
```

<details>
<summary>👀 Answer</summary>

We didn't include the https part of the URL in the link.

```python
<p><a href = "https://www.shecandoit.lv/profesijas-un-lomas">Here you can meet IT professions</a></p>
```

</details>


### No Image

👉 What's the problem here?

 ```python
<img src="{{ url_for('static', filename='images/1') }}" width="30%">
<p>Lets go to the work! 💼 </p>
```

<details>
<summary>👀 Answer</summary>

We forgot the file extension.

```python
<img src="{{ url_for('static', filename='images/1.png') }}" width="30%">
<p>Lets go to the work! 💼 </p>
```

</details>


### A Massive Problem

👉 What's the problem here?

 ```python
<h1>These ladies know how to code! 🚀
Welcome to our website!
<p>We all know that throughout history, some of the greatest minds in IT have been women. Let’s celebrate the brilliance and impact they have had on the tech world.</p>
<h2>Some ladies in the tech world</h2>
<p>Here are some of the legends of the tech world.</p>
```

<details>
<summary>👀 Answer</summary>

Because we forgot to close the `<h1>` tag, the rest of the page gets treated as headings.

```python
<h1>These ladies know how to code! 🚀 </h1>
<h2>Welcome to our website! </h2>
<p>We all know that throughout history, some of the greatest minds in IT have been women. Let’s celebrate the brilliance and impact they have had on the tech world.</p>
<h2>Some ladies in the tech world</h2>
<p>Here are some of the legends of the tech world.</p>
```

</details>


## Fix My Code

👉 Try and fix this code which is *full* of errors.

First, delete any other code in your `day73.py` file. Copy each code snippet below into `day73.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

```python
  <head>
    <title>These ladies know how to code! 🚀</title>
  </head>


  <body>
  <h1>These ladies know how to code! 🚀
  <h2>Welcome to our website!</h2>

  <p>We all know that throughout history, some of the greatest minds in IT have been women. Let’s celebrate the brilliance and impact they have had on the tech world.</p>

  <h2>Lets go to the work!</h2>

  <img src="{{ url_for('static', filename='images/1') }}" width="30%">
  <p><a href = "www.shecandoit.lv/profesijas-un-lomas">Here you can meet IT professions</a></p>

  <h2>Here are three facts about women in IT:</h2>
  <ul>
    <li>Ada Lovelace was the first computer programmer.</li>
    <li>Women pioneered software development during World War II.</li>
    <li>Women make up only 26% of the tech workforce today.</li>
  </ul>

  <p><a href = "page2.html">Go to page 2</a></p>
  
</body>
```

<details>
<summary>👀 Answer</summary>

```python
<head>
  <title>These ladies know how to code! 🚀</title>
</head>

<body>
  <!-- Mistake 1: Missing closing tag for <h1> -->
  <h1>These ladies know how to code! 🚀</h1>

  <h2>Welcome to our website!</h2>

  <p>We all know that throughout history, some of the greatest minds in IT have been women. Let’s celebrate the brilliance and impact they have had on the tech world.</p>

  <h2>Let's go to the work!</h2>
  
  <!-- Mistake 2: Missing file extension (.jpg, .png, etc.) for the image -->
  <img src="{{ url_for('static', filename='images/1.png') }}" width="30%">
  
  <!-- Mistake 3: Missing 'http://' or 'https://' in the URL -->
  <p><a href="https://www.shecandoit.lv/profesijas-un-lomas">Here you can meet IT professions</a></p>

  <h2>Here are three facts about women in IT:</h2>
  
  <ul>
    <li>Ada Lovelace was the first computer programmer.</li>
    <li>Women pioneered software development during World War II.</li>
    <li>Women make up only 26% of the tech workforce today.</li>
  </ul>

  <!-- Mistake 4: Ensure correct file path for 'page2.html' if it is in another folder or remove it -->
  <p><a href="page2.html">Go to page 2</a></p>

</body>
```

</details>


# 👉 Day 73 Challenge: Build Your Web Portfolio

Today’s challenge is to create a web portfolio to showcase your coding projects. You'll build a simple webpage that highlights **5 of your best projects** from the past 72 days. This portfolio will serve as a platform to display your skills and link directly to your Replit projects.

---

### 💡 Portfolio Requirements:

1. **Title**: Create a webpage with the title **"My Portfolio"**.
2. **Heading**: Add a heading that displays **"Your Name - Portfolio"**.
3. **Project Showcase**:
   - Select **5 of your best projects** from the previous 72 days.
   - For each project, include:
     - A second-level heading (`<h2>`) with the **project name** or **Day number**.
     - A paragraph (`<p>`) with a short **description** of the project.
     - An image (`<img>`) of the project’s Replit page (you can use screenshots or preview images).
     - Each image should be **clickable** and linked directly to the Replit project.

---

### 💻 Example Webpage Structure:

1. **Title**: "My Portfolio"
2. **Heading**: "Your Name - Portfolio"
3. **Projects**:
   - Each project will have a heading, a description, an image, and a link to the live Replit project page.


<details>
<summary>💡 Hints</summary>

- Use an `<a>` tag around the `<img>` tag to create the linked image.

</details>


## Solution (No Peeking!)


<details>
<summary>👀 Answer</summary>

```python
<!DOCTYPE html>
<html>
  <head>
    <title>Alises Portfolio</title>
  </head>

  <body>
    <h1>Alises Portfolio</h1>

    <h2>Day 72!</h2>
    <p>This is Alises secret diary and you can access it only with right credentials.</p>
    <a href="https://replit.com/@aalisiite/Day72100Days?v=1">
      <img src="{{ url_for('static', filename='images/day72.png') }}" width="30%">
    </a>

    <h2>Day 10!</h2>
    <p>This was the first task in Python challenge where you had to do a little bit of math. To be precise, you had to know how to calculate %.</p>
    <a href="https://replit.com/@aalisiite/day10?v=1">
      <img src="{{ url_for('static', filename='images/day10.png') }}" width="30%">
    </a>

    <h2>Day 24!</h2>
    <p>In this day I had to write a program that rolls a dice.</p>
    <a href="https://replit.com/@aalisiite/day24?v=1">
      <img src="{{ url_for('static', filename='images/day24.png') }}" width="30%">
    </a>

    <h2>Day 49!</h2>
    <p>In day 49 I learned how to manage files in my project.</p>
    <a href="https://replit.com/@aalisiite/day49?v=1">
      <img src="{{ url_for('static', filename='images/day49.png') }}" width="30%">
    </a>

    <h2>Day 60!</h2>
    <p>This day taught me about date and time management.</p>
    <a href="https://replit.com/@aalisiite/day60?v=1">
      <img src="{{ url_for('static', filename='images/day60.png') }}" width="30%">
    </a>

  </body>
</html>
```

</details>