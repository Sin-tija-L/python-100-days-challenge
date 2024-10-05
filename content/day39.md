# 👉 Day 39 Challenge: Hangman

<a href="https://www.youtube.com/watch?v=g2Go3XS3VZg" target="_blank">Dāvida video</a>


This simple game is actually pretty complex. This hangman project combines lists, string manipulation, and slicing, along with other concepts.

It's a bit of a step up, so don't be afraid to check hints and solutions if you're getting stuck. Also, check out our <a href="https://replit.com/community-hub" target="_blank">100 Days of Code forum</a>  for help.

### Picking from a list randomly

👉 `random.choice()` picks a random item from a list.

Here's a list of words:

`listOfWords = ["british", "suave", "integrity", "accent", "evil", "genius", "Downton"]`

To select randomly from this list, we assign `random.choice()` to a variable. We give `random.choice()` the name of the list in the brackets.

```python
listOfWords = ["british", "suave", "integrity", "accent", "evil", "genius", "Downton"]

wordChosen = random.choice(listOfWords)
```

There's lots of other stuff needed to make this program work, but, we'll break that down in the challenge section of today's tutorial.

### Try it out and get randomizing!

## 👉 Day 39 Challenge

Once the word has been picked, the following things need to happen:

1. Prompt the user to type in a letter.
2. Check if the letter is in the word.
3. If it does, output the word with all blanks apart from the letter(s) they've already guessed.
4. Keep a running list of the letters they've used.
5. Count how many times they've picked a letter that isn't in the word - more than 6 and they lose.
6. Output a 'win' message if they reveal all the letters.

🥳 Extra points for using <a href="https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c" target="_blank">ASCII art</a>  to draw the hangman as the player makes incorrect guesses.

Example:

```python
🌟Hangman🌟

Choose a letter: i
Nope, not in there.
5 left.

Choose a letter: a
Correct!
__a__

Choose a letter: s
Correct!
s_a__

Choose a letter: u
Correct!
sua__

# Repeat until.....
# If user wins
You won with 5 lives left.

# Loses
You lost!
```

### To run this code use terminal and run the file (now you know how it should be done 😎)


<details>
<summary>💡 Hint</summary>

- Check if a letter is in the string: `if inputLetter in string`.
- Try using underscores to show blanks to let the user know how many more letters there are to guess.
- Keep track of letters used. Try adding each letter chosen to a new list, then checking this list for each subsequent choice.
- Check out our <a href="https://replit.com/community-hub" target="_blank">100 Days of Code forum</a> for help.

</details>


## Solution (No Peeking!)

<a href="https://www.youtube.com/watch?v=UH3vIwOPXA0" target="_blank">Solution video</a>

<details>
<summary>👀 Answer</summary>

```python
import random, os, time

listOfWords = ["apple", "orange", "grapes", "pear"]
letterPicked = []
lives = 6

word = random.choice(listOfWords)

while True:
  time.sleep(1)
  os.system("clear")
  letter = input("Choose a letter: ").lower()
  
  if letter in letterPicked:
    print("You've tried that before")
    continue
    
  letterPicked.append(letter)
  
  if letter in word:
    print("You found a letter")
  else:
    print("Nope, not in there")
    lives -= 1
  
  allLetters = True
  print()
  for i in word:
    if i in letterPicked:
      print(i, end="")
    else:
      print("_", end="")
      allLetters = False
  print()

  if allLetters:
    print(f"You won with {lives} left!")
    break

  if lives<=0:
    print(f"You ran out of lives! The answer was {word}")
    break
  else:
    print(f"Only {lives} left")
```

</details>

Šajā uzdevumā run pogu neizmantojam. 
