# 👉 Day 18 Challenge

<a href="https://www.youtube.com/watch?v=ox5KGtrXs5E" target="_blank">Dāvida video</a>

We are going to build a "Guess the Number" guessing game.

You are going to use a `while` loop and some of the concepts from the past few days.

1. Start by picking a number between 0 and 1,000,000. This will be your first variable.

<details>
<summary>💡 Hint</summary>

Essentially, what do you want the correct number to be. Create a variable for that number.

</details>

2. Create a `while` loop to keep asking the user to guess your number.

3. If they are too low, tell them "too low." If they guess too high tell, them "too high."

<details>
<summary>💡 Hint</summary>

You will need to include `if` statements here with logical operators. Include the correct number variable you created at the beginning in these `if` statements.

</details>

4. If the user guesses correctly, tell them they are a winner (maybe add a fun emoji too!)

<details>
<summary>💡 Hint</summary>

If they are a winner, they need to get out of the loop. How do you do that?

</details>

5. Count the number of attempts it took for the user to guess number. Make sure you only show that after they get the answer correct.


<details>
<summary>💡 Hint</summary>

Create a counter before the `while` loop and `print` the number of attempts after the user is a winner. Don't forget to count attempts using `+= `in the loop.


</details>

Extra challenge: If the user types a negative number, exit program.

## Solution (No Peeking!)


<details>
<summary>👀 Answer</summary>

```python
print("Welcome to Guess the Number.")
print()
print("Guess a number between 1 and 1,000,000 and I will tell you if you are too low, too high, or get it correct.")
print()
print("Let's play!")

correct_number = 2300
attempt = 1

while True:
  user_guess = int(input("Pick a number between 1 and 1,000,000: "))
  if user_guess < 0:
    print("Now we'll never know what the answer is …")
    exit()
  if user_guess < correct_number:
    print("That number is too low. Try again!")
    attempt += 1
  elif user_guess > correct_number:
    print("That number is too high. Try again!")
    attempt += 1
    continue
  elif user_guess == correct_number:
    print("You are a winner! 🥳🥳")
    break 
  else:
    print("That is not a number I recognize.")
print("It took you", attempt, "attempt(s) to get the correct answer.")
```

</details>