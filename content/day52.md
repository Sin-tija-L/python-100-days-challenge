# 👉 Day 52: Avoiding Crashes


**To run this day's code use terminal and run the file 😎**

Sometimes, we just can't code around a crash. It's coming anyway, and all you can do is brace for impact.

Until now!

Let's look at an example based on yesterday's lesson.

---

👉 In this example, if the 'Stuff.mine' file doesn't exist, then the code will throw a 'no such file' error.

```python
myStuff = []

f = open("Stuff.mine","r")
myStuff = eval(f.read())
f.close()

for row in myStuff:
  print(row)
```

### Try...except

The new construct to get around this is called `try.... except`

All the code that should work goes inside the `try`.

<img id="image" src="assets/day52_1.png" alt="Replit Workspace Overview" width="960">

The error messages/instructions to handle any errors running the `try` code go inside the `except`.

<img id="image" src="assets/day52_2.png" alt="Replit Workspace Overview" width="960">

👉 Like this:

```python
myStuff = []

try:
  f = open("Stuff.mine","r")
  myStuff = eval(f.read())
  f.close()
# Try to find a file called 'Stuff.mine' and open it

except:
  print("ERROR: Unable to load")
# If the file can't be found, show the error instead of crashing the whole program
  

for row in myStuff:
  print(row)
```


### You are a Software Developer!

`try.... except` is great for improving the user experience to reduce frustration.

However, there are problems with just putting the whole code in a 'try except'.

As developers (yes you are a software developer now), it'd be nice to know what sort of error has occurred so that we have a better idea of how to fix it.

