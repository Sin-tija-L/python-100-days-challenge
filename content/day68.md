# 👉 Day 68: Hide & Remove


<a href="https://youtu.be/Bj1TkuZEjK0" target="_blank">📹 David video</a>


**DISCLAIMER: I promise the good stuff is coming back. We have to go through the valley to get to the mountain, right?**

Sometimes, we want to remove a button, image or piece of text from the screen.

To do this, we use `pack_forget(`.

👉 We'll start with our default tkinter program.

**👉 This days challenge should be run from Terminal**

```python
import tkinter as tk

window = tk.Tk()
window.title("Hello World") 
window.geometry("300x200") 


hello = tk.Label(text = "Hello World") 
hello.pack() 

button = tk.Button(text = "Click me!") 
button.pack()

tk.mainloop()
```

👉 Now I'm going to add a new subroutine to hide the label and call it on a button click.

```python
import tkinter as tk

window = tk.Tk()
window.title("Hello World") 
window.geometry("300x200") 

# New subroutine
def hideLabel():
  hello.pack_forget() # Removes the 'hello' label

hello = tk.Label(text = "Hello World") 
hello.pack() 

button = tk.Button(text = "Click me!", command = hideLabel) # Calls the 'hideLabel' sub on click.
button.pack()

tk.mainloop()
```

👉 Let's look at the window after this code runs:

<img id="image" src="assets/day68_1.png" alt="day68 image" width="960">

Yay! The label has been hidden.


### Come Back!

To bring the label back, we use a Boolean variable to store the state of the label. Is it 'on' (True) or 'off' (False)? The variable starts as True.

I'll add this variable to the `hideLabel` sub as a global, and set it to 'False' when the sub is called.

Now I can use selection in the `hideLabel` sub to check the value in `labelOn`. If it's 'True' I'll hide the label, if it's 'False', I'll show the label.

```python
import tkinter as tk

window = tk.Tk()
window.title("Hello World") 
window.geometry("300x200") 

labelOn = True

def hideLabel():
  global labelOn

  if labelOn: # if labelOn is Python shorthand for 'if labelOn == True'
    hello.pack_forget()
    labelOn = False
  else:
    hello.pack()
    labelOn = True

hello = tk.Label(text = "Hello World") 
hello.pack() 

button = tk.Button(text = "Click me!", command = hideLabel) 
button.pack()

tk.mainloop()
```

Try it out. The button should now toggle the label from visible to invisible.

👉 It will spawn underneath the button though, so we'll need to control where it loads.

I can do this by hiding and respawning everything in the correct order in the `else` part of the selection.

```python
def hideLabel():
  global labelOn

  if labelOn: 
    hello.pack_forget()
    labelOn = False
  else:
    button.pack_forget #hides the button
    hello.pack() # shows the label first (top of the window)
    button.pack() # then reloads the button underneath
    labelOn = True
```


**Try it out!**


### Hiding Images

Here's our image code from Day 67.

```python
import tkinter as tk
import os

# Get the directory of the current script
script_dir = os.path.dirname(__file__)

# Build the full path to the image
feels_path = os.path.join(script_dir, "photos/theFeels.png")
success_path = os.path.join(script_dir, "photos/success.png")

window = tk.Tk()
window.title("Hello World") 
window.geometry("300x200") 

def changeImage(): 
  canvas.itemconfig(container, image = newImage)

hello = tk.Label(text = "Hello World") 
hello.pack() 

button = tk.Button(text = "Click me!", command=changeImage)
button.pack()


canvas = tk.Canvas(window, width = 300, height=150) 
canvas.pack()
image = tk.PhotoImage(feels_path) 
image = image.subsample(5)

newImage = tk.PhotoImage(success_path)
newImage = newImage.subsample(5) 

container = canvas.create_image(150,1,image=image)


tk.mainloop()
```

👉 I'm going to add a second button called 'button2' that will hide the image. Actually, what we're really doing is hiding the canvas. Here's the isolated code for that.

```python
button2 = tk.Button(text = "Hide Image!", command=hideImage) 
button2.pack()
```

---

👉 Next I need to create the `hideImage` sub above the button creation. The isolated code is:

```python
def hideImage():
  canvas.pack_forget()
```

---

👉 Now, here are those code snippets as part of the whole program:

```python
import tkinter as tk
import os

# Get the directory of the current script
script_dir = os.path.dirname(__file__)

# Build the full path to the image
feels_path = os.path.join(script_dir, "photos/theFeels.png")
success_path = os.path.join(script_dir, "photos/success.png")

window = tk.Tk()
window.title("Hello World") 
window.geometry("300x200") 

def changeImage():
  canvas.itemconfig(container, image = newImage)

  #### NEW SUBROUTINE ######
def hideImage():
  canvas.pack_forget()

hello = tk.Label(text = "Hello World") 
hello.pack() 

button = tk.Button(text = "Click me!", command=changeImage)
button.pack()

#### NEW BUTTON ######
button2 = tk.Button(text = "Hide Image!", command=hideImage) 
button2.pack()

canvas = tk.Canvas(window, width = 300, height=150) 
canvas.pack()
image = tk.PhotoImage(feels_path) 
image = image.subsample(5)

newImage = tk.PhotoImage(success_path) 
newImage = newImage.subsample(5)

container = canvas.create_image(150,1,image=image)


tk.mainloop()
```


**Try it out!**


