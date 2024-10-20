# 👉 Day 65 Challenge! 🚀

<a href="https://youtu.be/edfFZoCDou0" target="_blank">📹 David video</a>


Today, you'll dive into **Object-Oriented Programming (OOP)** and apply your skills to create **characters** for my video game! 🚀

## Here's What You Need to Do:

1. **Create a character** 🧙‍♀️
   - Every character should have a **name**, **health**, and **magic points**.
   - These values should be set when the character is created (initialized).
   - Add a method to **output** this character's stats.

2. **Create a Player sub-class** 🎮
   - The **player** class should inherit from the character class and also have a number of **lives**.
   - Add an 'Am I Alive?' method to check if the player is still alive and return a **yes/no**.

3. **Create an Enemy sub-class** 😈
   - The **enemy** class should have additional attributes: **type** (what kind of enemy it is) and **strength**.
   - The enemy class should have two sub-classes:
     - **Orc** 🐗 with an added attribute: **speed**.
     - **Vampire** 🧛‍♂️ with a **day/night tracker**.

4. **Instantiate**:
   - Create one **player**, two **vampires**, and three **orcs** with unique names of your choice.
   - **Print out** all their values and attributes to see them in action! ⚔️

### Example:
- 🧙‍♀️ A player with 100 health, 50 magic points, 3 lives, and a check to see if they're alive.
- 🧛‍♂️ Vampires with their strength, type, and whether it's day or night.
- 🐗 Orcs with their speed and strength, ready for battle.

Now it's time to bring your characters to life in code! 💻

<img id="image" src="assets/day65_1.png" alt="day65 image" width="960">


<details>
<summary>💡 Hints</summary>

- You only need to inherit from the class directly above. So orc only needs to inherit from enemy, for example.

</details>


## Solution (No Peeking!)

<a href="https://youtu.be/VK6TDrVy6Fg" target="_blank">📹 David solution</a>

<details>
<summary>👀 Answer</summary>

```python
class Character:
  def __init__(self, name, health, magic_points):
      self.name = name
      self.health = health
      self.magic_points = magic_points

  def print_stats(self):
      print("Name:", self.name)
      print("Health:", self.health)
      print("Magic Points:", self.magic_points)


class Player(Character):
  def __init__(self, name, health, magic_points, lives):
      super().__init__(name, health, magic_points)
      self.lives = lives

  def is_player_alive(self):
      if self.lives > 0:
          print("Player is alive with", self.lives, "lives left.")
          return True
      else:
          print("Player is not alive.")
          return False


class Enemy(Character):
  def __init__(self, name, health, magic_points, type, strength):
      super().__init__(name, health, magic_points)
      self.type = type
      self.strength = strength


class Orc(Enemy):
  def __init__(self, name, health, magic_points, type, strength, speed):
      super().__init__(name, health, magic_points, type, strength)
      self.speed = speed


class Vampire(Enemy):
  def __init__(self, name, health, magic_points, type, strength, day_night_tracker):
      super().__init__(name, health, magic_points, type, strength)
      self.day_night_tracker = day_night_tracker


print("🌟Generic RPG🌟")
print()

# Instantiate characters
player = Player("Alise", 100, 50, 3)
vampire1 = Vampire("Vampire1Name", 80, 60, "Vampire", 30, "Night")
vampire2 = Vampire("Vampire2Name", 85, 55, "Vampire", 35, "Day")
orc1 = Orc("Orc1Name", 120, 40, "Orc", 45, 25)
orc2 = Orc("Orc2Name", 110, 45, "Orc", 40, 30)
orc3 = Orc("Orc3Name", 115, 42, "Orc", 42, 28)

# Print stats for each character
player.print_stats()
player.is_player_alive()
print()
vampire1.print_stats()
print()
vampire2.print_stats()
print()
orc1.print_stats()
print()
orc2.print_stats()
print()
orc3.print_stats()
```

</details>