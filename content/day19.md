# 👉 Day 19: For Loop

<a href="https://www.youtube.com/watch?v=0n65nmmuCSI" target="_blank">Dāvida video</a>

A `while` loop is perfect to use when we don't know how many times we want the loop to repeat.

If we have an idea of how many times we want the loop to repeat, we can use a `for` loop to loop code in exactly the same way the `while` loop did.

However, we can set up the variable, control condition, and increment all in ONE line of code.

<img id="image" src="assets/day19.png" alt="Replit Workspace Overview" width="960">

### Let's compare

Here is how we created a counter with a `while` loop:

```python
counter = 0
while counter < 10:
  print(counter)
  counter += 1
```

And here is the same counter using a `for` loop:

```python
for counter in range(10):
  print(counter)
```

## Range

The `range` function creates a list of numbers in the range you create. If you only give it one number, it will start at `0` and move to a state where the final number is one less than the number in the brackets. In this case, the final number would be `9`.

```python
range(10)
```

Note: The variable is only there during the loop, not after it is completed.

<details>
<summary>Fun Fact</summary>

Commonly computer programmers use the variable names `i`, `j`, and `k` when using `for` loops for counter. There is no real reason. It's just how everyone has always done it. However, feel free to use a variable that has a bit more meaning if you like.

</details>

## Common Errors

First, delete any other code in your `day19.py` file. Copy each code snippet below into `day19.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

### Invalid Syntax

👉 This program will add all the numbers from 0 to 99 and continually print out the total. Why is it not working?

```python
total = 0
for number in range 100:
  total += number
  print(total)
```

<details>
<summary>👀 Answer</summary>

We forgot the `()` with the `range`. The brackets are important because `range` is a function (like the exit function). What range is doing is creating a list of numbers between 0 and the number we put in the brackets. If there are no `()`, it won't work.

```python
for number in range (100):
```

</details>

## Name Error

👉 In this program, the computer should be printing out day + numbers 1-6. Why is it saying 'day is not defined'?

```python
for days in range(7):
  print("Day", day)
```

<details>
<summary>👀 Answer</summary>

The variable name is wrong inside the code. If you want to refer to a created variable in a `for` loop, you have to spell it the same way each time.

```python
print("Day", days)
```

</details>

## Fix My Code

👉 Try and fix this code which is full of errors.

First, delete any other code in your `day19.py` file. Copy each code snippet below into `day19.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

```python
total = 10
while counter in range 100:
  total += 10
  print("total")
```

<details>
<summary>👀 Answer</summary>

```python
total = 10
for counter in range(100):
  total += 10
  print(total)
```

</details>

## 👉 Day 19 Challenge

A common thing people do is borrow money. When people repay money, they pay interest which is paid back annually and added to the original amount the person borrowed.

You are going to create a loan calculator that shows how much money you owe for a loan of $1,000 with a 5% APR (APR is fancy for Annual Percentage Rate) over 10 years.

This means each year the amount of money you owe will increase 5%.

Figure out how much you owe altogether for 10 years?

Use a `for` loop and one or two lines of looped code to determine the answer. (Hint: Don't make this overcomplicated. It should only be a few lines of code altogether.)

<details>
<summary>💡 Hint</summary>

- Make sure the for loop happens 10 times.
- Start your value (amount you are borrowing) before the loop starts.
- If you need to count on one more number, just write i+ in the print statement to tell the computer to add the next number.

</details>

## Solution (No Peeking!)

<details>
<summary>👀 Answer</summary>

```python
loan = 1000
apr = 0.05
for i in range(10):
  loan+=(loan*apr)
  print("Year", i+1, "is", round(loan,2))
```

</details>
