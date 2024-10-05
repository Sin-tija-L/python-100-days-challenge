# 👉 Day 27 Challenge

<a href="https://www.youtube.com/watch?v=jCtk6DZLHoQ" target="_blank">Dāvida video</a>

Welcome to your first video game creation. You will create a video game that creates a character's health and attack stats...along with an epic name for your character.

**Do not delete today's code. You will be building upon it on Day 28.**

- Write a subroutine that generates a character: first name and character type (human, imp, wizard, elf, etc.).
- Write a subroutine that multiplies a bunch of random dice rolls together to generate the character's health stats. Use this formula:

<img id="image" src="assets/day27.png" alt="Replit Workspace Overview" width="960">

- Write a second subroutine that multiplies a bunch of random dice rolls together to generate the character's strength stats. Use this formula:

<img id="image" src="assets/day27-01.png" alt="Replit Workspace Overview" width="960">

- Present the data in a menu with `time.sleep` and `os.system("clear")` to make it appealing.
- Wrap it in a loop so the user has the option to create another character.

Example:

```python
Character Builder

Name Your Legend:
Sheila the Almighty

Character Type (Human, Elf, Wiard, Orc):
Human

Sheila the Almighty
HEALTH: 40
STRENGTH: 26

May your name go down in Legend...
```

<details>
<summary>💡 Hint</summary>

- Import libraries first. You will need to use all three libraries you have learned so far.
- You will need four subroutines: character name and type, to create a random sided dice, for the formula to generate health, and for the formula to generate strength. You will `return` each subroutine.
- Create a `while` loop that allows the player to choose to play again, clears the code, and pauses it when needed (think about your libraries).

</details>

## Solution (No Peeking!)

<a href="https://www.youtube.com/watch?v=r2SThdlG7j0" target="_blank">Solution video</a>

<details>
<summary>👀 Answer</summary>

```python
import random, os, time

def rollDice(side):
  result = random.randint(1,side)
  return result

def health():
  healthStat = ((rollDice(6)*rollDice(12))/2)+10
  return healthStat

def strength():
  strengthStat = ((rollDice(6)*rollDice(8))/2)+12
  return strengthStat

while True:
  print("⚔️ CHARACTER BUILDER ⚔️")
  print()
  name = input("Name your Legend:\n")
  type = input("Character Type (Human, Elf, Wizard, Orc):\n")
  print()
  print(name)
  print("HEALTH:", health())
  print("STRENGTH:", strength())
  print()
  print("May your name go down in Legend…")
  print()
  again = input("Again?:\n")
  if again=="No" or again=="no":
    break
  time.sleep(1)
  os.system("clear")
```

</details>
