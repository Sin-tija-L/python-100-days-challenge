# 👉 Day 66: Gooey GUIs


<a href="https://youtu.be/MhVg1LVKP5k" target="_blank">📹 David video</a>


**DISCLAIMER: As the title states, this can get gooey. TKinter totally sucks - if you'd rather move on to something more fun, click "mark lesson as complete" and move on to Day 70 to get back to the good stuff. Also this may not work in VSCode. If it is so, then move to day 70. We still have lots of challenges to finish. 💪**

It's time to bring our programs into the early 90s as we learn how to create a Graphical User Interface (GUI) with a Python library called tkinter.


## tkinter

tkinter is one of the more popular Python GUI libraries.

👉 When you start a tkinter project, you get some boilerplate, or starter code.

```python
import tkinter as tk

window = tk.Tk()
window.title("Hello World") # Sets the name of the window in the border
window.geometry("300x300") # Sets the size of the window in pixels

hello = tk.Label(text = "Hello World") # Creates a text box
hello.pack() # 'pack' places the element on the screen

button = tk.Button(text = "Click me!") # Creates a button
button.pack()

tk.mainloop()
```

**👉 This days challenge should be run from Terminal**


**If window doesn't appear like in the picture below or similar, try to run this command -> `TK_SILENCE_DEPRECATION=1 python3 python_files/day66.py`**

This code will produce a window that looks like this:

<img id="image" src="assets/day66_1.png" alt="day66 image" width="960">

Play around with the size of the window to see the effect of changing the dimensions.


### Label Tricks

👉 We can also use variables to pass strings into labels like this:

```python
label = "Hey there world"
hello = tk.Label(text = label)
```

👉 Now I'm going to use a subroutine that changes the text in the label when I click the button.

```python
window = tk.Tk()
window.title("Hello World") 
window.geometry("300x300") 

label = "Hey there world"

def updateLabel():
  label = "Bye world!"
  hello["text"] = label 
  # Subroutine that updates the text in the label.

hello = tk.Label(text = label) 
hello.pack() 

button = tk.Button(text = "Click me!", command = updateLabel) # Calls the updateLabel subroutine when the button is clicked
button.pack()

tk.mainloop()
```

👉 Let's try the same trick, only this time the label contains a number which increments with every button click. For this I need to use a global label variable.

```python
window = tk.Tk()
window.title("Hello World") 
window.geometry("300x300") 

label = 0 # Sets the starting label value to 0

def updateLabel():
  global label # Uses the values in the label variable
  label += 1 # Adds one to the value in the label
  hello["text"] = label 
  

hello = tk.Label(text = label) 
hello.pack() 

button = tk.Button(text = "Click me!", command = updateLabel) # Calls the updateLabel subroutine when the button is clicked
button.pack()

tk.mainloop()
```


### Adding Text


We can add text boxes to our windows using the entirely obvious `text` command.

👉 Here's the code you need in isolation:

```python
text = tk.Text(window ,height=1, width = 50)
# Three arguments, name of the window to place the text box in, height & width.
text.pack
```

👉 And here it is in context.

```python
window = tk.Tk()
window.title("Hello World") 
window.geometry("300x300") 

label = 0

def updateLabel():
  global label
  label += 1 
  hello["text"] = label 
  

hello = tk.Label(text = label) 
hello.pack() 

button = tk.Button(text = "Click me!", command = updateLabel) 
button.pack()

text = tk.Text(window ,height=1, width = 50)
text.pack()

tk.mainloop()
```

This gives us a window with a text box something like this:

<img id="image" src="assets/day66_2.png" alt="day66 image" width="960">


### It All Adds Up

Let's make our program add the number in the text box to the number in the label when the button is pressed.

👉 To do this, we need to change the `updateLabel` subroutine. Here's the code in isolation:

```python
def updateLabel():
  global label
  number = text.get("1.0","end") # Gets the number from the text box (starting at the first position and going to the end.) and stores in the number variable
  number = int(number) #Casts to an integer. I've done this on a separate line to prevent the line above getting too complex, but you can combine the two.
  label += number # Adds the number from the text box to the one in the label.
  hello["text"] = label
```

👉 Let's add a specific color to the bird class.

```python
class bird(animal):

  def __init__(self):
    self.name = "Bird"
    self.species = "Avian"
    self.sound = "Tweet"
    self.color = color # Only applies to the bird sub class


polly = bird("Green") # Sets polly's colour to 'Green'
polly.talk()
print(polly.color) # Prints polly's color
```

**Try it out!**


### Placing Items

Our window does look a bit odd, doesn't it? Why have the button above the text box?

<img id="image" src="assets/day66_2.png" alt="day66 image" width="960">

👉 We can simply change the order by defining the text box before the button in the code:

