# 👉 Day 69 Challenge! 🚀

<a href="https://youtu.be/edwWQJUxApQ" target="_blank">📹 David video</a>


## 🎮 Today's Challenge: Create Your Own Visual Novel! 📖✨

Ready to dive into a world of interactive storytelling? Today, your task is to create your very own **visual novel** – a simple **"choose your own adventure"** video game that lets players make choices and explore different outcomes. 🌟

### Here's What Your Visual Novel Should Do:

1. **Start with a Scene** 🖼️  
   Begin with an **image**, a short text **introduction**, and two clickable options for the player.

2. **Make it Interactive** 🎯  
   The user will click buttons to **choose their path**, and your game will **display the next scene** based on their decision – showing new **images** and **text**.

3. **Branching Paths** 🌳  
   - From the first branch, **both options lead to the same unhappy ending** 😢 (this will save you some time!).
   - The ending should show an **image**, some text, and a **'Start Again'** button to return the player to the beginning.

4. **Multiple Endings** 🏁  
   - The second branch should have **two new options**:
     - One option leads to a **good ending** 🌈.
     - The other option leads to a **bad ending** 💀.
   - Both of these endings should also include a **'Start Again'** button.

### 🌟 Bonus Tip:
Keep it simple and fun! Your story can be anything – mysterious, adventurous, or even funny! 🤩

---

**Example**:  


<img id="image" src="assets/day69_1.png" alt="day69 image" width="960">

<img id="image" src="assets/day69_2.png" alt="day69 image" width="960">

<img id="image" src="assets/day69_3.png" alt="day69 image" width="960">


<details>
<summary>💡 Hints</summary>

- Nothing big here. Just use functions for each of your pages and call them when necessary.
- Create all of your images and text labels in the main program, but only pack them when they should appear.
- Don't forget to unpack the other page elements that should disappear.

</details>


## Solution (No Peeking!)


<a href="https://youtu.be/3hyL8Ci8fsE" target="_blank">📹 David solution</a>

<details>
<summary>👀 Answer</summary>

```python
import tkinter as tk
import os

# Get the directory of the current script
script_dir = os.path.dirname(__file__)

# Build the full paths to the images
start_path = os.path.join(script_dir, "photos/1.png")
codes_path = os.path.join(script_dir, "photos/3.png")
replit_path = os.path.join(script_dir, "photos/2.png")  # This image will be renamed to something more fitting
days_path = os.path.join(script_dir, "photos/4.png")
amazing_path = os.path.join(script_dir, "photos/5.png")
vs_path = os.path.join(script_dir, "photos/6.png")

window = tk.Tk()
window.title("Visual Novel")
window.geometry("400x400")

story = "You meet a woman on the way to a VSCode meetup IRL"

def iCode():
    global story
    canvas.itemconfig(container, image=codes)
    story = "She tries to pull out her laptop and drops it on the floor"
    storyLabel["text"] = story
    button.pack_forget()
    button2.pack_forget()
    button3.pack()
    button4.pack()

def iVSCode():
    global story
    canvas.itemconfig(container, image=replit)
    story = "Why I use VSCode of course, like every developer!"
    storyLabel["text"] = story
    button.pack_forget()
    button2.pack_forget()
    button5.pack()
    button6.pack()

def iEdit():
    global story
    canvas.itemconfig(container, image=vs)
    story = "She spends two hours loading up VSCode\nand getting it working, you wait politely"
    storyLabel["text"] = story
    button3.pack_forget()
    button4.pack_forget()
    restartButton.pack()

def iUse():
    global story
    canvas.itemconfig(container, image=amazing)
    story = "You both celebrate using VSCode\non your way to the meetup"
    storyLabel["text"] = story
    button3.pack_forget()
    button4.pack_forget()
    restartButton.pack()

def iToo():
    global story
    canvas.itemconfig(container, image=days)
    story = "She tells you all about the 100 days of code challenge!"
    storyLabel["text"] = story
    button5.pack_forget()
    button6.pack_forget()
    restartButton.pack()

def iWin():
    global story
    canvas.itemconfig(container, image=amazing)
    story = "You both celebrate using VSCode\nand talk about the 100 days of code challenge"
    storyLabel["text"] = story
    button5.pack_forget()
    button6.pack_forget()
    restartButton.pack()

def restart():
    global story
    canvas.itemconfig(container, image=start)
    story = "You meet a woman on the way to a VSCode meetup IRL"
    storyLabel["text"] = story
    restartButton.pack_forget()
    button.pack()
    button2.pack()

# Load images
start = tk.PhotoImage(file=start_path).subsample(4)
codes = tk.PhotoImage(file=codes_path).subsample(4)
replit = tk.PhotoImage(file=replit_path).subsample(4)  # Rename this image to better fit the story
days = tk.PhotoImage(file=days_path).subsample(4)
amazing = tk.PhotoImage(file=amazing_path).subsample(4)
vs = tk.PhotoImage(file=vs_path).subsample(4)

canvas = tk.Canvas(window, width=300, height=200)
canvas.pack()
container = canvas.create_image(150, 150, image=start)
storyLabel = tk.Label(text=story)
storyLabel.pack()
button = tk.Button(text="Ask her how she codes?", command=iCode)
button.pack()
button2 = tk.Button(text="Tell her about VSCode", command=iVSCode)
button2.pack()
button3 = tk.Button(text="She says 'I use a local editor (VSCode)'", command=iEdit)
button4 = tk.Button(text="She says 'I use VSCode'", command=iUse)
button5 = tk.Button(text="You say 'I use VSCode too'", command=iToo)
button6 = tk.Button(text="You say 'I'm going through 100 days of code right now'", command=iWin)
restartButton = tk.Button(text="Restart", command=restart)

tk.mainloop()
```

</details>