## Common Errors
 
 First, delete any other code in your `day68.py` file. Copy each code snippet below into `day68.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.


👉 Why am I getting an attribute error when I try to `pack_forget` the container?

 ```python
import tkinter as tk
import os

# Get the directory of the current script
script_dir = os.path.dirname(__file__)

# Build the full path to the image
feels_path = os.path.join(script_dir, "photos/theFeels.png")
success_path = os.path.join(script_dir, "photos/success.png")

window = tk.Tk()
window.title("Hello World") 
window.geometry("300x200") 

def changeImage():
  canvas.itemconfig(container, image = newImage)
def hideImage():
  container.pack_forget()

hello = tk.Label(text = "Hello World") 
hello.pack() 

button = tk.Button(text = "Click me!", command=changeImage) 
button.pack()

button2 = tk.Button(text = "Hide Image!", command=hideImage) 
button2.pack()

canvas = tk.Canvas(window, width = 300, height=150) 
canvas.pack()

image = tk.PhotoImage(feels_path) 
image = image.subsample(5)

newImage = tk.PhotoImage(success_path) 
newImage = newImage.subsample(5) 

container = canvas.create_image(150,1,image=image) 

tk.mainloop()
```

<details>
<summary>👀 Answer</summary>

The container is not directly in the window, so it can't be hidden. The canvas is. That's what we have to hide.

```python
def hideImage():
  canvas.pack_forget()
```

</details>


## Fix My Code

👉 Try and fix this code which is *full* of errors.

First, delete any other code in your `day68.py` file. Copy each code snippet below into `day68.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

```python
import tkinter as tk
import os

# Get the directory of the current script
script_dir = os.path.dirname(__file__)

# Build the full path to the image
feels_path = os.path.join(script_dir, "photos/theFeels.png")
success_path = os.path.join(script_dir, "photos/success.png")

def changeImage():
  canvas.itemconfig(container, image = newImage)

def hideImage():
  container.pack_forget()

hello = tk.Label(text = "Hello World") 
hello.pack() 

button = tk.Button(text = "Click me!", command=changeImage) 
button.pack()

button2 = tk.Button(text = "Hide Image!", command=hideImage) 
button2.pack()

canvas = tk.Canvas(window, width = 300, height=150) 
canvas.pack()

image = tk.PhotoImage(feels_path) 
image = image.subsample(5)

newImage = tk.PhotoImage(success_path) 
newImage = newImage.subsample(5) 

container = canvas.create_image(150,1,image=image) 

tk.mainloop()
```

<details>
<summary>👀 Answer</summary>

Oh no! This was a *really* tricky one. di you get it?
Yep, we were tyring to hide the container instead of the canvas.

```python
def hideImage():
  canvas.pack_forget()
```

</details>


## 👉 Day 68 Challenge

For today's challenge, you need your code from Day 67.

1. Start the program with no image displayed. 
2. If the user inputs a name that can't be found, a new label should appear in the image location saying 'Unable to find image'.

🥳 Extra points for getting all the inputs with just one `input` command and the `split` function.

**Example:**

<img id="image" src="assets/day68_2.png" alt="day68 image" width="960">

<details>
<summary>💡 Hints</summary>

- Create the error label in the main program. Just don't pack it so it doesn't show.
- If the image can't be found, hide the canvas and pack the error label.

</details>


## Solution (No Peeking!)

<a href="https://youtu.be/fz-AYuYFjzM" target="_blank">📹 David solution video</a>

<details>
<summary>👀 Answer</summary>

```python
import tkinter as tk
import os

# Get the directory of the current script
script_dir = os.path.dirname(__file__)

# Build the full path to the images
feels_path = os.path.join(script_dir, "photos/theFeels.png")
success_path = os.path.join(script_dir, "photos/success.png")
image1_path = os.path.join(script_dir, "photos/image1.png")
image2_path = os.path.join(script_dir, "photos/image2.png")
image3_path = os.path.join(script_dir, "photos/image3.png")

window = tk.Tk()
window.title("Guess Who?")
window.geometry("1000x1000")

label = "Guess Who?"

def changeImage(newImage):
    canvas.itemconfig(container, image=newImage)

def getUserInput():
    input_text = text.get("1.0", "end").strip().lower()
    images = {
        "mario": image1,
        "luigi": image2,
        "peach": image3,
        "toad": image4,
        "yoshi": image5
    }
    new_image = images.get(input_text)
    if new_image is not None:
        changeImage(new_image)
    else:       
        canvas.pack_forget()
        unable_label.pack()
        return
    unable_label.pack_forget()
    canvas.pack()

hello = tk.Label(text=label)
hello.pack()

unable_label = tk.Label(text="Unable to find image")

text = tk.Text(window, height=1, width=30)
text.pack()

button = tk.Button(text="Click me!", command=getUserInput)
button.pack()

canvas = tk.Canvas(window, width=700, height=5000)
canvas.pack()

image1 = tk.PhotoImage(feels_path)
image1 = image1.subsample(1)

image2 = tk.PhotoImage(success_path)
image2 = image2.subsample(1)

image3 = tk.PhotoImage(image1_path)
image3 = image3.subsample(1)

image4 = tk.PhotoImage(image2_path)
image4 = image4.subsample(1)

image5 = tk.PhotoImage(image3_path)
image5 = image5.subsample(1)

container = canvas.create_image(150, 1, image="")  

tk.mainloop()
```

</details>