```python
window = tk.Tk()
window.title("Hello World") 
window.geometry("300x300") 

label = 0

 def updateLabel(): 
  global label
  number = text.get("1.0","end") 
  number = int(number) 
  label += number
  hello["text"] = label 
  

hello = tk.Label(text = label) 
hello.pack() 

text = tk.Text(window ,height=1, width = 50)
text.pack

button = tk.Button(text = "Click me!", command = updateLabel) 
button.pack()

tk.mainloop()
```

<img id="image" src="assets/day66_3.png" alt="day66 image" width="960">


### Packing

We can add arguments to `pack()` to control the position of items in the window. Again, I'm just showing the relevant lines of code in these examples.

👉 Let's move the button to the bottom of the window.

```python
button.pack(side=tk.BOTTOM)
```

👉 And the text box to the top to the left of the window.

```python
text.pack(side=tk.LEFT)
```

You can also use TOP, RIGHT, CENTER to control location.


### Unpacking

If we had several buttons, the default would be to put them one on top of another.

```python
button = tk.Button(text = "Click me!",
command = updateLabel) 
button.pack()

button = tk.Button(text = "Another Button", command = updateLabel) 
button.pack()

button = tk.Button(text = "Last one", command = updateLabel) 
button.pack()
```

<img id="image" src="assets/day66_4.png" alt="day66 image" width="960">

We can arrange them into a nicer grid layout, but to do this we have to **completely remove** `pack` and break the entire window into a grid.

👉 We then use row and column numbers (zero indexed remember) to place our elements. I've put the label in row 0, text box in row 1 and buttons in row 2.

```python
window = tk.Tk()
window.title("Hello World") 
window.geometry("300x300") 

label = 0

def updateLabel():
  global label
  number = text.get("1.0","end") 
  number = int(number) 
  label += number
  hello["text"] = label 
  

hello = tk.Label(text = label).grid(row=0, column=1)


text = tk.Text(window ,height=1, width = 50).grid(row=1, column=1)


button = tk.Button(text = "Click me!", command = updateLabel).grid(row=2, column=0)

button = tk.Button(text = "Another Button", command = updateLabel).grid(row=2, column=1)

button = tk.Button(text = "Last one", command = updateLabel).grid(row=2, column=2)

tk.mainloop()
```

<img id="image" src="assets/day66_5.png" alt="day66 image" width="960">


**Try It Out**


## Common Errors
 
 First, delete any other code in your `day66.py` file. Copy each code snippet below into `day66.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.


 ### Attribute Error

 👉 Why is there a 'hello.pack()' attribute error?

 ```python
window = tk.Tk()
window.title("Hello World") 
window.geometry("300x300") 

label = 0

def updateLabel():
  global label
  number = text.get("1.0","end") 
  number = int(number) 
  label += number
  hello["text"] = label 
  

hello = tk.Label(text = label).grid(row=0, column=1)
hello.pack()

text = tk.Text(window ,height=1, width = 50).grid(row=1, column=1)

button = tk.Button(text = "Click me!", command = updateLabel).grid(row=2, column=0)

button = tk.Button(text = "Another Button", command = updateLabel).grid(row=2, column=1)

button = tk.Button(text = "Last one", command = updateLabel).grid(row=2, column=2)

tk.mainloop()
```

<details>
<summary>👀 Answer</summary>

- `pack` doesn't work with `grid`. You have to decide to use one or the other.

</details>


### Another Attribute Error

👉 Why am I getting a 'NoneType' attribute error when I click a button? My program was working, but now it isn't.

```python
text = tk.Text(window ,height=1, width = 50).grid(row=1, column=1)
```

<details>
<summary>👀 Answer</summary>

'Getting' the data from the text box worked nicely with `pack`, but not with `grid`.

The `grid` method is directly on the `text` object creation line of code. This causes issues when the `updateLabel` subroutine tries to `get` the contents of the text box.

Wherever I've used `grid` with the text box and the label, I need to split this out onto a separate line. This is because I want to manipulate this data later. I don't need to do it with the buttons because I don't need to manipulate that data.

```python
window = tk.Tk()
window.title("Hello World") 
window.geometry("300x300") 

label = 0

def updateLabel():
  global label
  number = text.get("1.0","end") 
  number = int(number) 
  label += number
  hello["text"] = label 
  

hello = tk.Label(text = label)
hello.grid(row=0, column=1) # New line here

text = tk.Text(window ,height=1, width = 50)
text.grid(row=1, column=1) # New line here

button = tk.Button(text = "Click me!", command = updateLabel).grid(row=2, column=0)

button = tk.Button(text = "Another Button", command = updateLabel).grid(row=2, column=1)

button = tk.Button(text = "Last one", command = updateLabel).grid(row=2, column=2)

tk.mainloop()
```

</details>


## Fix My Code

👉 Try and fix this code which is *full* of errors.

First, delete any other code in your `day66.py` file. Copy each code snippet below into `day66.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

