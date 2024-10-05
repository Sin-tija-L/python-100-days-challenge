# 👉 Day 31 Challenge

<a href="https://www.youtube.com/watch?v=rV6en_DUBZk" target="_blank">Dāvida video</a>


- Create a classic user interface using string manipulation.

- Create these two user interfaces (below) using everything you know about extensions to `print` statements and f-strings.

- The second one is a bit more tricky as it involves alignment.

- There are no input statements. This is all about using `print` and variables in interesting ways. However, you may want to create a subroutine to make the color changing easier (like you did on Day 29).

Interface 1:

<img id="image" src="assets/day31.png" alt="Replit Workspace Overview" width="960">


Interface 2:

<img id="image" src="assets/day31-01.png" alt="Replit Workspace Overview" width="960">


<details>
<summary>💡 Hint</summary>

- Create a subroutine to define your colors. It can be very similar to the subroutine you used on Day 29.
- Assign variables to the title, text, and words like "prev", "next", "username", etc. to make it easier to align the text.
- You will need f-strings anytime you include a variable and text alignment and a string together.

</details>

## Solution (No Peeking!)


<a href="https://www.youtube.com/watch?v=zKMPQLoh0zA" target="_blank">Solution video</a>

<details>
<summary>👀 Answer</summary>

```python
def colorChange(color):
  if color=="red":
    return ("\033[31m")
  elif color=="white":
    return ("\033[0m")
  elif color=="blue":
    return ("\033[34m")
  elif color=="yellow":
    return ("\033[33m")
  elif color == "green":
    return ("\033[32m")
  elif color == "purple":
    return ("\033[35m")

title = f"{colorChange('red')}={colorChange('white')}={colorChange('blue')}= {colorChange('yellow')}Music App {colorChange('blue')}={colorChange('white')}={colorChange('red')}="

print(f"        {title:^35}")
print(f"🔥▶️\t{colorChange('white')}Radio Gaga")
print(f"\t{colorChange('yellow')}Queen")

prev = "prev"
next = "next"
pause = "pause"

print(f"{colorChange('white')}{prev:<35}")
print(f"{colorChange('green')}{next:^35}")
print(f"{colorChange('purple')}{pause:>35}")


print()
print()
text = "WELCOME TO"
print(f"{colorChange('white')}{text:^35}")
text = "--  ARMBOOK  --"
print(f"{colorChange('blue')}{text:^35}")
text = "Definitely not a rip off"
print(f"{colorChange('yellow')}{text:>35}")
text = "a certain other social"
print(f"{colorChange('yellow')}{text:>35}")
text = "networking site"
print(f"{colorChange('yellow')}{text:>35}")
text = "Honest."
print(f"{colorChange('red')}{text:^35}")
text = "Username: "
username = input(f"{colorChange('white')}{text:^35}")
text = "Password: "
username = input(f"{colorChange('white')}{text:^35}")
```

</details>