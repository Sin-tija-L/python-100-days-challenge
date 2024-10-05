# 👉 Day 40: Dictionaries

<a href="https://www.youtube.com/watch?v=TkKsEq6ODNs" target="_blank">Dāvida video</a>


As you might have guessed, we love lists. However, list items are accessed in order by index number. This isn't always the way we want it to work.

Dictionaries are a slightly different type of list that access data by giving each item a key. This creates what we call key:value pairs.

Now we can access each item through its key, instead of having to remember what index it is at in the list.

### Creating a dictionary - brace!
Curly, curly braces...

To create a dictionary we start just like a list, except with curly braces `{}`. This dictionary will store data about a user.

The data is inserted in key value pairs like this. Each pair is separated by a comma:

<img id="image" src="assets/day40.png" alt="Replit Workspace Overview" width="960">

👉 The first key:value pair below has "name" as the key and "David" as the value. Try it out:

```python
myUser = {"name": "David", "age": 128}
```

## Printing the keys


To output (print) from a dictionary, we can use the key instead of the index. Note that we still use square brackets for accessing items (ex: `["name"]`).

<img id="image" src="assets/day40-01.png" alt="Replit Workspace Overview" width="960">

👉 Let's `print` "name".

```python
myUser = {"name": "David", "age": 128}

print(myUser["name"])

# This code outputs 'David'.
```

## Changing an item

You can use the `=` syntax to change key values.

<img id="image" src="assets/day40-02.png" alt="Replit Workspace Overview" width="960">


👉 Let's change 'David' to 'The legendary David'

```python
myUser = {"name": "David", "age": 128}

myUser["name"] = "The legendary David"
print(myUser)

# This code outputs 'name:'the legendary David', 'age':'128.
```

### Create your own dictionary!

## Common Errors

First, delete any other code in your `day40.py` file. Copy each code snippet below into `day40.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

### Printing with keys and fStrings

👉 Let's `run` this code and see what happens:

```python
myUser = {"name": "David", "age": 128}

print(f"Your name is {myUser["name"]} and your age is {myUser["age"]}")
```

<details>
<summary>👀 Answer</summary>

- Note that we have to put the keys in single quotation marks `''` inside the fString when using this technique.

- This is because we've already used double quotes to start and end the fString. So, using `""` for the dictionary value would get Python all confuzzled.

```python
myUser = {"name": "David", "age": 128}

print(f"Your name is {myUser['name']} and your age is {myUser['age']}")

# This code outputs 'Your name is David and your age is 128'.
```

</details>

## Syntax error?

👉 Why are you getting a syntax error on the print statement line?

```python
myUser = {"name": "David", "age": 128}

print(myUser{"name"})
```

<details>
<summary>👀 Answer</summary>

- The `print` statement uses square brackets. Curly braces `{}` are only used to call the value.


```python
myUser = {"name": "David", "age": 128}

print(myUser["name"])
```

</details>

## Undefined?

👉 What is the problem here?

```python
myUser = {name: "David", "age": 128}

print(myUser["name"])
```

<details>
<summary>👀 Answer</summary>

- The key, name, in the dictionary should be inside quotes.


```python
myUser = {"name": "David", "age": 128}

print(myUser["name"])
```

</details>

## Spare Key?

👉 What is the problem here?

```python
myUser = {name:"David", "age": 128, "age" = 129}

print(myUser)
```

<details>
<summary>👀 Answer</summary>

- A dictionary can't have two keys with the same name. It always overrides the previous one. Therefore, the 129 overrides the age, 128.


```python
myUser = {name:"David", "age": 128}

myUser["age"] = 129

print(myUser)
```

</details>


## Fix My Code

👉 Try and fix this code which is full of errors.

First, delete any other code in your `day40.py` file. Copy each code snippet below into `day40.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

```python
myUser = {name:"Andy", "age":128, "age" = 129}

print(myUser{"name"})
```


<details>
<summary>👀 Answer</summary>

```python
myUser = {"name":"Andy", "age":128}

myUser["age"] = 129

print(myUser["name"])
```

- The key, `"name"`, needs to be in quotations.
- You can't have two keys with the same value.
- You need `[]` for your `print` statement. `{}` are only used to call the value.

</details>


## 👉 Day 40 Challenge

Today's challenge is to create a contact card using a dictionary.

1. Ask the user to input their name, date of birth, telephone number, email and physical address.
2. Store it all in a dictionary.
3. Print it out in a nice way once its stored.

Example:

```python
🌟Contact Card🌟

Input your name > David Morgan

Input your date of birth > 01/01/1900

Input your telephone number > 01234 567890

Input your email > david@replit.com

Input your address > The Cupboard Under The Stairs, Replit Towers, NY.

Hi David Morgan. Our dictionary says that you were born on 01/01/1900, we can call you on 01234 567890, email david@replit.com, or write to The Cupboard Under The Stairs, Replit Towers, NY.
```


<details>
<summary>💡 Hint</summary>

- You may find `"""` helpful here.
- Don't forget to `.strip()` out any unwanted spaces.
- Pay close attention to when to use `[]` and when to use `{}`.
- For extra fun, try  <a href="https://www.w3schools.com/python/python_dictionaries_add.asp" target="_blank">investigating the</a> `.update()` <a href="https://www.w3schools.com/python/python_dictionaries_add.asp" target="_blank">method</a> for another way of working with dictionaries.


</details>

## Solution (No Peeking!)

<a href="https://www.youtube.com/watch?v=FXegOVAT2e4" target="_blank">Solution video</a>

<details>
<summary>👀 Answer</summary>

```python
name = input("Name: ").strip().capitalize()
dob = input("Date of Birth: ").strip()
tel = input("Telephone number: ").strip()
email = input("Email: ")
address = input("Address: ")
contact = {"name": name, "dob": dob, "tel": tel, "email": email, "address": address}

print()
print(f"""Name: {contact["name"]}""")
print(f"""DOB: {contact["dob"]}""")
print(f"""Tel: {contact["tel"]}""")
print(f"""Email: {contact["email"]}""")
print(f"""Address: {contact["address"]}""")
```

</details>