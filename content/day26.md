# 👉 Day 26: os Library

<a href="https://www.youtube.com/watch?v=_IGpC-sA7M4" target="_blank">Dāvida video</a>


What is the os library?

It allows us to "talk" to the console. One of the most powerful things we can do with this library is allow it to clear the console.

## Import the os library

👉 Well, this just prints a list of numbers to 1,000...

```python
import os
for i in range(1,1000):
  print(i)
```

### Adding os.system

We can clear the code above by using the `os.system` function to 'clear' the console.

<img id="image" src="assets/day26.png" alt="Replit Workspace Overview" width="960">

👉 Add this to the code above: (remember to indent this properly)

```python
os.system("clear")
```

Do you notice how it clears the console? Cool, right?!

## Let's try one more...

👉 For this code, I want the program to say "Welcome to Replit!", delete that, and then ask for my username on a blank screen. Remove the previous code, add the code below and see what happens when you hit `run`!

```python
import os
print("Welcome")
print("to")
print("Replit")
os.system("clear")
username = input("Username: ")
```

Wow! The console printed and cleared 'Welcome to Replit!' before I even had a chance to read it.

### Let's fix that with another library.

## Time Library

We can import a second library by placing a `,` after the name of the first library.

👉 Let's add a second library, time.

```python
import os, time
```

This library allows us to pause the execution of a program for a specific amount of time.

<img id="image" src="assets/day26-01.png" alt="Replit Workspace Overview" width="960">

The `time.sleep(1)` function allows us to pause the program for the amount of seconds listed in the `()`.

👉 Add this to your code before the program is cleared to pause the program for 1 second before displaying the username.

```python
time.sleep(1)
os.system("clear")
```

### Try it out with other amounts of time and see what happens.

## 👉 Day 26 Challenge

Play a song from this repl and build a menu to go with it. Make it look like an iPod!

When you run the code below, it should open the Output tool which will have a checkbox with a headphones icon in the bottom right corner. Select this checkbox to hear the sound. (It may be behind the video.)

- Use a `while true` loop to create a title for a music player.
- Allow the user to select to play a song and use subroutine called 'play' when they select the song.
- Give the user the option to exit the program.
- The title should pop up and pause along with the menu options.
- If the user chooses anything else, start again by clearing the screen.

Use this code to get started:

```python
import os
import time

import pygame

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('audio.wav')
sound.play()

def pause():
  pygame.mixer.pause()

pause()

def play():
  # Play the sound
  pygame.mixer.unpause()
  while True:
    # Start taking user input and doing something with it
    input()

while True:
  # clear the screen

  # Show the menu

  # take user's input

  # check whether you should call the play() subroutine depending on user's input
  if True:
    play()
```

###  To `run` code we have to use VS Code terminal not browser.

<img id="image" src="assets/day26-04.png" alt="Replit Workspace Overview" width="960">


1. Add new terminal with `+` sign. 
2. Run in VS Code terminal → project root folder:  `python python_files/day26.py`

Here is an example:

```python
🎵 MyPOD Music Player

Press 1 to Play
Press 2 to Exit

Press anything else to see the menu again.
```

<details>
<summary>💡 Hint</summary>

- Import your libraries first.
- With the sample code above, think about what code can be added to pause and play the audio.
- What command do you need to use to return (hint, hint) to the main menu (subroutine)?
- Create a `while True` loop that clears the code and pauses the code. What libraries would you need for these things to happen?
- You may also need `if` statements within your loop.

</details>

## Solution (No Peeking!)

<details>
<summary>👀 Answer</summary>

```python
import os
import time

import pygame

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('assets/audio.wav')
sound.play()
pygame.mixer.pause()

def pause():
  pygame.mixer.pause()

pause()

def play():
  # Play the sound
  pygame.mixer.unpause()
  while True:
    stop_playback = int(
        input("Press 2 anytime to pause playback and go back to the menu: "))
    if stop_playback == 2:
      pause()
      return  # let's go back from this play() subroutine
    else:
      continue

while True:
  os.system("clear")
  print("🎵 MyPOD Music Player ")
  time.sleep(1)
  print("Press 1 to Play")
  print("Press 2 to Exit")
  print("Press anything else to see the menu again")
  userInput = int(input())
  if userInput == 1:
    print("Playing some proper tunes!")
    play()
  elif userInput == 2:
    exit()
  else:
    continue
```

</details>

## !NB 

Ja nestrādā `pygame`, tad nepieciešams to instalēt lokāli. Atveram VS CODE `terminal` un veicam sekojošus soļus:

<img id="image" src="assets/day26-06.png" alt="Replit Workspace Overview" width="960">


```python

1. python3 -m pip install pygame
2. python3 -c "import pygame"


```

Ja pēc instalācijas joprojām nestrādā `pygame`, tad veicam vēl sekojošas darbības: 

```python
1. VS CODE atveram komandu paleti (Cmd+Shift+P on Mac or Ctrl+Shift+P on Windows/Linux).
2. Rakstām:  "Python: Select Interpreter".
3. Izvēlamies variantu, kur ir mūsu - myenv, piemērs zemāk attēlā.
```
 
<img id="image" src="assets/day26-07.png" alt="Replit Workspace Overview" width="960">

Šajā uzdevumā run pogu neizmantojam. 
