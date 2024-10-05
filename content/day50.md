# 👉 Day 50 Challenge: Idea Maker...

<a href="https://youtu.be/nEoQq-FTMtA?si=dxDGslY8zGnWW2nv" target="_blank">📹 Dāvida video</a>

Do you have brilliant ideas at inconvenient times? Do you need a handy way of storing those ideas? Have you never heard of smartphone voice note apps? Or pens and paper? Then, today's project is for you!

Head on over to the challenge page for all the amazing details.

**To run this code use terminal and run the file 😎**


Day 50! Girl, you are smashing this 100 days! 🎉 To celebrate, here's a project for you.

Your idea storage system should:
1. Prompt the user to add an idea, or load a random one.
2. Choosing 'Add an idea' results in:
   - A prompt for the user to input their idea.
   -  Add the idea to a text file called 'my.ideas'.
   - Add the idea in append mode, with every new idea on a brand new line.
3. Choosing 'Load random' results in:
   - Load the list of ideas.
   - Choose one at random.
   - Display it on screen for a few seconds.
   - Return to the menu.

**Example:**

<img id="image" src="assets/day50_1.png" alt="Replit Workspace Overview" width="960">

<details>
<summary>💡 Hints</summary>

- To pick an idea at random, you could use `split()` to get an array of values. Or you could use `random.choice` to generate a random number and keep loading lines until you get to the random number line.
- Try implementing your menu as a subroutine, so you can call it whenever you need to return to it.

</details>

## Solution (No Peeking!)

<a href="https://youtu.be/ICF8b1aL5lM?si=iCGNLx3gObMHj5sD" target="_blank">Solution video</a>

<details>
<summary>👀 Answer</summary>

```python
import random, time, os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the 'files/my.ideas' file
file_path = os.path.join(script_dir, "files/my.ideas")

def add_idea(idea):
    # Ensure the 'files' directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    f = open(file_path, 'a')
    f.write(idea + '\n')
    print("Nice! Your idea has been stored.")

def load_random_idea():
    # Check if the file exists before trying to open it
    if not os.path.exists(file_path):
        print("No ideas found. Add some ideas first.")
        return

    f = open(file_path, 'r')
    ideas = f.readlines()
    if not ideas:
        print("No ideas found. Add some ideas first.")
        return

    random_idea = random.choice(ideas).strip()
    print(f"\nRandom Idea: {random_idea}")
    time.sleep(3)  # Display the idea for a few seconds

def main():
    while True:
        print("\n🌟 Idea Storage 🌟")
        choice = input("Add an idea or see a random idea? (a/r): ").lower().strip()

        if choice == 'a':
            user_idea = input("Input your idea: ").strip()
            if user_idea:
                add_idea(user_idea)
            else:
                print("No idea entered. Please try again.")
        elif choice == 'r':
            load_random_idea()
        else:
            print("Invalid choice. Please choose 'a' to add an idea or 'r' to see a random idea.")


main()
```

</details>