# Day20 - What can range really do?

<a href="https://www.youtube.com/watch?v=cstyIsl2Q6s" target="_blank">Dāvida video</a>

Give range one number, and it will count up to that number. However, you can actually give the range function a few options...

- **starting value**: what number do you want to start with?
- **ending value**: the number after the number you want to end with (example: if you type 10 as the ending value, the computer will count until 9)
- **increment**: How much should it increase by every time it loops? (example: Do you want to count by 1s, 5s, 10s?)

<img id="image" src="assets/day20.png" alt="Replit Workspace Overview" width="960">

**The ending value has an unsaid 'less than'. Meaning the computer will stop one number before the ending number that is written in the range.**

### Let's try some examples.

## Let's try it out

The first number in this range, 100, is the starting value. The second number in this range, 110, is the ending value (Remember to always put the ending number as one more than where you want to end up).

👉 What number will the code run first? What number will be last? `Run` the code and find out.

```python
for i in range(100, 110):
  print(i)
```

👉 What do you expect to print with the range below? `Run` and find out.

```python
for i in range(1, 7):
  print("Day", i)
```

Did you notice that the counter stopped at 'Day 6'? Change the ending value to be one more than the last number you want shown---in this case, 8 because we want to display 7 days of the week.

```python
for i in range(1, 8):
  print("Day", i)
```

👉 What happens when you `run` this code?

```python
print("Thirteen Times Table")
for i in range(1, 13):
  print(i, "x 13 =", i * 13)
```

### Let's add increments to our range.

## Increments

We know that this range will start at 0 and continue to 999,999 (which is the number right before the ending value written). The number will increase in increments of 25 each time.

👉 What numbers do you expect to see? Hit `run` and find out.

```python
for i in range (0, 1000000, 25):
  print(i)
```

## Counting Backward

In this example, we are starting at 10 and counting backward to 0 (because 0 is what comes right before the ending value listed), and counting backward 1 each time.

👉 What do you expect to see when you hit `run`?

```python
for i in range(10, -1, -1):
  print(i)
```

## Common Errors

First, delete any other code in your `day20.py` file. Copy each code snippet below into `day20.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

```python
for i in range (10, 0):
  print(i)
```

<details>
<summary>👀 Answer</summary>

The third value in the `range` function, increment, is missing. We need to add an increment of `-1` to go backward. Without the increment written, the computer does the default of +1.

Without the increment listed, we are telling the computer: "start at 10, keep going until 0, and add one each time." This can't be done so nothing will run unless we add an increment.

```python
for i in range (10, 0, -1):
```

</details>

## Fix My Code

👉 _Try and fix this code which is full of errors._

First, delete any other code in your `day20.py` file. Copy each code snippet below into `day20.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

```python
while i in range (20, 40, -1):
  print(i)
```

<details>
<summary>👀 Answer</summary>

```python
for i in range (20, 40, 1):
  print(i)
```

_Note: You can change the increment to a different number if you like and count by 2 or 5, etc._

</details>

## 👉 Day 20 Challenge

Ask the user to list a starting number, ending number, and increment to use. Display an answer based on the users' answers (use the `input` command.)

```python
Example:
Start at: 200
End before: 300
Increment between values: 20
200
220
240
260
280
```

<details>
<summary>💡 Hint</summary>

- Since you are using numbers, what else do you need to add when using `input`?
- Define your variables as letters that can be placeholders in the range for the user's answers.

</details>

## Solution (No Peeking!)

<details>
<summary>👀 Answer</summary>

```python
print("Welcome to my number list generator.")
print()
print("You are going to give me a number you want to start with, an ending number, and by how many you want me to add each time.")
print()

x = int(input("What number do you want to start with? "))
y = int(input("What number do you want to end with? "))
z = int(input("How many should I add each time? "))

for i in range(x, y, z):
  print(i)
```

</details>
