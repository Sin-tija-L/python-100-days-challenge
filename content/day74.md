# 👉 Day 74: CSS - Make Your Webpage Shine! 🎨✨

### Challenge Instructions (Run in VSCode)

So far, our webpages have been pretty basic - white background, black text, default fonts, etc. Today, we're going to take them to the next level using **Cascading Style Sheets (CSS)** to make our pages visually engaging and unique!

CSS allows us to create reusable styles that can be applied across the webpage. Think of it as giving your webpage its own personality and charm! 🌟

---

### 🌐 Setting Up in VSCode

Make sure you have a project structure like this:

```python
python_files/
├── day74.py              # Flask application to serve HTML
├── static/
│   └── styles/
│       └── day74.css     # CSS file for styling
├── templates/
│   └── day74.html        # HTML file for content
```

1. **Create Flask Application (day74.py)**:

   ```python
   from flask import Flask, render_template, url_for

   app = Flask(__name__)

   @app.route('/')
   def index():
       return render_template('day74.html')

   if __name__ == '__main__':
       app.run(debug=True)
   ```

2. **Linking the CSS File in HTML**:

   Inside your HTML, link to your CSS file with:
   ```python
   <link href="{{ url_for('static', filename='styles/day74.css') }}" rel="stylesheet" type="text/css" />
   ```

---

### 🖼️ Creating the HTML Page (templates/day74.html)

   ```python
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="utf-8">
       <meta name="viewport" content="width=device-width">
       <title>Your HTML and CSS</title>
       <link href="{{ url_for('static', filename='styles/day74.css') }}" rel="stylesheet" type="text/css" />
   </head>
   <body>
       <h1>Women in IT - Page 2</h1>
       <p>The continuation of our website highlighting influential women in technology who have shaped the field.</p>
       <h2>Ada Lovelace</h2>
       <img src="{{ url_for('static', filename='images/adaLovelace.png') }}" width="200px">
       <p class="blurb">Ada Lovelace, often considered the first computer programmer, made groundbreaking contributions to computing in the 19th century, envisioning algorithms that could be processed by machines.</p>
   </body>
   </html>
   ```

---

### 🎨 Styling Elements in CSS (static/styles/day74.css)

**1. Setting Up Basic Styling**:

Set the entire `<html>` and `<body>` sections to cover the page fully:

```python
html, body {
  height: 100%;
  width: 100%;
  background-color: #e4e2e2;
}
```

---

**2. Styling Headings**:

Let's make our headings stand out! CSS styles here will apply to all `<h1>` tags in the HTML.

```python
h1 {
  font-family: sans-serif;
  font-size: 24px;
  color: blue;
  background-color: #d3d345;
  text-align: center;
  padding: 10px;
}
```

Similarly, you can style the `<h2>` tag:

```python
h2 {
  font-family: sans-serif;
  font-size: 18px;
  color: blue;
  background-color: #d3d345;
  text-align: center;
}
```

---

**3. Paragraph Style**:

CSS can make your paragraphs look uniform and visually appealing. Use this to style all `<p>` tags on the page:

```python
p {
  font-family: monospace;
  font-size: 14px;
  color: blue;
  text-align: center;
}
```

---

**4. Background Color**:

To set a background color for the entire page, include it in the `html, body` style:

```python
html, body {
  height: 100%;
  width: 100%;
  background-color: #e4e2e2;
}
```

---

**5. Aligning Elements**:

Center-align text for specific tags. Here’s how to center both `<h1>` and `<p>` tags:

```python
h1, p {
  text-align: center;
}
```

---

**6. Combining Styles**:

To apply the same styles to both `<h1>` and `<h2>` tags, separate the selectors with a comma:

```python
h1, h2 {
  font-family: sans-serif;
  font-size: 24px;
  color: blue;
  background-color: #d3d345;
  text-align: center;
}
```

If you want `<h2>` to be a bit smaller, add a separate style afterward:

```python
h2 {
  font-size: 18px;
}
```

---

**7. Image Styling**:

To center an image, set it as a block element and apply automatic margins:

```python
img {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 50%;
}
```

---

**8. Class Styling**:

You can style individual elements by adding a class to them. Here’s an example of adding the `blurb` class to a `<p>` tag in HTML:

```python
<p class="blurb">Ada Lovelace, often considered the first computer programmer, made groundbreaking contributions to computing in the 19th century, envisioning algorithms that could be processed by machines.</p>
```

Then, style the `.blurb` class in CSS:

```python
.blurb {
  font-style: italic;
  font-weight: bold;
}
```

---

### 🚀 Running the Code in VSCode

1. **Run Flask**:
   In the terminal, navigate to your project folder and start the Flask app:

   ```python
   python3 python_files/day74.py
   ```

2. **Open in Browser**:
   Go to `http://127.0.0.1:5000/` in your browser to see your CSS-styled webpage.


