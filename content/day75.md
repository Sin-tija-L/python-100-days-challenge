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
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ url_for('static', filename='styles/day75.css') }}">
    <title>Alise's Link Tree</title>
</head>
<body>
    <div class="container">
        <!-- Profile Section -->
        <div class="header">
            <img src="{{ url_for('static', filename='images/myPicture.png') }}" alt="Alise Alka's Profile Picture" class="profile-pic">
            <h1>Alise Alka</h1>
            <p class="tagline">Empowering Women in IT</p>
            <div class="social-media">
                <a href="https://twitter.com/MissAlise" target="_blank">Twitter</a>
                <a href="https://www.instagram.com/alisealka/" target="_blank">Instagram</a>
                <a href="https://www.linkedin.com/in/%F0%9F%9A%80-alise-a-745863131/" target="_blank">LinkedIn</a>
            </div>
        </div>

        <!-- Links Section -->
        <div class="links">
            <h2>My Work</h2>
            <ul>
                <li><a href="https://replit.com/@aalisiite" target="_blank">Replit</a></li>
            </ul>

            <h2>Profiles</h2>
            <ul>
                <li><a href="https://github.com/aalisiite" target="_blank">GitHub</a></li>
                <li><a href="https://replit.com/@aalisiite" target="_blank">Replit</a></li>
            </ul>
        </div>
    </div>
</body>
</html>
```

### CSS file

```python
/* General styling */
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body, html {
    font-family: 'Arial', sans-serif;
    background: linear-gradient(135deg, #fce4ec, #f3e5f5);
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    color: #333;
}

/* Main container styling */
.container {
    max-width: 600px;
    width: 100%;
    padding: 30px;
    background-color: #ffffff;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    border-radius: 15px;
    text-align: center;
    animation: fadeIn 1.2s ease;
}

/* Profile Picture styling */
.profile-pic {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    object-fit: cover;
    box-shadow: 0px 6px 12px rgba(153, 102, 255, 0.2);
    margin-bottom: 15px;
}

/* Header Text */
h1 {
    font-size: 32px;
    color: #6a1b9a;
    margin-top: 10px;
}

.tagline {
    font-size: 18px;
    color: #8e24aa;
    margin-bottom: 20px;
    font-style: italic;
}

/* Social Media Links */
.social-media a {
    display: inline-block;
    text-decoration: none;
    color: #ffffff;
    font-size: 16px;
    padding: 10px 20px;
    margin: 8px;
    border-radius: 25px;
    background-color: #ab47bc;
    transition: background-color 0.3s ease, transform 0.3s ease;
}

.social-media a:hover {
    background-color: #8e24aa;
    transform: scale(1.1);
}

/* Links Section Styling */
.links {
    margin-top: 20px;
    text-align: left;
}

.links h2 {
    font-size: 22px;
    color: #6a1b9a;
    margin-bottom: 15px;
}

.links ul {
    list-style: none;
    padding: 0;
}

.links li {
    margin-bottom: 10px;
}

/* Link buttons */
.links a {
    display: block;
    text-decoration: none;
    color: #6a1b9a;
    font-weight: bold;
    font-size: 18px;
    padding: 12px 15px;
    background: #f3e5f5;
    border: 2px solid #8e24aa;
    border-radius: 10px;
    transition: background-color 0.3s ease, color 0.3s ease, transform 0.3s ease;
}

.links a:hover {
    background-color: #8e24aa;
    color: #ffffff;
    transform: scale(1.05);
}

/* Animation */
@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
```

</details>