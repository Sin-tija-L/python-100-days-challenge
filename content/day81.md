# 👉 Day 81 Challenge: Build an "I'm Not a Robot" Verification Program 🤖

Today’s challenge is to create a fun and interactive **"I'm Not a Robot"** verification program to distinguish humans from robots. 🕹️

---

### 🚀 How it Should Work:

1. **Ask the User Verification Questions:**  
   - Your program should prompt the user with **at least three different questions** designed to identify potential "robotic" responses. These questions should be playful yet challenging. 🤔
   - **Example questions:**
     - "Are you made of metal?" (Yes/No, radio button) 🛠️
     - "What’s your creator's name?" (Free text) 👤
     - "Which one of these describes you best?" (Drop-down menu with options like "Human," "Robot," "Alien," etc.) 🌌

2. **Question Formats:**
   - **One question** should be a **Yes/No** question using **radio buttons** for answer options. ✅❌
   - **One question** should allow for **free text** input. ✏️
   - **One question** should use a **drop-down menu** for selecting the answer. 🔽

3. **Analyze the Responses:**  
   - Identify "robotic" responses based on pre-set giveaway answers (e.g., "Yes" to "Are you made of metal?"). 💡
   - Use the responses to determine if the user is more likely to be a human or a robot. 🧑🤖

4. **Display the Result:**  
   - After the user answers all questions, your program should display either a **"You’re a robot!"** or **"Not a robot!"** message based on their answers. 🎉

<img id="image" src="assets/day81_1.png" alt="day81 image" width="960">

<img id="image" src="assets/day81_2.png" alt="day81 image" width="960">

<img id="image" src="assets/day81_3.png" alt="day81 image" width="960">

---

### 🌟 Extra Tips:
   - Make it fun! 🎈 You can add additional quirky questions or customize the messages to create an entertaining experience.
   - Consider using basic HTML or a simple GUI framework to create an interactive interface if you’re working on this in Python or JavaScript. 🖥️

Happy coding! 🥳

---

## Solution (No Peeking!)


<details>
<summary>👀 Answer</summary>

### day81.py file

```python
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def verify_robot():
    if request.method == 'POST':
        answers = {
            'question1': request.form.get('q1'),
            'question2': request.form.get('q2'),
            'question3': request.form.get('q3')
        }

        # Check for giveaway answers
        if (
            answers['question1'] == 'Yes' or
            'Sirius Cybernetics Corporation' in answers['question2'] or
            answers['question3'] == 'ED-209'
        ):
            result = "You're a robot 🤖"
        else:
            result = "Not a robot! 🎉"

        return render_template('result.html', result=result)

    return render_template('day81.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)
```

### day81.html file

```python
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>I'm Not a Robot Verification</title>
  <link rel="stylesheet" href="{{ url_for('static', filename='styles/day81.css') }}">
</head>
<body>
  <div class="container">
    <h2>I'm Not a Robot Verification 🤖</h2>
    <form method="POST" action="/">
      <div class="question">
        <label for="q1">1. Are you made of metal? 🛠️</label><br>
        <input type="radio" name="q1" value="Yes" required> Yes
        <input type="radio" name="q1" value="No"> No
      </div>

      <div class="question">
        <label for="q2">2. Who created you? 👤</label><br>
        <input type="text" id="q2" name="q2" required>
      </div>

      <div class="question">
        <label for="q3">3. What do you dream of becoming? 🌌</label><br>
        <select id="q3" name="q3">
          <option value="Human">Human</option>
          <option value="Robot">Robot</option>
          <option value="ED-209">ED-209</option>
        </select>
      </div>

      <button type="submit" class="submit-btn">Submit</button>
    </form>
  </div>
</body>
</html>
```

### result.html file

```python
<!-- templates/result.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Verification Result</title>
  <link rel="stylesheet" href="{{ url_for('static', filename='styles/day81.css') }}">
</head>
<body>
  <div class="container">
    <h2>Verification Result</h2>
    <p class="result">{{ result }}</p>
    <a href="/" class="back-link">Try Again</a>
  </div>
</body>
</html>
```

### CSS file

```python
/* static/style.css */

body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f9;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
  }
  .container {
    background: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    width: 300px;
    text-align: center;
  }
  h2 {
    color: #333;
  }
  .question {
    margin: 10px 0;
    font-size: 16px;
    color: #555;
  }
  input[type="radio"] {
    margin-right: 5px;
  }
  input[type="text"], select {
    width: 100%;
    padding: 8px;
    margin-top: 5px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  .submit-btn {
    background-color: #4CAF50;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
    margin-top: 10px;
  }
  .submit-btn:hover {
    background-color: #45a049;
  }
  .result {
    font-size: 18px;
    font-weight: bold;
    color: #333;
    margin: 20px 0;
  }
  .back-link {
    text-decoration: none;
    color: #4CAF50;
  }
  .back-link:hover {
    text-decoration: underline;
  }
```

</details>
