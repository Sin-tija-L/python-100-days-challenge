# 👉 Day 42: Gotta Catch 'Em All....

<a href="https://www.youtube.com/watch?v=sizWhMe5Tog" target="_blank">Dāvida video</a>


### And Put Them In A Dictionary
This challenge is all about using dictionaries to create a game about small creatures that you have captured, enslaved, and forced to fight for your amusement. You monster.

This game works in a completely non-copyright and totally lawyer friendly way. Pika-who? I have absolutely no idea what you mean..... officer.

### Go to the challenge page for details.

## 👉 Day 42 Challenge

"Some trainers have no fear. To them, this is just one more challenge".

1. Create a dictionary to store the details of your, ahem, MokéBeast.
2. Ask the user to input the following details: name, type (earth, fire, air, water or spirit), special move, starting HP and starting MP. For now we're just taking in one set of values for one beast.
3. Output the beast's details.
4. Check the beast's type and change the color of the text accordingly. Fire is red, water is blue, air is white. You decide on the others.

🥳 Extra points for getting all the inputs with just one `input` command and the `split` function.

👉 IMPORTANT INFO - keep a note of where this Repl is, you'll need it in a couple of lessons' time.

```python
Example:

👾 MokéBeast - The Non-Copyright Generic Beast Battle Game 👾

Input your beast's name > Brian

Input your beast's type > Earth

Input your beast's special move > Flying bellyflop

Input your beast's staring HP > 50

Input your beast's staring MP > 20

# This text outputs in green
Your beast is called Brian. It is an earth beast with a special move of Flying bellyflop
```

### ➡️ To run this code use terminal and run the file ⬅️

<details>
<summary>💡 Hint</summary>

- Start with your dictionary.
- You will need a `for` loop.
- Change the font color for the beast's type by using `if` statements.
- Change font color using `print("\033[XXm", end="")` - replace the XX with a <a href="https://ozzmaker.com/add-colour-to-text-in-python/" target="_blank">color code</a>.

</details>


## Solution (No Peeking!)

<a href="https://www.youtube.com/watch?v=f6az2mDeRYk" target="_blank">Solution video</a>

<details>
<summary>👀 Answer</summary>

```python
mokedex = {"Beast Name": None, "Type": None, "Special Move": None, "HP": None, "MP": None}

print("MokéBeast")
print()

for name, value in mokedex.items():
  mokedex[name] = input(f"{name}:\t").strip().title()

if mokedex["Type"]=="Earth":
  print("\033[32m", end="")
elif mokedex["Type"]=="Air":
  print("\033[37m", end="")
elif mokedex["Type"]=="Fire":
  print("\033[31m", end="")
elif mokedex["Type"]=="Water":
  print("\033[34m", end="")
else:
  print("\033[33m", end="")

for name, value in mokedex.items():
  print(f"{name:<15}: {value}")
```

</details>

Šajā uzdevumā run pogu neizmantojam. 
