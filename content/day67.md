# 👉 Day 67: tkinter Is Weird? Right?


<a href="https://youtu.be/Bj1TkuZEjK0" target="_blank">📹 David video</a>


**I will say it again for the people in the back. tkinter is horrible. I only showed you this so you will have more love and appreciation for what's coming up next. Click "mark lesson as complete" and skip ahead to Day 70 if tkinter is not your thing. Also this may not work in VSCode. If it is so, then move to day 70. We still have lots of challenges to finish. 💪**

Most GUI creators have a lovely drag & drop interface that makes life easy. tkinter doesn't, so it can feel awkward, fiddly, and frustrating at times.

However, it does give you full control of your GUI, and it's always good to learn the magic behind the scenes so you have a better understanding of what's going on.

Today, we're going to add images into our tkinter GUI.

👉 Let's start with the basic boilerplate GUI and define an image. To do this, I need to build a canvas and then create the image.

**👉 This days challenge should be run from Terminal**

```python
import tkinter as tk
import os

# Get the directory of the current script
script_dir = os.path.dirname(__file__)

# Build the full path to the image
image_path = os.path.join(script_dir, "photos/theFeels.png")

window = tk.Tk()
window.title("Hello World") 
window.geometry("300x200") 


hello = tk.Label(text = "Hello World") 
hello.pack() 

button = tk.Button(text = "Click me!") 
button.pack()

#### NEW BIT ######
canvas = tk.Canvas(window, width = 300, height=150) # Creates a placeholder for the image in the window.
canvas.pack()
image = tk.PhotoImage(file=image_path)  # Sets the file name of the image
canvas.create_image(150,1,image=image) #creates image and sets the co-ordinates for it (150 is horizontal center).
######

tk.mainloop()
```

Note that I've had to upload the image file to my repl. You can just drag & drop it over to your files menu.

<img id="image" src="assets/day67_1.png" alt="day67 image" width="960">


### Big Picture

You may have noticed that your image is HUGE.

👉 We can use `subsample` to resize it. I've just included the relevant lines here.

```python
image = tk.PhotoImage(image_path) 
image = image.subsample(5) # makes the image smaller by a factor of 5
canvas.create_image(150,1,image=image)
```

This technique is OK, but our canvas doesn't have an identifier, so we can't access it again if we need to.

---

👉 Here's the code that solves that problem. I'm also going to make the button change the image on click. All changes to the code are identified with comments.

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

def changeImage(): # new Subroutine
  canvas.itemconfig(container, image = newImage) # itemconfig updates our canvas when this sub is called

hello = tk.Label(text = "Hello World") 
hello.pack() 

button = tk.Button(text = "Click me!", command=changeImage) # Given the button a command to call the changeImage subroutine.
button.pack()


canvas = tk.Canvas(window, width = 300, height=150) 
canvas.pack()
image = tk.PhotoImage(feels_path) 
image = image.subsample(5)

newImage = tk.PhotoImage(success_path) # filename of the replacement image assigned to newImage
newImage = newImage.subsample(5) # scaled down the new image

container = canvas.create_image(150,1,image=image) # Assigned create image to the container variable


tk.mainloop()
```


## Common Errors
 
 First, delete any other code in your `day67.py` file. Copy each code snippet below into `day67.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.


 ### No Replacement Image

👉 Why is it not showing the new image when I click the button?

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
  newImage = tk.PhotoImage(success_path) 
  newImage = newImage.subsample(5) 
  canvas.itemconfig(container, image = newImage) 

hello = tk.Label(text = "Hello World") 
hello.pack() 

button = tk.Button(text = "Click me!", command=changeImage)
button.pack()

canvas = tk.Canvas(window, width = 300, height=150) 
canvas.pack()

image = tk.PhotoImage(feels_path) 
image = image.subsample(5)

container = canvas.create_image(150,1,image=image)