👉 This is how your webpage should look like:

<img id="image" src="assets/day74_1.png" alt="day74 image" width="960">

---

### 🌟 Customization Tips

- **Experiment!**: Play with colors, fonts, and layouts to see what works best.
- **Use Classes for Unique Elements**: Custom styles using classes give you more control.
- **Image Adjustments**: Resize and align images for a polished look.
- **Learn More on CSS**: [CSS Introduction](https://www.w3schools.com/css/css_intro.asp)

---

This guide gives you a solid foundation for making visually appealing websites with CSS. Let your creativity shine! 🌈 **Happy styling!**

---


## Common Errors
 
 First, delete any other code in your `day74.py` file. Copy each code snippet below into `day74.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.


### Common Problem 1

👉 What's the problem here?

 ```python
p{
  font-family: monospace;
  font-size: 10px
  color: blue
   text-align:center;
    
}
```

<details>
<summary>👀 Answer</summary>

We missed some semi colons from the end of lines.

```python
p{
  font-family: monospace;
  font-size: 10px;
  color: blue;
   text-align:center;
    
}
```

</details>


### Common Problem 2

👉 What's the problem here?

 ```python
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>Your HTML and CSS</title>
</head>
```

<details>
<summary>👀 Answer</summary>

We forgot the file extension.

```python
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>Your HTML and CSS</title>
  <link href="{{ url_for('static', filename='styles/day74.css') }}" rel="stylesheet" type="text/css" />
</head>
```

Solution 2 is to have a `style` tag in the head of the html page that contains all the css needed. This isn't ideal though, because then you can't share your CSS across multiple pages.

</details>

---

## Fix My Code

👉 Try and fix this code which is *full* of errors.

First, delete any other code in your `day74` files. Copy each code snippet below into `day74` files by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

### HTML File

```python
  <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>Your HTML and CSS</title>
</head>
<body>
    <h1>Women in IT - Page 2</h1>
    <p>The continuation of our website highlighting influential women in technology who have shaped the field.</p>
    <h2>Ada Lovelace</h2>
    <img src="{{ url_for('static', filename='images/adaLovelace.png') }}" width="200px">
    <p class="blurb">Ada Lovelace, often considered the first computer programmer, made groundbreaking contributions to computing in the 19th century, envisioning algorithms that could be processed by machines.</p>
</body>
</html>
```

### CSS File

```python
html, body {
  height: 100%;
  width: 100%;
  background-color: #e4e2e2;
}

h1, h2{
  font-family: sans-serif;
  font-size: 24px
  color: blue
  background-color: #d3d345;
  text-align:center;
    
}

h2{
  font-size: 12px;
  
}

p{
  font-family: monospace;
  font-size: 10px;
  color: blue;
   text-align:center;
    
}

{
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 50%;
  
}

.blurb{
  font-style: italic;
  font-weight: bold;
}
```

<details>
<summary>👀 Answer</summary>

### HTML File

```python
  <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>Your HTML and CSS</title>
    <link href="{{ url_for('static', filename='styles/day74.css') }}" rel="stylesheet" type="text/css" />  ## Missing link to style sheet
</head>
<body>
    <h1>Women in IT - Page 2</h1>
    <p>The continuation of our website highlighting influential women in technology who have shaped the field.</p>
    <h2>Ada Lovelace</h2>
    <img src="{{ url_for('static', filename='images/adaLovelace.png') }}" width="200px">
    <p class="blurb">Ada Lovelace, often considered the first computer programmer, made groundbreaking contributions to computing in the 19th century, envisioning algorithms that could be processed by machines.</p>
</body>
</html>
```

### CSS File

```python
html, body {
  height: 100%;
  width: 100%;
  background-color: #e4e2e2;
}

h1, h2{
  font-family: sans-serif;
  font-size: 24px; ## Missing semi colon
  color: blue; ## Missing semi colon
  background-color: #d3d345;
  text-align:center;
    
}

h2{
  font-size: 12px;
  
}

p{
  font-family: monospace;
  font-size: 10px;
  color: blue;
  text-align:center;
    
}

img{ ## No style name
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 50%;
  
}

.blurb{
  font-style: italic;
  font-weight: bold;
}
```

</details>


# 👉 Day 74 Challenge: Style Up Your Webpage! 🎨✨

Today’s challenge is all about **taking your CSS skills further** and transforming yesterday's code into something beautiful and unique! Let’s add depth, spacing, and flair to make your page look polished and professional.

---

### 💡 Challenge Instructions

1. **Build on Yesterday's Code**:
   - Use yesterday's webpage as your starting point.

2. **Make It Stunning!** 🌟:
   - Experiment with **CSS properties** like:
     - **Box shadows** for depth.
     - **Padding** and **margins** for spacing.
     - **Borders** to create sections or define areas.
     - **Hover effects** to add interactivity.
     - **Transitions** for smooth animations.

3. **Explore New CSS Tricks**:
   - Research new CSS ideas that you haven’t tried yet. Here are a few suggestions:
     - **Rounded corners** with `border-radius`.
     - **Text shadows** to make headings pop.
     - **Gradients** as backgrounds.
     - **CSS Flexbox or Grid** for layout structure.

---

### 🚀 Tips for an Engaging Design

- **Experiment with Colors** 🎨: Try new color schemes that contrast well and make elements stand out.
- **Add Spacing and Structure** 🧱: Use padding and margins to give breathing space to elements and make the layout look clean.
- **Use Hover Effects** 🎯: Create feedback when users hover over buttons, links, or images.
- **Personalize Your Page** 🌈: Let your style shine! Use unique fonts, images, and layouts to make the page truly yours.

---

The goal of today’s challenge is to make your page look polished, engaging, and truly **one-of-a-kind**. This is your canvas, so go all out! **Happy styling!** 🎉


<details>
<summary>💡 Hints</summary>

### Inspiration Resources

If you’re looking for design inspiration, here are a few helpful CSS resources:
- **[CSS Tricks](https://css-tricks.com/)**: Tips, guides, and ideas for all things CSS.
- **[CodePen](https://codepen.io/)**: Browse CSS design examples and find inspiration.
- **[W3Schools CSS Reference](https://www.w3schools.com/cssref/)**: Explore all CSS properties and their effects.

</details>


## Solution (No Peeking!)


<details>
<summary>👀 Answer</summary>


### HTML file

```python
<!DOCTYPE html>
<html>
  <head>
    <title>Alises Portfolio</title>
    <link href="{{ url_for('static', filename='styles/portfolio.css') }}" rel="stylesheet" type="text/css" />
  </head>

  <body>
    <div class="container">
      <h1>Alises Portfolio</h1>

      <!-- Project 1 -->
      <div class="project">
        <h2>Day 72!</h2>
        <p>This is Alises secret diary, and you can access it only with the right credentials.</p>
        <a href="https://replit.com/@aalisiite/Day72100Days?v=1">
          <img src="{{ url_for('static', filename='images/day72.png') }}" alt="Day 72 project image">
        </a>
      </div>

      <!-- Project 2 -->
      <div class="project">
        <h2>Day 10!</h2>
        <p>This was the first task in the Python challenge, where you had to do a bit of math to calculate %.</p>
        <a href="https://replit.com/@aalisiite/day10?v=1">
          <img src="{{ url_for('static', filename='images/day10.png') }}" alt="Day 10 project image">
        </a>
      </div>

      <!-- Project 3 -->
      <div class="project">
        <h2>Day 24!</h2>
        <p>On this day, I had to write a program that rolls a dice.</p>
        <a href="https://replit.com/@aalisiite/day24?v=1">
          <img src="{{ url_for('static', filename='images/day24.png') }}" alt="Day 24 project image">
        </a>
      </div>

      <!-- Project 4 -->
      <div class="project">
        <h2>Day 49!</h2>
        <p>On day 49, I learned how to manage files within my project.</p>
        <a href="https://replit.com/@aalisiite/day49?v=1">
          <img src="{{ url_for('static', filename='images/day49.png') }}" alt="Day 49 project image">
        </a>
      </div>

      <!-- Project 5 -->
      <div class="project">
        <h2>Day 60!</h2>
        <p>This day taught me about date and time management in Python.</p>
        <a href="https://replit.com/@aalisiite/day60?v=1">
          <img src="{{ url_for('static', filename='images/day60.png') }}" alt="Day 60 project image">
        </a>
      </div>
    </div>
  </body>
</html>
```

### CSS file

```python
/* Page styling */
body {
    font-family: Arial, sans-serif;
    background-color: #f9f9f9;
    color: #333;
    margin: 0;
    padding: 20px;
  }
  
  /* Main title styling */
  h1 {
    font-size: 36px;
    text-align: center;
    color: #2c3e50;
    margin-bottom: 30px;
  }
  
  /* Section heading styling */
  h2 {
    font-size: 24px;
    color: #2980b9;
    margin-top: 40px;
  }
  
  /* Paragraph styling */
  p {
    font-size: 16px;
    color: #555;
    line-height: 1.6;
  }
  
  /* Image styling */
  img {
    width: 100%;
    max-width: 300px;
    border-radius: 8px;
    transition: transform 0.3s ease;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  }
  
  /* Hover effect for images */
  img:hover {
    transform: scale(1.05);
  }
  
  /* Link styling */
  a {
    text-decoration: none;
    color: inherit;
  }
  
  /* Container styling */
  .container {
    max-width: 800px;
    margin: auto;
  }
  
  /* Project box styling */
  .project {
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 20px;
    margin-bottom: 20px;
    transition: box-shadow 0.3s ease;
  }
  
  /* Hover effect for project containers */
  .project:hover {
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
  }
```

</details>