# Day15 - All About Loops

<a href="https://www.youtube.com/watch?v=AwCI7IG-i38" target="_blank">Dāvida video</a>

On Day 14, you created an epic rock, paper, scissors game, but we had to click `run` every time (which makes for a terrible experience!) Let's fix that with a `while` loop...

## While Loop

A `while` loop allows your code to repeat itself based on a condition you set.

It is similar to an `if` statement in that you ask a question, and as long as the answer is true, the computer will repeatedly run the code.

<img id="image" src="assets/day15.png" alt="Replit Workspace Overview" width="960">

In the code below, the variable is called `counter` and starts at zero. The `while` loop has the condition saying, "while the counter is less than ten do this..."

In this case, `print` the variable and then add `+=1` to that variable. As long as variable is less than 10, the loop will repeat the code.

```python
counter = 0
while counter < 10:
  print(counter)
  counter +=1
```

### 👉 Try it out!

## Infinite Loop

You have to be really careful that you don't accidentally invoke an infinite loop! This is where the computer will loop code until the end of time. Without a break. Forever. 😭

### Fix an infinite loop by adding:

```python
  variable +=1
```

This is just saying "count to 10 by 1 each time." to make the loop end.

Don't forget, if your condition is a `>` then you might need to `-=`. This will subtract from the variable instead of adding to it.

## 👉 Try it out

```python
counter = 0
while counter < 10:
  print(counter)
  counter +=1
```

Can you extend this code to print to 100?

<details>
<summary>💡 Hint</summary>

Think about your `while` condition.

</details>

## Common Errors

First, delete any other code in your `day15.py` file. Copy each code snippet below into `day15.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

## Infinite Loop

`Run` this code. What happens?

```python
counter = 0
while counter < 10:
  print(counter)
```

<details>
<summary>👀 Answer</summary>

You see a series of infinite 0s printing over and over. Why? You have created an infinite loop because the counter will always be less than 10 in this case. Manually stop the program and specify `counter +=1`.

```python
counter = 0
while counter < 10:
  print(counter)
  counter += 1
```

</details>

## Nothing happens...

`Run` this code. What goes wrong?

```python
counter = 0
while counter > 6:
  print(counter)
  counter += 1
```

<details>
<summary>👀 Answer</summary>

The issue is the condition. It is the wrong way around. The inequality is saying when the counter is greater than 6 to add one. However, the counter is 0. Therefore, it is not greater than six to start.

Fix this by sorting out the inequality to `<`.

</details>

## Exit

You can use a `while` loop with text too. In the code below, the while condition is saying "as long as you do not type yes, the computer will type 🥳."

`Run` this code. What do you see?

```python
exit = ""
while exit != "yes":
  print("🥳")
exit = input("Exit?: ")
```

<details>
<summary>👀 Answer</summary>

Wait! No matter what you type, you get 🥳. Check your indentation. Change the variable that controls the condition within the loop itself.

```python
exit = ""
while exit != "yes":
  print("🥳")
  exit = input("Exit?: ")
```

</details>

## 👉 Fix My Code

👉 Try and fix this code which is full of errors.

First, delete any other code in your `day15.py` file. Copy each code snippet below into `day15.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

```python
counter = 0
while counter < 25:
  print(counter)
```

<details>
<summary>👀 Answer</summary>

```python
counter = 0
while counter < 25:
  print(counter)
  counter +=1
```

</details>

```python
counter = 0
while counter >= 12:
  print(counter)
  counter += 1
```

<details>
<summary>👀 Answer</summary>

```python
counter = 0
while counter <= 12:
  print(counter)
  counter += 1
```

</details>

```python
exit = ""
while exit = "yes":
  print("🥳")
exit = input("Exit?: ")
```

<details>
<summary>👀 Answer</summary>

```python
exit = ""
while exit != "yes":
  print("🥳")
  exit = input("Exit?: ")
```

</details>

## 👉 Day 15 Challenge

Write a program that loops. Inside the loop, ask the user what animal sound they want to hear.

### Example

```python
What animal do you want?: Cow
A cow goes moo.

Do you want to exit?: no

What animal do you want?: A Lesser Spotted lemur
Ummm...the Lesser Spotter Lemur goes awooga.

Do you want to exit?: yes
```

<details>
<summary>💡 Hint</summary>

- You will need to start with a while loop.
- Add nested if statements inside the while loop.
- End with exit for the user to get out of the loop.

</details>

In case you are curious...check out the <a href="https://www.amazon.com/Rain-Labs-Animal-Sounds/dp/B01AHGU3M6" target="_blank">Alexa skill</a> David mentioned in the video.

## Solution (No Peeking!)

<details>
<summary>👀 Answer</summary>

```python

exit = "no"


while exit == "no":
  animal_sound = input("What animal sound do you want to hear?")

  if animal_sound == "cow" or animal_sound == "Cow":
    print("🐮 Moo")
  elif animal_sound == "pig" or animal_sound == "Pig":
    print ("🐷 Oink")
  elif animal_sound == "sheep" or animal_sound == "Sheep":
    print ("🐑 Baaa")
  elif animal_sound == "duck" or animal_sound == "Duck":
    print("🦆 Quack")
  elif animal_sound == "dog" or animal_sound == "Dog":
    print("🐶 Woof")
  elif animal_sound == "cat" or animal_sound == "Cat":
    print("🐱 Meow")
  else:
    print("I don't know that animal sound. Try again.")


  exit = input("Do you want to exit?: ")
```

</details>
