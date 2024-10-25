# 👉 Day 75 Challenge: Create Your Own Link Tree Website 🌐✨

As the great Jon Bon Jovi almost sang:

> 🎶 *“Wooooahhh, we’re three quarters of the way there…”* 🎶

Alright, alright – a bit cheesy, but congrats on reaching **Day 75**! You’re well on your way, and today’s reward is a project day to create something personal and powerful: **Your very own link tree website!**

---

## 🎯 Why a Link Tree?

A **link tree site** is like a compact portfolio. It’s a single page that displays links to your:
- **Social media profiles**
- **Project examples**
- **Anything else you’re proud of**!

With a link tree, you can keep just one URL in your social profiles, and updating your links becomes super easy. This single link is all you’ll need to keep your audience connected to your best work and online presence.

---

## 💡 Link Tree Requirements

Your link tree website should include:

1. **A Picture of You** 📸
   - Start with an image that represents you at the top of the page. It can be a professional photo or something fun!

2. **Your Name & Social Media Handles** 📝
   - Let people know who you are with your name and, if you want, a short intro.
   - Add links to your social media profiles or handles.

3. **Headings with Links to Your Work** 🖇️
   - Include a series of links (mid-sized headings) that direct people to:
     - Examples of your work
     - Profiles or pages you’re active on
     - Anything else you want to share with the world!


## Example

<img id="image" src="assets/day75_1.png" alt="day75 image" width="960">

---

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