tk.mainloop()
```

<details>
<summary>👀 Answer</summary>

All the images should be defined in the main body of the code, not in the subroutine. If they're in the subroutine, the variables are **local** - they only exist inside the subroutine. So they can't be accessed by the rest of the program.

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
# Moved from the sub to the main program

container = canvas.create_image(150,1,image=image)


tk.mainloop()
```

</details>


## Fix My Code

👉 Try and fix this code which is *full* of errors.

First, delete any other code in your `day67.py` file. Copy each code snippet below into `day67.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

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
  newImage = tk.PhotoImage(success_path) 
  newImage = newImage.subsample(5) 
  canvas.itemconfig(container, image = newImage) 

hello = tk.Label(text = "Hello World") 
hello.pack() 

button = tk.Button(text = "Click me!", command=changeImage)
button.pack()

canvas = tk.Canvas(window, width = 300, height=150) 


image = tk.PhotoImage(feels_path) 
image = image.subsample(5)

container = canvas.create_image(150,1,image=image)
```

<details>
<summary>👀 Answer</summary>

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
  newImage = tk.PhotoImage(success_path) 
   

hello = tk.Label(text = "Hello World") 
hello.pack() 

button = tk.Button(text = "Click me!", command=changeImage)
button.pack()

canvas = tk.Canvas(window, width = 300, height=150) 
canvas.pack() # Didn't pack the canvas

image = tk.PhotoImage(feels_path) 
image = image.subsample(5)

newImage = newImage.subsample(5) 
canvas.itemconfig(container, image = newImage)
# Needed to create the images in the main program.

container = canvas.create_image(150,1,image=image)


tk.mainloop() # Missed out main loop
```

</details>


## 👉 Day 67 Challenge

I've provided you with a folder called "Guess Who" containing images of 4 people.

Your program should:
1. Prompt the user to input a name.
2. If the user inputs 'Charlotte', 'Gerald', 'Kate' or 'Mo', then their image should load.
3. Otherwise an 'image not found' message should display.

**Example:**

<img id="image" src="assets/day67_2.png" alt="day67 image" width="960">

<details>
<summary>💡 Hints</summary>

- Pass the user input into the 'newImage' variable.
- Use `try... except` to load the image or generate the error.

</details>


## Solution (No Peeking!)

<a href="https://youtu.be/q_gsLH9aTWc" target="_blank">📹 David solution video</a>

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

window = tk.Tk()
window.title("Guess Who?")
window.geometry("400x400")
label_text = "Guess Who?"

def showImage():
    person = text.get("1.0", "end").strip().lower()
    if person == "mo":
        canvas.itemconfig(container, image=mo)
        hello["text"] = "Here is Mo!"
    elif person == "charlotte":
        canvas.itemconfig(container, image=charlotte)
        hello["text"] = "Here is Charlotte!"
    elif person == "gerald":
        canvas.itemconfig(container, image=gerald)
        hello["text"] = "Here is Gerald!"
    elif person == "katie":
        canvas.itemconfig(container, image=katie)
        hello["text"] = "Here is Katie!"
    else:
        hello["text"] = "Unable to find this user"

hello = tk.Label(window, text=label_text)
hello.pack()

text = tk.Text(window, height=1, width=30)
text.pack()

button = tk.Button(window, text="Find", command=showImage)
button.pack()

canvas = tk.Canvas(window, width=300, height=300)
canvas.pack()

try:
    charlotte = tk.PhotoImage(file=feels_path)
except Exception as e:
    print(f"Error loading image 'feels.png': {e}")
    charlotte = None

try:
    gerald = tk.PhotoImage(file=success_path)
except Exception as e:
    print(f"Error loading image 'success.png': {e}")
    gerald = None

try:
    katie = tk.PhotoImage(file=image1_path)
except Exception as e:
    print(f"Error loading image 'image1.png': {e}")
    katie = None

try:
    mo = tk.PhotoImage(file=image2_path)
except Exception as e:
    print(f"Error loading image 'image2.png': {e}")
    mo = None

container = canvas.create_image(0, 0, anchor=tk.NW)

window.mainloop()
```

</details>