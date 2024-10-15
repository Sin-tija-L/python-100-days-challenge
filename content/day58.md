# 👉 Day 58: Debugging


🪲 Debugging is the process of finding and fixing errors, or "bugs," in your code. As a beginner, learning how to effectively debug your code is crucial to becoming a better programmer. In Python, VS Code provides powerful debugging tools that make the process easier, allowing you to set breakpoints, inspect variables, and step through your code to understand its behavior.

In this documentation, we’ll walk through the basics of debugging in VS Code, covering:
1. What debugging is and why it's important.
2. How to set and use breakpoints.
3. How to inspect your code using the VS Code debugger.

---

## What is Debugging?

👉 Debugging helps you identify and resolve errors in your code, including:
- **Syntax Errors:** Mistakes like missing colons or parentheses.
- **Runtime Errors:** Errors that cause your program to crash, such as dividing by zero.
- **Logical Errors:** When your program runs but doesn’t produce the expected output.

VS Code offers an integrated debugger that allows you to pause your code at specific points, check the values of variables, and step through your code line by line to observe how it behaves.


### Syntax Errors

These occur when there’s an error in the syntax of the code. For example, missing colons or incorrect indentation.

**Example of a Syntax Error:**

```python
def say_hello()
    print("Hello, world!")
```
This code will throw a SyntaxError because there's a missing colon (:) after def say_hello(). The correct version should be:

```python
def say_hello():
    print("Hello, world!")
```

Syntax errors prevent your program from running. The Python interpreter will point you to the location of the error, which you can then fix.


### Runtime Errors

These occur when your code runs into a problem during execution, even though the syntax is correct. A common runtime error is trying to divide by zero.

**Example of a Runtime Error:**

```python
def divide(a, b):
    return a / b

result = divide(10, 0)
print(result)
```

This code will raise a ZeroDivisionError because dividing by zero is not allowed. To fix this, you can add error handling to your code:

```python
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

result = divide(10, 0)
print(result)  # Outputs: Error: Cannot divide by zero
```

### Logical Errors

These occur when your code runs without crashing but doesn't produce the correct result. Logical errors can be tricky to spot, as the syntax is correct, and no runtime error is raised.

**Example of a Logical Error:**

```python
def calculate_area(length, width):
    return length + width  # Bug: Should be length * width, not addition

area = calculate_area(5, 3)
print(area)  # Outputs: 8 (incorrect result)
```

The function is supposed to calculate the area of a rectangle, but due to a logical error, it's adding the length and width instead of multiplying them. The correct code should be:

```python
def calculate_area(length, width):
    return length * width  # Corrected the logic to multiply

area = calculate_area(5, 3)
print(area)  # Outputs: 15 (correct result)
```

## Using Breakpoints in VS Code

👉 A breakpoint is a marker that pauses the execution of your code at a specific line. When the execution is paused, you can inspect variables, step through the code, and see what's going on under the hood.

### How to Set a Breakpoint:

1. **Set a Breakpoint:**
- Open your Python file in VS Code.
- Find the line where you want the code to pause.
- Click to the left of the line number, and a red dot will appear. This is your breakpoint.

<img id="image" src="assets/day58_1.png" alt="Replit Workspace Overview" width="960">

2. **Run the Debugger:**
- Once your breakpoints are set, you can start debugging.
- Press `F5` or go to the **Run** menu and select **Start Debugging**. This will run your code in debug mode.

<img id="image" src="assets/day58_2.png" alt="Replit Workspace Overview" width="960">

3. **Inspect Variables:**
- When your program hits a breakpoint, the code execution pauses.
- You can hover over variables to see their current values or check the **Variables** panel in the **Debug** sidebar to view all active variables.

<img id="image" src="assets/day58_3.png" alt="Replit Workspace Overview" width="960">

4. **Step Through Code:**
- Use the debugging toolbar that appears at the top of the editor to control code execution:
    - **Continue (F5):** Resumes the program until the next breakpoint.
    - **Step Over (F10):** Moves to the next line in the current function.
    - **Step Into (F11):** Steps into a function to debug it line by line.
    - **Step Out (Shift+F11):** Steps out of the current function.

---

## Debugging Workflow in VS Code 🪲

Let’s walk through an example to see how debugging works in VS Code.

**Example Python Code with a Bug:**

```python
def divide_numbers(a, b):
    return a / b

result = divide_numbers(10, 0)
print(result)
```

This code will raise a `ZeroDivisionError` because the program attempts to divide by zero. Let’s debug it using breakpoints.

### Steps to Debug:

1. **Set a Breakpoint:**
- In the VS Code editor, click on the line number to set a breakpoint at the `return a / b` line. A red dot will appear, indicating a breakpoint.

2. **Run the Debugger:**
- Press `F5` to start debugging.
- The program will run and pause at the breakpoint before executing the division.

3. **Inspect Variables:**
- Hover over `a` and `b` to see their values (`a=10`, `b=0`).
- The **Variables** pane in the Debug sidebar will also show you all active variables.

4. **Step Through Code:**
- Use the **Step Over (F10)** button to move line by line and watch the program’s behavior.

5. **Fix the Bug:**
- Now that you know `b` is zero, you can modify the code to handle this error:

```python
def divide_numbers(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b
```

6. **Re-run the Program:**
- Press `F5` again, and now the program will return the error message instead of crashing.


## Conclusion

🐞 Debugging in VS Code makes it easy to find and fix bugs in your Python code. By using breakpoints, inspecting variables, and stepping through your code, you can quickly identify what’s going wrong and correct it.

**Key takeaways:**
- Set breakpoints to pause your code at specific points.
- Use the debug toolbar to step through your code.
- Inspect variable values in the Debug panel to understand the program’s state.
- Fix issues and rerun the code to see the results.

With these tools, you'll be able to debug your Python programs effectively. Happy debugging!


## 👉 Day 58 Challenge

This challenge is all about using the debugger.

Copy the broken code below into `day58.py` and use the debugger to help spot the mistakes in it.

```python
import random, os, time
totalAttempts = 0

def game():
  attempts = 0
  while True:
    number = random.randint(1,100)
    guess = int(input("Pick a number between 1 and 100: "))
    if guess > number:
      print("Too high")
      attempts+=1
    elif guess < number:
      print("Too low")
      attempts+=1
    else:
      print("Just right!")
      print(f"{attempts} attempts this round")
      return attempts

while True:
  menu = input("1: Guess the random number game\n2: Total Score\n3: Exit\n> ")
  if menu == 1:
    totalAttempts+= game()
  elif menu == 2:
    print(f"You've had {totalAttempts} attempts")
  else:
    break
```


## Solution (No Peeking!)

<details>
<summary>👀 Answer</summary>

```python
import random, os, time
totalAttempts = 0

def game():
  attempts = 0
  number = random.randint(1,100)
  while True:
    guess = int(input("Pick a number between 1 and 100: "))
    if guess > number:
      print("Too high")
      attempts+=1
    elif guess < number:
      print("Too low")
      attempts+=1
    else:
      print("Just right!")
      print(f"{attempts} attempts this round")
      return attempts

while True:
  menu = int(input("1: Guess the random number game\n2: Total Score\n3: Exit\n> "))
  if menu == 1:
    totalAttempts+= game()
  elif menu == 2:
    print(f"You've had {totalAttempts} attempts")
  else:
    break
```

</details>