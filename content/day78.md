
# 🚀 Day 78 Challenge: Build a Personal Reflection Log with Flask

Welcome to Day 78! Today, you’ll create a personalized reflection journal to log your thoughts and insights for the next 22 days of coding. By the end of this challenge, you'll have a beautifully designed, URL-based journal to revisit!

---

### Challenge Instructions (Run in VSCode)

## 🛠️ Challenge Overview

In this challenge, you’ll:
1. **Build a Flask app** to host your reflection log.
2. **Create dynamic routes** to show reflections based on the day number.
3. **Add CSS** to style each page and make it visually appealing.

You’ll be using URL parameters to display content for each day!

---

## 🌐 Code Example

Here's a dynamic route in Flask that lets you input any day number at the end of the URL. The number will be displayed as part of the content on the page.

```python
from flask import Flask, render_template

app = Flask(__name__)

# Define a dynamic route to capture the day number
@app.route('/<int:dayNumber>')
def reflection(dayNumber):
    return render_template("day.html", dayNumber=dayNumber)
```

In this setup:
- The route `/<int:dayNumber>` captures any number you add to the URL (e.g., `http://127.0.0.1:81/78`) and passes it as `dayNumber`.
- `dayNumber` is then displayed on the page using an HTML template.

---

## 📝 Your Reflection Page Should Include

1. **Day Title**: Display the day number in a heading.
2. **Reflection Text**: Add your daily notes, experiences, or lessons learned.
3. **Screenshot of Result**: Add a placeholder or section for an image showing a screenshot of the result for that day's work.

> **Tip:** Use HTML templates with Flask to keep your structure organized and separate content from code.

---

## 🖌️ Adding CSS Styling

To enhance the look and feel of your reflection pages, add some CSS styles.

1. **Create a CSS file** in a folder called `static` (Flask will recognize it automatically).
2. **Link your CSS** in your HTML template file.

Example template (`days.html`):

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Reflection for Day {{ dayNumber }}</title>
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='day.css') }}">
</head>
<body>
    <h1>Reflection for Day {{ dayNumber }}</h1>
    <p>Here’s where you can write your notes and thoughts for Day {{ dayNumber }}.</p>
    
    <!-- Screenshot Section -->
    <h2>Screenshot of Result</h2>
    <img src="{{ url_for('static', filename='images/day{{ dayNumber }}_screenshot.png') }}" alt="Screenshot for Day {{ dayNumber }}" style="max-width:100%;">
</body>
</html>
```

### Sample CSS (`days.css`)

```python
body {
    font-family: Arial, sans-serif;
    max-width: 600px;
    margin: 0 auto;
    line-height: 1.6;
}
h1 {
    color: #333;
}
img {
    border: 1px solid #ccc;
    padding: 5px;
    margin-top: 10px;
}
```

In the above HTML, the screenshot for each day should be saved in the `static/images` folder with a filename format like `day1_screenshot.png`, `day2_screenshot.png`, etc.

---

## 🎯 Challenge Recap

- **Dynamic Route**: `/dayNumber` for each day’s reflection.
- **Styled Page**: CSS for visual appeal.
- **Reflection Content**: Personal notes and a screenshot of your work.

---

Enjoy building your reflection log! 🎉

---

## Solution (No Peeking!)


<details>
<summary>👀 Answer</summary>

### day78.py file

```python
from flask import Flask, render_template

app = Flask(__name__)

# Blog entries with image paths instead of links
blog_entries = {
    "10": {
        "title": "DAY 10 from 100 day of Python challenge",
        "text": """
        This was the first task in the Python challenge where you had to do a little bit of math. 
        To be precise, you had to know how to calculate percentages. 
        """,
        "image": "day10_screenshot.png"
    },
    "49": {
        "title": "DAY 49 from 100 day of Python challenge",
        "text": """
        On day 49, I learned how to manage files in my project.
        """,
        "image": "day49_screenshot.png"
    }
}

@app.route('/<pageNumber>')
def index(pageNumber):
    if pageNumber in blog_entries:
        entry = blog_entries[pageNumber]
        return render_template("days.html", title=entry["title"], text=entry["text"], image=entry["image"])
    else:
        return f"This is page {pageNumber}"

app.run(host='0.0.0.0', port=81)
```

### HTML file

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles/days.css') }}">
</head>
<body>
    <div class="container">
        <h1>{{ title }}</h1>
        <p>{{ text }}</p>
        
        <!-- Image placeholder -->
        <h2>Screenshot of Result</h2>
        <img src="{{ url_for('static', filename='images/' + image) }}" alt="Screenshot for {{ title }}">
    </div>
</body>
</html>
```

### CSS file

```python
/* General body styling */
body {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    background-color: #f0f4f8;
    color: #333;
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    margin: 0;
    padding: 20px;
}

/* Container styling */
.container {
    background-color: #ffffff;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    padding: 40px;
    max-width: 800px;
    text-align: center;
}

/* Title styling */
h1 {
    color: #007acc;
    font-size: 2.5em;
    margin-bottom: 10px;
    text-transform: uppercase;
    letter-spacing: 1.5px;
}

/* Paragraph styling */
p {
    font-size: 1.2em;
    line-height: 1.8;
    margin: 20px 0;
    color: #555;
}

/* Subtitle for screenshot section */
h2 {
    color: #333;
    font-size: 1.8em;
    margin-top: 30px;
    text-transform: uppercase;
    letter-spacing: 1px;
    border-bottom: 2px solid #007acc;
    display: inline-block;
    padding-bottom: 5px;
}

/* Image styling */
img {
    border: 1px solid #ddd;
    border-radius: 8px;
    margin-top: 20px;
    max-width: 100%;
    height: auto;
    transition: transform 0.3s ease;
}

/* Hover effect on image */
img:hover {
    transform: scale(1.05);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

/* Add subtle hover effect for the container */
.container:hover {
    box-shadow: 0 8px 16px rgba(0, 122, 204, 0.2);
}
```

</details>