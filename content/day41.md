# 👉 Day 41: Dictionaries With Loops

<a href="https://www.youtube.com/watch?v=MENfSTbAcn8" target="_blank">Dāvida video</a>


Loops and lists are a perfect pair. Dictionaries and loops are a bit trickier. This is because each dictionary item is made up of two parts - the name of the key and the actual value of that key.

### I've Lost My Keys!
Let's set up a looped dictionary.

👉 Using a `for` loop, like we would with a list, will output the values, but not the keys. Not ideal.

```python
myDictionary = {"name" : "Ian", "health": 219, "strength": 199, "equipped": "Axe"}

for i in myDictionary:
  print(myDictionary[i])
```

👉 This loop uses the `.values()` method, which can be run on a data type. We still only get the value, and not the key.

```python
myDictionary = {"name" : "Ian", "health": 219, "strength": 199, "equipped": "Axe"}

for value in myDictionary.values():
  print(value)
```

### I've Got The Key...I've Got The Secret

There is a better way!

Here's a loop that will output both key and value.

👉 The `.items()` function returns the key name and value. Note that I've supplied the loop with two arguments: 'name' and 'value').

This example will just output the names and values using an fString.

```python
myDictionary = {"name" : "Ian", "health": 219, "strength": 199, "equipped": "Axe"}

for name,value in myDictionary.items():
  print(f"{name}:{value}")
```

## A Bit Iffy

Let's go one step further and use some `if` statements inside the loop.

👉 This example makes a comment about the strength key.

```python
myDictionary = {"name" : "Ian", "health": 219, "strength": 199, "equipped": "Axe"}

for name,value in myDictionary.items():
  print(f"{name}:{value}")

  if (name == "strength"):
    print("Whoa, SO STRONG!")
```

👉This example uses nested `if` statements to react to the key name and the value stored within it.

```python
myDictionary = {"name" : "David the Mildy Terrifying", "health": 186, "strength": 4, "equipped":"l33t haxx0r p0werz"}

for name,value in myDictionary.items():
  print(f"{name}:{value}")

  if (name == "strength"):
    if value > 100:
      print("Whoa, SO STRONG")
    else:
      print("Looks like you skipped leg day, arm day, chest day and, well, gym day entirely bro!")
```

### Try it out and harness the power of iteration with your dictionary!

## Common Errors

First, delete any other code in your `day41.py` file. Copy each code snippet below into `day41.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

## Make The Brackets Go Away!

👉 What is the problem here?

```python
myDictionary = {"name" : "Ian", "health": 219, "strength": 199, "equipped": "Axe"}

for name in myDictionary.items():
  print(f"{name}")
```

<details>
<summary>👀 Answer</summary>

We only gave the loop one variable instead of two.


```python
myDictionary = {"name" : "Ian", "health": 219, "strength": 199, "equipped": "Axe"}

for name, value in myDictionary.items():
  print(f"{name} {value}")
```

</details>

## Fix My Code

👉 Try and fix this code which is full of errors.

First, delete any other code in your `day41.py` file. Copy each code snippet below into `day41.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

```python
myDictionary = {"name" : "David the Mildy Terrifying", "health": 186, "strength": 4, "equipped":"l33t haxx0r p0werz"}

for name in myDictionary.items():
  print(f"{name}:{value}")

  if (name == "strength"):
  if value > 100:
    print("Whoa, SO STRONG")
  else:
    print("Looks like you skipped leg day, arm day, chest day and, well, gym day entirely bro!")
```

<details>
<summary>👀 Answer</summary>

```python

myDictionary = {"name" : "David the Mildy Terrifying", "health": 186, "strength": 4, "equipped":"l33t haxx0r p0werz"}

for name, value in myDictionary.items():
print(f"{name}: {value}")

if (name == "strength"): 
if value > 100: # This nested if wasn't indented properly
  print("Whoa, SO STRONG")
else:
  print("Looks like you skipped leg day, arm day, chest day and, well, gym day entirely bro!")
```

</details>

## 👉 Day 41 Challenge

1. Create a dictionary that stores the following information about a website: name, URL, description and a star rating (out of 5).
2. Use a loop to output the names of the keys, ask the user to type in the details and store the input in the dictionary.
3. Finally, output the whole dictionary (keys and values).

🥳 Extra points for getting all the inputs with just one `input` command and the `split` function.

Example:

```python
🌟Website Rating🌟

Input the website name: Replit

Input the URL: replit.com

Input your a description: An awesome online IDE.

Input the a star rating out of 5: *****

name:Replit, URL:replit.com, description:An awesome online IDE, rating:*****
```

<details>
<summary>💡 Hint</summary>

- When creating your dictionary, you will need to use e`xample = { "MyValue": none}` to show a key name and no value.
- Use a loop to `print` the entire dictionary.
- Make sure you include both variables (name and value) in your loop and your `print` statement.

</details>

## Solution (No Peeking!)

<a href="https://www.youtube.com/watch?v=J-ea9g4R9PI" target="_blank">Solution video</a>

<details>
<summary>👀 Answer</summary>

```python
website = {"name": None, "url": None, "desc": None, "rating": None}

for name in website.keys():
  website[name] = input(f"{name}: ")

print()
for name, value in website.items():
  print(f"{name}: {value}")
```

</details>