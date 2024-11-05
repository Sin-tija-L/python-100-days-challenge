# 👉 Day 83 Challenge: Custom Themes for Your Blog! 🎨🖌️

Today’s challenge is all about adding a splash of style to your blog! We’re going to implement custom themes, so users can personalize their experience. Ready to get creative? Let’s go! 🚀

### 📝 Challenge Instructions

1. **Retrieve Your Blog Code from Day 77**  
   - Start by grabbing the code you wrote on Day 77, including your HTML template file.

2. **Set Up Theme Customization**  
   - Use `GET` requests to detect a `theme` variable. When a theme name is passed in the URL, your app should apply that specific theme to the blog page.

3. **Create Multiple Themes**  
   - Design at least **two visually distinct themes**:
     - Each theme should differ in at least one primary color.
     - Feel free to get creative — experiment with fonts, layouts, or backgrounds if you're inspired!

4. **Default Theme**  
   - If no `theme` variable is provided, the blog should load a **default theme**.

### ✨ Pro Tip: Personalize It!
Give each theme a unique vibe! Perhaps one theme is calming and professional, while the other is bold and playful. The goal is to make your blog feel customizable and engaging. 🌈

---

Enjoy adding a touch of customization to your blog, and see how each theme changes the feel of your content!

<img id="image" src="assets/day83_1.png" alt="day83 image" width="960">

<img id="image" src="assets/day83_2.png" alt="day83 image" width="960">

<img id="image" src="assets/day83_3.png" alt="day83 image" width="960">

<img id="image" src="assets/day83_4.png" alt="day83 image" width="960">

---

## Solution (No Peeking!)


<details>
<summary>👀 Answer</summary>

👉 **day82.py**

```python
from flask import Flask, render_template, redirect, url_for, request
from datetime import datetime

app = Flask(__name__)

# Template for blog entries with theme support
@app.route('/blog1')
def blog1():
    theme = request.args.get('theme', 'default')  # Get the theme from URL, default if none
    return render_template(
        'blog_template.html',
        heading="Celebrating Latvia's Birthday - A Nation's Journey",
        date=datetime.now().strftime("%Y-%m-%d"),
        content="""
        On November 18th, Latvia proudly celebrated its 105th birthday, marking a significant milestone in the nation's history. This Baltic gem has a rich and vibrant culture, and its journey from independence to occupation and back to sovereignty is a testament to the resilience of its people.

        In this blog post, we delve into Latvia's fascinating history, exploring its cultural heritage, traditions, and the struggles it has overcome. From the beautiful landscapes of the Latvian countryside to the bustling streets of Riga, we'll take you on a virtual journey to this enchanting nation.

        Join us as we raise a toast to Latvia's enduring spirit and celebrate its remarkable 105 years of independence.
        """,
        theme=theme
    )

@app.route('/blog2')
def blog2():
    theme = request.args.get('theme', 'default')  # Get the theme from URL, default if none
    return render_template(
        'blog_template.html',
        heading="Python: The Swiss Army Knife of Programming Languages",
        date=datetime.now().strftime("%Y-%m-%d"),
        content="""
        Python, often referred to as the "Swiss Army Knife" of programming languages, has become an indispensable tool for developers and data scientists worldwide. Its simplicity, versatility, and an extensive library ecosystem make it a powerhouse in the modern tech landscape.

        In this blog post, we dive into the world of Python, exploring its origins, growth, and practical applications. Whether you're a beginner looking to learn your first programming language or a seasoned developer seeking a powerful tool for web development, data analysis, or machine learning, Python has got you covered.

        Join us as we unravel the mysteries of Python and discover why it has earned a place as one of the most popular and beloved programming languages on the planet.
        """,
        theme=theme
    )

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
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ heading }}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles/themes.css') }}">
</head>
<body class="{{ theme }}-theme">
    <h1>{{ heading }}</h1>
    <p><strong>Date:</strong> {{ date }}</p>
    <p>{{ content }}</p>
</body>
</html>
```

👉 **themes.css**

```python
/* Default theme */
body.default-theme {
    background-color: #f7f7f7;
    color: #333;
    font-family: Arial, sans-serif;
}

h1.default-theme {
    color: #4a90e2;  /* Soft blue accent for headings */
}

p.default-theme {
    line-height: 1.6;
}

/* Dark theme */
body.dark-theme {
    background-color: #1e1e1e;
    color: #e0e0e0;
    font-family: 'Courier New', Courier, monospace;
}

h1.dark-theme {
    color: #ffa500;  /* Bright orange accent for headings */
}

p.dark-theme {
    line-height: 1.8;
}

/* Nature theme */
body.nature-theme {
    background-color: #e8f5e9;  /* Light green */
    color: #2e7d32;
    font-family: 'Georgia', serif;
}

h1.nature-theme {
    color: #388e3c;  /* Darker green for a nature-inspired look */
    border-bottom: 2px solid #81c784;  /* Subtle underline for style */
    padding-bottom: 5px;
}

p.nature-theme {
    line-height: 1.5;
}

/* Sunset theme */
body.sunset-theme {
    background-color: #ffecd2;  /* Soft peach */
    color: #d84315;
    font-family: 'Lucida Sans', sans-serif;
}

h1.sunset-theme {
    color: #ff6f61;  /* Warm red-orange for headings */
}

p.sunset-theme {
    line-height: 1.7;
}

/* Ocean theme */
body.ocean-theme {
    background-color: #e0f7fa;  /* Light aqua */
    color: #00796b;
    font-family: 'Verdana', sans-serif;
}

h1.ocean-theme {
    color: #004d40;  /* Deep teal for ocean feel */
}

p.ocean-theme {
    line-height: 1.5;
}
```

</details>

