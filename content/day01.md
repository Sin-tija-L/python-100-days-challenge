# Day1- Welcome!

## Wow, One Hundred Days?!

<a href="https://www.youtube.com/watch?v=ASZVEe2WkI4&t=1s" target="_blank">Dāvida video</a>

Yeah, that's a lot! It's a big commitment, but you'll do great!

Python is a great language for beginners:

- It's easy to learn
- Has an active supportive community
- Offers versatile opportunities in web development, games, data science

Replit is the best place to learn to code because there's zero set up - which means you do not have to download, set up, or install anything. You already did all the work needed because you are here!

All you need to do now is follow along with the video, go from one chapter to the next in this tutorial panel, and just have fun! Now let's go!

# Replit Workspace

- Click on the day01.py file on the left. It should open up the file in the main coding window (#2 below) so we can get starte

<img id="image" src="assets/day01.png" alt="Replit Workspace Overview" width="960">

Let's take a quick tour of the Replit workspace:

1. **Tutorial:** This is accessible from the 📖 (9) icon. You will find video transcript and helper code here.
2. **Files:** If you need to view a different file, just click on it here. This is also where you can upload any assets (pictures, gifs, etc.) to use in your project.
3. **Coding window:** Where you will do most of your typing. All your code will be added here, and you can also view files here.
4. **Console:** Shows you the _output_ of the program (anything we tell our program to show to our users will appear here).
5. **Run:** Will make your code... well, run.
6. **Publish:** Share your code with our community for others to see and remix.
7. **Invite:** Allow someone else to edit your code live in multiplayer.
8. **Hamburger:** Go back to the main menu.
9. This button brings up the tutorial pane if you've closed it.
10. Your video tutorial, play through and pause when asked to build up your coding skills!

# Let's get coding!

Let's start with some simple code to get a simple output (the information the program gives to the user).

👉 Type this line of code in `day01.py` and click `run`.

```python
print("Hello Replit")
```

(HINT: Anytime you see 👉 this means you are going to copy, add or write code in the coding editor).

If everything works as expected your console should now show you your lovely message!

<details>
<summary>💡 Hint</summary>

If you want to feel like a proper hacker, when you've finished writing your code hit `CMD + Enter` to run your code!

</details>

# Our first statement

## Print Statements

You just learned your first command: the `print` statement. It says "Print out whatever's in my brackets". The `print` statement is how you get your program to put messages in the console.

<img id="image" src="assets/day01-1.png" alt="Replit Workspace Overview" width="960">

- The `""` (quotes) are used to tell the command that you're putting text in there (any text you want)
- A bunch of text (or whatever you put in quotes) is called a string.

### Multiple Print Statements

👉 Here is what multiple `print` statements looks like. Copy this code into `day01.py` and hit `run`.

```python
print("Well we")
print("just use more lines")
print("of code")
```

👉 Use the triple quote """ if you want to write a big chunk of text with gaps or line breaks. Add this code to what you have in day01.py and hit run.

```python
print("""Anything that starts
with three quotes, and ends
in three quotes can span
many lines and even contain " symbols
within it without freaking anything out!""")
```

#### You are on your way to being a coder in no time!

# Common Errors

First, delete any other code in your `day01.py` file. Copy each code snippet below into `day01.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free.

Sometimes you get errors when coding. Here are the most popular errors:

## NameError

You'll see this error message if:

- you get the name of a function wrong
- you misspell it
- get the capitalization wrong

👉 Let's try to run this code and see what error message we get. Add this code to your coding editor and hit `run`.

```python
Print("What could go wrong?")
```

What do you think is wrong? It's always important to read the error messages as they try to be helpful.

```python
Traceback (most recent call last):
  File "day01.py", line 1, in <module>
    Print("What could go wrong?")
NameError: name 'Print' is not defined
```

Did you notice the p in `print` is capitalized? `print` is only lower case letters.

## SyntaxError

You will see this message if:

- you have the order of the symbols wrong
- you forget () or " "

👉 We will get an error when we run this code. Copy this code to your coding editor and hit `run`.

```python
print "Hello Again"
```

What do you think is wrong?

```python
  File "day01.py", line 1
    print "Hello Again"
          ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Hello Again")?
```

That's right. You forgot `()`.

👉 What is causing the error here? Copy the code and hit `run` to find out.

```python
print(Please work)
```

```python
File "day01.py", line 1
    print(Please work)
                 ^
SyntaxError: invalid syntax
```

You need `" "`.

#### You will only get better at debugging by practicing! You'll find lots of errors in your own code as you go, so make sure you get practice by trying all the "Fix my code" activities whenever you see them!

# Fix my code!

👉 Try and fix this code which is full of errors.

First, delete any other code in your `day01.py` file. Copy each code snippet below into `day01.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the 👀 `Answer` to compare your code to the correct code.

```python
print(= MUSIC+ =)
print("> Songs"
Print("> Albums")
print(> Artists")
```

<details>
<summary>👀 Answer</summary>

```python
print("= MUSIC+ =")
print("> Songs")
print("> Albums")
print("> Artists")
```

_It does not matter if you use capital letters or lowercase letters for your string. Just be consistent._

</details>

# Here is your challenge for Day 1

## Project 1: Print into the World

_Let's get started with your first project! After only one day, you already have something you can share with the world._

_You can continue to use this same repl for your project. Just make sure you delete any previous code from our practice session._

1. Write your `full name` and `today's date` in separate lines of code.

<details>
<summary>💡 Hint</summary>

Don't forget `""` and `()` when creating your print statements.

</details>

2. Copy this text below. See if you can do it with just the one `print` statement!

```python
I am signing up for Replit's 100 days of Python challenge!
I will make sure to spend some time every day coding along, for a minimum of 10 minutes a day.
I'll be using Replit, an amazing online IDE so I can do this from my phone wherever I happend to be. No excuses for not coding from the middle of a field!
```

<details>
<summary>💡 Hint</summary>

Remember you can use triple quotes for a large block of text. `"""`

</details>

3. On the next line add I am feeling with an emoji of your choice to illustrate how you're feeling about the challenge.

4. Add one more line to your output You can follow my progress at replit.com/@ and add in your Replit username. This will be a great way of maintaining accountability for yourself!

5. Run your program.

# Solution (No peeking!)

<details>
<summary>👀 Answer</summary>

```python
print("Marky")
print("September 20, 2029")
print("""I am signing up for Replit's 100 days of Python challenge!
I will make sure to spend some time every day coding along, for a minimum of 10 minutes a day.
I'll be using Replit, an amazing online IDE so I can do this from my phone wherever I happen to be. No excuses for not coding from the middle of a field!""")
print("I am feeling 🥳")
print("You can follow my progress at replit.com/IamMarkProbably")
```

</details>
