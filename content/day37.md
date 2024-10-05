# 👉 Day 37: String Slicing

<a href="https://www.youtube.com/watch?v=0fJNVerQaNI" target="_blank">Dāvida video</a>


Aren't strings brilliant? Yes, yes they are.

However, sometimes we might want to take part of a string to use it somewhere else. Sometimes, we might want to look at just the first letter of a string or chop it into chunks.

To do this, we use string slicing.

A string isn't just one big lump of text. In fact it's a list of individual characters. This means that we can use indexing just like we did with lists waaay back on Day 32.

By giving our program an index, we can specify which part of the string to chop out. 🪓🪓

Pssst... When you see '#' followed by green text, these are comments for you. The computer will ignore it.

### Slicing
To slice a single character from a string, you use the index of that character in square brackets `[]` just like you'd use with a list! Gasp!

👉 Let's see what happens:

```python
myString = "Hello there my friend."
print(myString[0])

# This code outputs the 'H' from 'Hello'
```

To slice more than one character, you use two indices (yes that is the plural form of 'index'): the start character and one after your desired end character.

<img id="image" src="assets/day37.png" alt="Replit Workspace Overview" width="960">

👉 Let's try it:

```python
myString = "Hello there my friend."
print(myString[6:11])

# This code outputs 'there'.
```

👉 Leaving the first index blank defaults to 'start from index 0'.

```python
myString = "Hello there my friend."
print(myString[:11])

# This code outputs 'Hello there'.
```

👉 Leaving the last index blank defaults to 'go to the end'.

```python
myString = "Hello there my friend."
print(myString[12:])
# This code outputs 'my friend.'.
```
### Try it out and see what you can slice!

## The Secret Third Argument

Adding a third argument to the square brackets `[]` specifies the gap left between characters.

<img id="image" src="assets/day37-01.png" alt="Replit Workspace Overview" width="960">

👉 Try to `print` every other character in the word 'hello':

```python
myString = "Hello there my friend."
print(myString[0:6:2])

# This code outputs 'Hlo' (every second character from 'Hello').\
```

👉 Can you `print` every third character in the whole string?

```python
myString = "Hello there my friend."
print(myString[::3])

# This code outputs 'Hltrmfe!' (every third character from the whole string).
```

Using a negative number in the third argument can be super useful. It starts the slice from the end of the string instead of the beginning.

👉 Can you `print` the string backwards?!

```python
myString = "Hello there my friend."
print(myString[::-1])

#This code reverses the string, outputting '.dneirf ym ereht olleH'
```

### Play around with this third secret argument. What else can you do?

## Split

👉 `split` lets us split a string into a list of individual words by separating it at the space characters.

```python
myString = "Hello there my friend."
print(myString.split())

#This code outputs ['Hello', 'there', 'my', 'friend.']
```

### What can you split?

## Common Errors

First, delete any other code in your `day37.py` file. Copy each code snippet below into `day37.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

### It stops printing too early

👉 Why is it printing 'Hell' instead of 'Hello'?

```python
myString = "Hello there my friend."
print(myString[0:4])
```


<details>
<summary>👀 Answer</summary>

- The second argument should always be one more than the index of the final character.

```python
myString = "Hello there my friend."
print(myString[0:5])
```

</details>

## It won't stop printing the same character

👉 What is the problem here?

```python
myString = "Hello there my friend."
print(myString[0:4:0])
```

<details>
<summary>👀 Answer</summary>

The 0 in the third argument means 'move on 0 characters in the string each time'. You've told it to print the same character again and again and again....

The third argument should be `at least 1`.


```python
myString = "Hello there my friend."
print(myString[0:4:1])
```

</details>

## Fix My Code

👉 Try and fix this code which is full of errors.

First, delete any other code in your `day37.py` file. Copy each code snippet below into `day37.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

```python
# This code should output 'Hello there'
myString = "Hello there my friend."
print(myString[0:10:0])
```

<details>
<summary>👀 Answer</summary>

```python
myString = "Hello there my friend."
print(myString[0:11])
```

OR 

```python
myString = "Hello there my friend."
print(myString[0:11:1])
```

</details>

## 👉 Day 37 Challenge

This is the challenge you're looking for. This program will generate your Star Wars Name.

1. Ask the user to input their first & last names.
2. Slice the first 3 letters of the first name.
3. Slice the first 3 letters of the last name (surname).
4. Join them together. Ideally change the case so that it looks good - think fStrings or `.upper()/.lower()`. This is the user's Star Wars first name.
5. Now ask the user for their mother's maiden name and the city where they were born. (Maiden name is the last name they had before they got married. If you are not sure, make up a last name.)
6. Combine the first two letters of the maiden name with the last 3 letters of the city to make the user's Star Wars last name. Remember, fStrings and `.upper()/.lower().`
7. Finally, `print` them both as part of a sentence.

🥳 Extra points for getting all the `inputs` with just one input command and the `split` function.

Example:

```python
🌟Star Wars Name Generator🌟

Input your first name > David

Input your lastname > Morgan

Input your mother's maiden name > Jones

Input the city where you were born > Cardiff

Your Star Wars name is Davmor Joiff
```

<details>
<summary>💡 Hint</summary>

- To get charaters from the beginning of a string, leave the first argument blank. ex: [:3] gets the first 3 characters.
- To get charaters from the end of a string, make the first argument a negative number for how many charaters to get. Leave the last argument blank. ex: [-5:] gets the last 5 characters.
- fString formatting uses `.title` for first character capitalization and `.lower` for all lower case.
- Use fStrings to join the sliced characters to a new variable as you get the correct characters from each string.
- For extra points, get the user to input all info at once separated by spaces.

</details>

## Solution (No Peeking!)

<a href="https://www.youtube.com/watch?v=hdKPin7DQrc" target="_blank">Solution video</a>

<details>
<summary>👀 Answer</summary>

```python
print("STAR WARS NAME GENERATOR")

all = input("Enter your first name, last name, Mum's maiden name and the city you were born in").split()

first = all[0].strip()
last = all[1].strip()
maiden = all[2].strip()
city = all[3].strip()

name = f"{first[:3].title()}{last[:3].lower()} {maiden[:2].title()}{city[-3:].lower()}"

print(f"Your Star Wars name is {name}")
```

</details>