# Day17 - Another Cheat

<a href="https://www.youtube.com/watch?v=e5048kp-ogk" target="_blank">Dāvida video</a>

So far we've used `break` in the `while True` loop. `break` leaves the loop completely and runs the next unindented line of code. However, you may want to stop the code and start the loop from the top again. (This is ideal for building games!)

<img id="image" src="assets/day17.png" alt="Replit Workspace Overview" width="960">

In the code below, the game runs and the user is asked if they want to go left or right. If the user chooses left, they fall to their death, and `break` will kick the user out of the loop. That's the game.

```python
while True:
  print("You are in a corridor, do you go left or right?")
  direction = input("> ")
  if direction == "left":
    print("You have fallen to your death")
    break
```

### Well that's a bit lame and not any different than what we learned in day 16...now for the cheat.

## The Continue Command

The `continue` command stops executing code in the loop and starts at the top of the loop again. Essentially, we want to kick the user back to the original question.

<img id="image" src="assets/day17-01.png" alt="Replit Workspace Overview" width="960">

Adding `continue` will start the code from the start and ask the first question again: _"Do you go left or right?"._

```python
while True:
  print("You are in a corridor, do you go left or right?")
  direction = input("> ")
  if direction == "left":
    print("You have fallen to your death")
    break
  elif direction == "right":
    continue
  else:
    print("Ahh! You're a genius, you've won")
```

The `else` statement refers to any input besides left or right (up or esc). Since the user is a winner, we do not want to use `break` or it would say they have failed.

### So how do we make it stop?

## Proceed to the Nearest Exit

The previous code continues to loop even after the user has won. Let's fix that with the `exit()` command
day

<img id="image" src="assets/day17-02.png" alt="Replit Workspace Overview" width="960">

The `exit()` command completely stops the program and it will not run any more lines of code.

### 👉 Copy all the code and try it out. Does it do what you expected?

```python
while True:
  print("You are in a corridor, do you go left or right?")
  direction = input("> ")
  if direction == "left":
    print("You have fallen to your death")
    break
  elif direction == "right":
    continue
  else:
    print("Ahh! You're a genius, you've won")
    exit()
print("The game is over, you've failed!")
```

# Common Errors

First, delete any other code in your `day17.py` file. Copy each code snippet below into `day17.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

👉 What is wrong here?

```python
while True:
  print("You are in a corridor, do you go left or right?")
  direction = input("> ")
  if direction == "left":
    print("You have fallen to your death")
    break
  elif direction == "right":
    continue
  else:
    print("Ahh! You're a genius, you've won")
    exit
print("The game is over, you've failed!")
```

<details>
<summary>👀 Answer</summary>

`exit` is a function and needs `()`. The moment you add the `()` you notice the color change of `exit` from white to yellow.

```python
while True:
  print("You are in a coridoor, do you go left or right?")
  direction = input("> ")
  if direction == "left":
    print("You have fallen to your death")
    break
  elif direction == "right":
    continue
  else:
    print("Ahh! You're a genius, you've won")
    exit ()
print("The game is over, you've failed!")
```

</details>

## Fix My Code

👉 Try and fix this code which is full of errors.

First, delete any other code in your `day17.py` file. Copy each code snippet below into `day17.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

```python
print("Let's play chutes and ladders. Pick ladder or chute.")
while True:
  print("Do you want to go up the ladder or down the chute?")
  direction = input("> ")
  if direction == "chute"
    print("Game over!")
  break
  elif direction == "ladder":
    continue
else:
    print("Game over!")
    exit
print("Thanks for playing!")
```

<details>
<summary>👀 Answer</summary>

```python
print("Let's play chutes and ladders. Pick ladder or chute.")
while True:
  print("Do you want to go up the ladder or down the chute?")
  direction = input("> ")
  if direction == "chute":
    print("Game over!")
    break
  elif direction == "ladder":
    continue
  else:
    print("Game over!")
    exit ()
print("Thanks for playing!")
```

</details>

## 👉 Day 17 Challenge

Go find your Rock, Paper, Scissors game from Day 14 and add the code here before you start. We are going to build upon this game.

1. Use a loop to repeat the game multiple rounds.
2. Keep score of player 1 and player 2.
3. End the game when a player wins three rounds using `break` and `exit`.
4. Use `continue` to restart the round until one player wins three rounds.
5. Your last bit of code should be the results of which player won.

<details>
<summary>💡 Hint</summary>

- Create a counting system using a variable and `+=` to keep track of the winner for each round.
- The `while` loop needs to be at the start of the game.
- Make sure you include `print` statements saying each player's final score at the end.
- Create an `if` statement to end the loop.

</details>

### You have created your first game involving scoring. Well done!

## Solution (No Peeking!)

<details>
<summary>👀 Answer</summary>

```python
print("E P I C    🪨  📄 ✂️    B A T T L E ")
print()
print("Select your move (R, P or S)")
print()
#hint: create these variables outside loop and then add += with correct player to keep score throughout
player1_score = 0
player2_score = 0
#hint: that the while loop needs to go around all code and then highlight the rest of the code and hit tab once.
while True:
  player1Move = input("Player 1 > ")
  print()
  player2Move = input("Player 2 > ")
  print()

  if(player1Move=="R"):
    if(player2Move=="R"):
      print("You both picked Rock, draw!")
    elif(player2Move=="S"):
      print("Player1 smashed Player2's Scissors into dust with their Rock!")
      player1_score += 1
    elif(player2Move=="P"):
      print("Player1's Rock is smothered by Player2's Paper!")
      player2_score += 1
  elif(player1Move=="P"):
    if(player2Move=="R"):
      print("Player2's Rock is smothered by Player1's Paper!")
      player1_score += 1
    elif(player2Move=="S"):
      print("Player1's Paper is cut into tiny pieces by Player2's Scissors!")
      player2_score += 1
    elif(player2Move=="P"):
      print("Two bits of paper flap at each other. Dissapointing. Draw.")
  elif(player1Move=="S"):
    if(player2Move=="R"):
      print("Player 2's Rock makes metal-dust out of Player1's Scissors")
      player2_score += 1
    elif(player2Move=="S"):
      print("Ka-Shing! Scissors bounce off each other like a dodgy sword fight! Draw.")
    elif(player2Move=="P"):
      print("Player1's Scissors make confetti out of Player2's paper!")
      player1_score += 1

# hint: make sure you add player scores at the end of all the options but still inside the while loop.
  print("Player 1 has", player1_score, "wins.")
  print("Player 2 has", player2_score, "wins.")

  if player1_score==3 or player2_score==3:
    print("Thanks for playing!")
    exit()
  else:
    continue
```

</details>
