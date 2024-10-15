# 👉 Day 59 Challenge: A Man A Plan A Canal Panama!

<a href="https://youtu.be/ONBbX6Qz2k4" target="_blank">📹 Dāvida video</a>

Today's challenge is all about [palindromes](https://en.wikipedia.org/wiki/Palindrome).

A palindrome is a word that is symmetrical, (i.e. it reads the same backwards as forwards).

For example:
- racecar
- madam
- radar

Now that you know what a palindrome is, just go back and have a look at this page title. The one that made you go, *huh?!* Got it now? Sweet!


### Hop over to the challenge for details!

You're going to write a program that checks a string to see if it is a palindrome.

Yes. We know that Python has the built in function `string.reverse()` that you could use.

Zero points for that today, we want you to think hard and utilize your skills in:
- recursion
- string slicing
- looping

Your program should:
- Prompt the user to input a word.
- Analyze the word to see if it is a palindrome.
- Output a relevant 'yes/no message.

**Example:**

<img id="image" src="assets/day59_1.png" alt="Replit Workspace Overview" width="960">

<details>
<summary>💡 Hints</summary>

This is a tough one, so I've given you some hints about the algorithmic thinking needed for a problem like this:
- Don't forget to standardize the case on input.
- Think about which characters in a word are compared first. Check if they are the same.
- If they've been compared and are the same, remove them and repeat the process with the shorter string.
- Keep going until you're down to a string of length 1 or 0 (depending on whether the original word had an odd/even number of characters. If you get to this point, then you've got a palindrome.)

</details>


## Solution (No Peeking!)

<a href="https://youtu.be/Dr_dGJEt-dA" target="_blank">Solution video</a>

<details>
<summary>👀 Answer</summary>

```python
def palindromeChecker(word):
    newWord = word.strip().lower()
    reversedWord = newWord[::-1]
    return newWord == reversedWord

print("🌟Palindrome Checker🌟")
print()
word = input("Input a word > ")
print()
isPalindrome = palindromeChecker(word)
print(f"Is {word} a palindrome? {isPalindrome}")
```

</details>