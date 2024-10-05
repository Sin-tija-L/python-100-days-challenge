# 👉 Day 8 Challenge

<a href="https://www.youtube.com/watch?v=3SXW63IIs4I" target="_blank">Dāvida video</a>


## Affirmations (or insults) Generator

Today's focus is using all the skills you have learned so far:

- input and output
- concatenation
- if statements
- nested if statements

Build a custom affirmations generator to give the user a customized affirmation each day of the week.

1. Make sure you ask the user for their name, the current day of the week, and a few of their favorite things. All of this information should be used to help you build your affirmations.

<details>
<summary>💡 Hint</summary>
Think of these as variables.
</details>

2. The goal is to generate a unique message for each day of the week based on the user's answers.

<details>
<summary>💡 Hint</summary>
use `if` and nested `if` statements
</details>

3. Use concatenation to generate the affirmation.

4. If affirmations are not your jam, then you could do a daily joke or insult. Please don't be mean. Keep it light and funny.

5. Final challenge: Can you create if statements that do not care about capital or lowercase letters of names.

<details>
<summary>💡 Hint</summary>
Don't forget to restate the full question. `name ==`. The next chapter will explain this.

</details>


## Common Error with If Statements

Here is a common error when joining if statements using logical conditions `and` `or` `not`.

In this example, I am trying to ignore the capitalization of the name for saying hi to Dave with `or`.

```python
name = input("Name: ")
if name == "Dave" or "dave":
  print("Hi Dave")
```

The computer does not read the if statement in the same way a person does. The left side is saying "If the name is equal to Dave", but the computer reads the right side as saying "Does Dave exist?"

Here is how we fix this:


We need to restate the full question.

```python
name = input("Name: ")
if name == "Dave" or name == "dave":
  print("Hi Dave")
```

## Solution (No Peeking!)

<details>
<summary>👀 Answer</summary>

```python 
print("Hello. Welcome to your daily affirmation generator.")
name = input("What is your name? ")


if name =="Mark" or name == "mark":
 DOW = input("What is the day of the week? ")
 if DOW == "monday" or DOW == "Monday":
   print("It is going to be a great Monday", name)
 if DOW == "tuesday" or DOW == "Tuesday":
   print("What a wonderful Tuesday it is", name)
 if DOW == "wednesday" or DOW == "Wednesday":
   print("Happy Hump Day", name)
 if DOW == "thursday" or DOW == "Thursday":
   print(name,"your week is almost over!")
 if DOW == "friday" or DOW == "Friday":
   print(name, "It's FRIDAY!")

elif name == "David" or name== "david":
 DOW = input("What is the day of the week? ")
 if DOW == "monday" or DOW == "Monday":
   print("It is going to be a great Monday", name)
 if DOW == "tuesday" or DOW == "Tuesday":
   print("You look great in that color", name)
 if DOW == "wednesday" or DOW == "Wednesday":
   print("You look chipper today", name)
 if DOW == "thursday" or DOW == "Thursday":
   print(name,"you are doing a great job!")
 if DOW == "friday" or DOW == "Friday":
   print(name, "it's FRIDAY!")
else:
 print("I do not know your name, but I hope you are having a great day!")
```

</details>