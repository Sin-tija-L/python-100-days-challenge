# 👉 Day 57: What Is Recursion?

<a href="https://youtu.be/K7h9HlJtWjM" target="_blank">📹 Dāvida video</a>


Before we start, go Google 'recursion'.

Did you get this?

<img id="image" src="assets/day57_1.png" alt="Replit Workspace Overview" width="960">

Those cats at Google are hilarious, aren't they?

---

👉 Recursion is a type of program where you get a function to call itself. It gets kinda hard to explain. I'd very much recommend this [book](https://www.amazon.co.uk/Think-Like-Programmer-Introduction-Creative/dp/1593274246), which does an excellent job of explaining this concept.

Recursion lets us solve problems in a more human way. Some mathematical problems can just be solved better using recursion.

For example:

We want to print out a sequence of the same emoji, reducing by 2 emojis per line. (eg print a row of 9, then a row of 7, then 5, etc. until we get none).

We will end up with a reverse pyramid pattern.

We could use `range()`, but it's a bit odd with counting backwards. Or a loop, but that would be pretty long.

👉 Here's an example of a recursive solution.

```python
def reverse(value):
    if value <= 0: # This `if` provides the 'stop' condition for the program. Otherwise it would run forever.
        print("Done!")
        return
    else: # if we're not at the stop condition.
        emoji_line = "💯" * value  # Create a string of emojis
        print(emoji_line)  # Output the entire string in one line
        reverse(value - 2)  # Reduce the value by 2 and call the function again

reverse(5)
```

Try calling this with 10 as the argument. Did you get this output?

<img id="image" src="assets/day57_2.png" alt="Replit Workspace Overview" width="960">


## Common Errors

First, delete any other code in your `day57.py` file. Copy each code snippet below into `day57.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

### What Is Recursion?

👉 What's the problem here?

```python
def reverse(value):
    if value <= 0: 
        print("Done!")
    else: 
        emoji_line = "💯" * value  
        print(emoji_line)  
        reverse(value - 2) 

reverse(10)
```

<details>
<summary>👀 Answer</summary>
There is no ending condition. It will repeat until it eats up all of the machine's resources until there's no more RAM left! Then, it crashes.

Python has a limit to the amount of recursion. If it didn't, then you'd have unleashed a RAM eating monster!

```python
def reverse(value):
    if value <= 0:
        print("Done!")
        return
    else:
        emoji_line = "💯" * value
        print(emoji_line)
        reverse(value - 2)

reverse(10)
```

</details>


## 👉 Day 57 Challenge

Try to use recursion to build a factorial program.

Yep, it's a math challenge. Recursion is often good for this type of problem.

A factorial is the product of all the numbers up to a value, starting from 1.

For example, factorial 5 would be 1 * 2 * 3 * 4 * 5 = 120

1. Write a function that:
    - Starts at the highest number.
    - Multiplies that by factorial of itself minus one
    - Terminates when it reaches 1 and returns 1
    - Outputs the factorial.

**Example:**

<img id="image" src="assets/day57_3.png" alt="Replit Workspace Overview" width="960">

<details>
<summary>💡 Hints</summary>

- Don't forget to return 1 in your terminating condition.
- Try multiplying the number by the factorial (n-1) call.

</details>


## Solution (No Peeking!)

<a href="https://youtu.be/x0Dz-EJKz-o" target="_blank">Solution video</a>

<details>
<summary>👀 Answer</summary>

```python
def factorial(value, total=1): 
  if value <= 1:
      print("Done")
      return total
  total *= value
  return factorial(value - 1, total)

print("🌟Factorial Finder🌟")
print()
while True:
  try:
      value = int(input("Input a number > "))
      break
  except ValueError:
      print("Input should be a number!")

result = factorial(value)
print(f"The factorial of {value} is {result}")
```

</details>