We can tell `except` what type of error(s) to look for. `Exception` (capital 'E') means 'every type'. I've captured the error type in the 'err' variable and printed it out to tell me what the error is. [Here's a list](https://www.w3schools.com/python/python_ref_exceptions.asp) of some built in `except` error codes.

<img id="image" src="assets/day52_3.png" alt="Replit Workspace Overview" width="960">

👉 Look at how I've extended the `except` now.

```python
myStuff = []

try:
  f = open("Stuff.mine","r")
  myStuff = eval(f.read())
  f.close()
# Try to find a file called 'Stuff.mine' and open it

except Exception as err:
  print("ERROR: Unable to load")
  print(err)
  

for row in myStuff:
  print(row)
```


## Traceback

We could even get rid of the 'err' variable entirely and print a traceback, which will show you the red error tracing you see when python crashes.

I've created a 'debugMode' variable at the top of my code and pu the traceback in an `if` inside the `except`.

👉 This lets me show/hide the tracebacks easily by setting `debugMode` to True/False:

```python
debugMode = True
myStuff = []

try:
  f = open("Stuff.mine","r")
  myStuff = eval(f.read())
  f.close()
# Try to find a file called 'Stuff.mine' and open it

except Exception:
  print("ERROR: Unable to load")

  if debugMode:
    print(traceback)

for row in myStuff:
  print(row)
```

<img id="image" src="assets/day52_4.png" alt="Replit Workspace Overview" width="960">

**Try it out and see what errors you can catch!**


## Common Errors

First, delete any other code in your `day52.py` file. Copy each code snippet below into `day52.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

### Try, Try, Try Again

👉 What's the problem here?

```python
myStuff = []

try:
  f = open("Stuff.mine","r")
  myStuff = eval(f.read())
  f.close()

for row in myStuff:
  print(row)
```

<details>
<summary>👀 Answer</summary>

- No `except` to catch the error. `try` is not finished without an except.

```python
myStuff = []

try:
  f = open("Stuff.mine","r")
  myStuff = eval(f.read())
  f.close()

except:
  print(traceback)

for row in myStuff:
  print(row)
```

</details>


## Fix My Code

👉 Try and fix this code which is full of errors.

First, delete any other code in your `day52.py` file. Copy each code snippet below into `day52.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

```python
try:  
f = open("Stuff.mine","r")
myStuff = eval(f.read())
f.close()

for row in myStuff:
  print(row)
```

<details>
<summary>👀 Answer</summary>

```python
myStuff = [] # Didn't create the list.

try:
  f = open("Stuff.mine","r")
  myStuff = eval(f.read())
  f.close()
# The 'open' lines weren't indented inside the 'try'

except Exception as err:
  print("ERROR: Unable to load")
  print(err)
# Missing 'except'

for row in myStuff:
  print(row)
```

</details>


## 👉 Day 52 Challenge

There's no place like Rome...Or Napoli, Milan, possibly even New York if you must.

Just not the dodgy 2am 'round bread with suspicious toppings' merchants that I definitely do not visit on my way home from a night out.

That's right, you're opening a pizza shop! Try not to get anchovy on your keyboard. Man that stuff *never* washes out.

Regardless, your program today must:

1. Prompt the user to input the quantity and size of pizzas.
2. Multiply the two inputs together to calculate the cost of the pizzas.
3. Store that in a 2D list with the user's name.
4. Use `try.... except` for two reasons:
   - i. Include auto-save and auto-load. Use it with the auto-load.
   - ii. When casting the quantity of pizzas to an integer. Avoid the user crashing the program by typing 'three' instead of '3'. Or any other non-integer input. If they do, then prompt them to try again.

**Example:**

<img id="image" src="assets/day52_5.png" alt="Replit Workspace Overview" width="960">

<details>
<summary>💡 Hints</summary>

- Use subroutines for 'add' and 'view'
- Use a `while.... true` loop for the main menu
- Use a 2d list to store the details of each pizza.
- Use selection to decide which subroutine to run, then write the 2d list to the file.
- For add, get all the inputs in variables and append to a list. Append this list to a 2d one that stores all the pizza details.
- For view, get each index from one row of the 2d list at a time.

</details>


## Solution (No Peeking!)

<a href="https://youtu.be/oBf-gpTZTeE?si=6TkPxAG9tKRM9p0U" target="_blank">Solution video</a>

<details>
<summary>👀 Answer</summary>

```python
import os
import time

order = {}

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the 'files/orders.txt' file
file_path = os.path.join(script_dir, "files", "orders.txt")

# Ensure the 'files' directory exists
os.makedirs(os.path.dirname(file_path), exist_ok=True)

def clear():
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')

def addQuantity():
    while True:
        try:
            quantity = int(input("How many pizzas do you want? "))
            return quantity
        except ValueError:
            print("Wrong type of amount. It should be a number!")

def addSize():
    while True:
        try:
            size = int(input("What size? "))
            return size
        except ValueError:
            print("Wrong type of size. It should be a number!")

def loadOrders():
    orders = {}
    if os.path.exists(file_path):
        f = open(file_path, 'r')
        for line in f:
            name, pizzas = line.strip().split(":", 1)
            pizzas_list = eval(pizzas)  # Convert the string back to a list of dicts
            orders[name] = pizzas_list
        f.close()
    return orders

def saveOrders():
    f = open(file_path, 'w')
    for name, pizzas in order.items():
        f.write(f"{name}:{pizzas}\n")
    f.close()

print("Welcome to pizza shop! 🍕")
print()
order = loadOrders()
name = input("Name please > ")

if name not in order:
    order[name] = []

while True:
    quantity = addQuantity()
    size = addSize()
    total = quantity * size
    pizza = {"Quantity": quantity, "Size": size, "Total": total}
    order[name].append(pizza)

    print(f"Thanks {name}, your pizzas will cost {total}")

    anotherPizza = input("Do you want to add another pizza? (yes/no): ")
    if anotherPizza.lower() != "yes":
        break
    clear()

# Display the orders
print(f"Name: {name}")
print("Pizzas:")
for pizza in order[name]:
    print(f"  Quantity: {pizza['Quantity']}, Size: {pizza['Size']}, Total: {pizza['Total']}")

# Save orders
saveOrders()
```

</details>