```python
window = tk.Tk()
window.title("Hello World") 
window.geometry("300x300") 

label = 0

def updateLabel():
  global label
  number = text.get("1.0","end") 
  number = int(number) 
  label += number
  hello["text"] = label 
  

hello = tk.Label(text = label).grid(row=0, column=1)

text = tk.Text(window ,height=1, width = 50)
text.grid(row=1, column=1) # New line here

button = tk.Button(text = "Click me!", command = updateLabel).grid(row=2, column=0)

button = .Button(text = "Another Button", command = updateLabel).grid(row=2, column=1)

button = tk.Button(text = "Last one", command = updateLabel).grid(row=2, column=2)

tk.mainloop()
```

<details>
<summary>👀 Answer</summary>

```python
import tkinter as tk # No import

window = tk.Tk()
window.title("Hello World") 
window.geometry("300x300") 

label = 0

global label
  number = text.get("1.0","end") 
  number = int(number) 
  label += number
  hello["text"] = label 
  

hello = tk.Label(text = label)
hello.grid(row=0, column=1) # Needs grid on a new line.

text = tk.Text(window ,height=1, width = 50)
text.grid(row=1, column=1) 

button = tk.Button(text = "Click me!", command = updateLabel).grid(row=2, column=0)

button = tk.Button(text = "Another Button", command = updateLabel).grid(row=2, column=1) # Missed the '.tk'

button = tk.Button(text = "Last one", command = updateLabel).grid(row=2, column=2)

tk.mainloop()
```

</details>


## 👉 Day 66 Challenge

### 🎯 Your Challenge: Build a Simple GUI Calculator! 🎯

Ready to test your GUI skills? Let's create a **simple calculator** that will handle basic math operations and bring numbers to life with just a few clicks! 🧮✨

### Here's What Your Program Should Do:

- **Buttons, buttons, buttons!** 🎛️  
  Include buttons for numbers **0 to 9**, along with operations like **plus (+)**, **minus (-)**, **multiply (×)**, **divide (÷)**, and an **equals (=)** button to calculate the result.

- **User interaction** 🤹  
  The user should be able to press these buttons to **build a calculation**, just like a real calculator!

- **Result output** 📊  
  When the user presses the **equals button (=)**, your program should display the **correct result** right there in the GUI.

### 🎉 Bonus Challenge: 
Make your calculator even fancier by allowing the user to **clear** the current calculation and start fresh!

---

**Example**:  
The user presses **3 + 5 =**, and your calculator should display the result **8**. 🔢

<img id="image" src="assets/day66_6.png" alt="day66 image" width="960">

<details>
<summary>💡 Hints</summary>

- Use a grid to lay out the buttons.
- Create a buttonChoice subroutine or similar that takes in the value of the numeric button clicked, casts it to an int and displays it in the label.
- Create an operatorChoice sub that selects which operator to display and use.
- Investigate the `lambda` command for your buttons.
- Use a `calc` subroutine with global variables for answer, lastnumber and operator.

</details>


## Solution (No Peeking!)

<a href="https://youtu.be/tCrO93lIw2I" target="_blank">📹 David solution video</a>

<details>
<summary>👀 Answer</summary>

```python
import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.geometry("400x500")

label = ""
result = 0
operator = ""

def update_label(text):
    global label
    label += str(text)
    display.config(text=label)

def clear():
    global label
    global result
    global operator
    label = ""
    result = 0
    operator = ""
    display.config(text=label)

def calculate():
    global label
    global result
    global operator
    if operator == "+":
        result += float(label)
    elif operator == "-":
        result -= float(label)
    elif operator == "*":
        result *= float(label)
    elif operator == "/":
        if float(label) != 0:
            result /= float(label)
        else:
            clear()
            display.config(text="Error")
            return
    label = str(result)
    display.config(text=label)
    operator = ""

def set_operator(op):
    global label
    global result
    global operator
    if label != "":
        if operator != "":
            calculate()
        result = float(label)
        operator = op
        label = ""
        display.config(text=label)

display = tk.Label(window, text="", height=2, font=("Arial", 30), anchor="e")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Button layout
button_text = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

row = 1
col = 0

for text in button_text:
    button = tk.Button(
        window, text=text, command=lambda text=text: button_click(text),
        height=3, width=8, font=("Arial", 20)
    )
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    col += 1
    if col > 3:
        col = 0
        row += 1

# Make rows and columns expand with window resizing
for i in range(4):
    window.grid_columnconfigure(i, weight=1)
for i in range(5):
    window.grid_rowconfigure(i, weight=1)

def button_click(text):
    if text in "0123456789":
        update_label(text)
    elif text == ".":
        if "." not in label:
            update_label(text)
    elif text == "C":
        clear()
    elif text == "=":
        calculate()
    else:
        set_operator(text)

tk.mainloop()
```

</details>