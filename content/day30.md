# 👉 Day 30: f-strings

<a href="https://www.youtube.com/watch?v=uaOmD6XRt3A" target="_blank">Dāvida video</a>

## f-strings
f-strings (format strings) are the best way to combine variables and text together. Everything up until now has been...well...awkward.

👉 Let's look at how we have combined variables and text in the past...concatenating.

```python
name = "Katie"
age = "28"
pronouns = "she/her"

print("This is", name, "using", pronouns, "pronouns and is age", age)
```

👉 Let's now use an f-string for this same code. What changes did I make to this code?

```python
name = "Katie"
age = "28"
pronouns = "she/her"

print("This is {}, using {} pronouns, and is {} years old.".format(name, pronouns, age))
```


Change 1: Using `{}` as a placeholder for the variable. Change 2: Adding `.format(variable names, commas)`


<img id="image" src="assets/day30.png" alt="Replit Workspace Overview" width="960">

### Why is this easier? Let's find out.


## Local Variables

We can set local variables within the f-string itself. Now it doesn't matter the order of the variables.

👉 Looking at this code again, I can set my variables inside the text itself. Watch this:

```python
name = "Katie"
age = "28"
pronouns = "she/her"

print("This is {name}, using {pronouns} pronouns, and is {age} years old. Hello, {name}. How are you? Have you been having a great {age} years so far".format(name=name, pronouns=pronouns, age=age))
```

Change 1: Replace `{}` with variable names. Change 2: Replace each variable inside `{}` with what has been defined in `format.( = )`


<img id="image" src="assets/day30-01.png" alt="Replit Workspace Overview" width="960">

f-strings work with different variable types too: `int`, `float`, and `string`.

👉 We can assign concatenated sentences to variables. Watch this. We made a variable called response and made it equal to a concatenated sentence. Now I can use this response easily wherever I want.

```python
name = "Katie"
age = "28"
pronouns = "she/her"

response = "This is {name}, using {pronouns} pronouns, and is {age} years old. Hello, {name}. How are you? Have you been having a great {age} years so far".format(name=name, pronouns=pronouns, age=age)

print(response)
```

#### Now we have a unique text string. We can't do this with commas.

## The Power of f...

Instead of all that faffing about...try this instead.

Use the letter `f` before any string with `{}` for variable names (and forget that `.format` business).

<img id="image" src="assets/day30-02.png" alt="Replit Workspace Overview" width="960">

👉 Look at this same code and see the difference using this technique:

```python
name = "Katie"
age = "28"
pronouns = "she/her"

response = f"This is {name}, using {pronouns} pronouns, and is {age} years old. Hello, {name}. How are you? Have you been having a great {age} years so far"

print(response)
```

#### You can even use this trick with the `"""` triple quote. (Remember, when we learned that on Day 1.)

## Alignment

<img id="image" src="assets/day30-03.png" alt="Replit Workspace Overview" width="960">

left = `<`, right = `>`, center = `^`

👉 This program shows how much of 100 Days of Code we have completed so far. I want this to look like a list. However, once we get to day 10, it starts to look a bit messy. Make sure you include f when using alignment.

```python
for i in range(1, 31):
  print(f"Day {i} of 30")
```

👉 Let's fix it by adding a left alignment of 2 characters long.


```python
for i in range(1, 31):
  print(f"Day {i: <2} of 30")
```

#### Play around with alignment. What do you think?

## Common Errors

First, delete any other code in your `day30.py` file. Copy each code snippet below into `day30.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

👉 What's wrong with this code:

```python
for i in range(1, 31):
  print("Day {i} of 100")
```

<details>
<summary>👀 Answer</summary>

We missed the `f `before the string OR we need to add `.format`


```python
for i in range(1, 31):
  print(f"Day {i} of 100")
```
OR

```python
for i in range(1, 31):
  print(f"Day {i} of 100")
```

</details>

f-strings must have `f` before them or `.format` after them or they will not work.

## Fix My Code

👉 Try and fix this code which is full of errors.

First, delete any other code in your `day30.py` file. Copy each code snippet below into `day30.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

```python
food = pizza"
location = "beach"
color = "green"
friend = "Quinn"

"Alejandra ordered {food} to eat at the {location} with her friend, {friend}. She got to the {location} and looked for a {color} umbrella where {friend} said they would be waiting. By the time, Sally found {friend}, the {food} was cold and the {location} was lame." format(food=food, location=location, color=color,)

print(response)
```

<details>
<summary>👀 Answer</summary>

```python
food = "pizza"
location = "beach"
color = "green"
friend = "Quinn"

response = "Alejandra ordered {food} to eat at the {location} with her friend, {friend}. She got to the {location} and looked for a {color} umbrella where {friend} said they would be waiting. By the time, Sally found {friend}, the {food} was cold and the {location} was lame." .format(food=food, location=location, color=color, friend=friend)

print(response)
```

</details>

## 👉 Day 30 Challenge

- Create a program that uses a loop that asks the user what they have thought of each of the 30 days of challenges so far.

- For each day, prompt the user to answer a question and restate it in a full sentence that is center aligned underneath the heading.

Example:

```python
30 Days Down

Day 1: 
Amazing

            You thought Day 1 was amazing.
Day 2:
so good that I bought the David plushie

              You thought Day 2 was so good...
```

<details>
<summary>💡 Hint</summary>

- Look at the common error for help on the loop.
- Create an `input` statement for the user to express what they thought of that day.
- `print` using an f-string.
- Think about what symbol you need for center alignment. How many spaces should you move your statement?
- Think about the length of the heading. Maybe that's how many spaces you would need to center align the text.

</details>


## Solution (No Peeking!)

<a href="https://www.youtube.com/watch?v=JBJfN4aOyOY" target="_blank">Solution video</a>

<details>
<summary>👀 Answer</summary>

```python
print("30 Days Down - What did you think?")
print()
for i in range(1, 31):
  thought = input(f"Day {i}:\n")
  print()
  myText = f"You thought Day {i} was"
  print(f"{myText:^35}")
  print(f"{thought:^35}")
  print()
```

</details>