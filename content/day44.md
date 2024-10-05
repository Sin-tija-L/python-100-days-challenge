# 👉 Day 43: 2D Dynamic Lists

<a href="https://youtu.be/483vwaq7qjo?si=9QknIGJMHprn03K6" target="_blank">📹 Dāvida video</a>

### ➡️ To learn this topic we suggest to run this code using terminal and run the file ⬅️


Dynamic lists are lists that we populate as we go, getting user input and adding it to the list as we go.

We're combining several techniques here. I've left detailed code comments to help. Remember, comments can be found with `# comment` in green inside the code.


## Loops, append() and break

Here's an example to get some simple user details(name, age, computer preference) and add it to a list as a full row. This list will keep taking input until the user answers 'y' to the 'exit?' question.

Once we collect the user's input in a row, we will append the entire row to the list. The columns are maintained and we are keeping the structure of 2D lists.

<img id="image" src="assets/day44_1.png" alt="Replit Workspace Overview" width="960">

👉 Let's try it:

```python
listOfShame = [] 
# Creates an empty list.

while True: 
  # Starts a never ending loop (until we end it)
  name = input("What is your name? ")
  age = input("What is your age? ")
  pref = input("What is your computer platform? ")
  # Get the user input.

  row = [name, age, pref] 
  # Assigns the 3 variables into a single row.

  listOfShame.append(row) 
  # Adds the contents of the row variable at the end of the list

  exit = input("Exit? y/n") 
  # Get user choice to quit, yes or no?

  if (exit.strip().lower()[0] == "y"): 
    # strip removes unwanted spaces from the input. lower()[0] makes sure the first character of the input is lower case so it can be compared to 'y'
    break # break ends a loop and jumps to the next line of code that is not part of the loop.
    
print(listOfShame) # Outputs the list. Note this is NOT part of the loop (not indented), it only runs once the loop ends.
```

### Pretty Printing

Man, that `print(listOfShame)` output sure is ug-leeee.

👉 In the code below, I've added a `prettyPrint` subroutine to beautify the output. Remember, we did this before on Day 34.

```python
def prettyPrint():
  print() 
  # Puts a blank row at the top
  for row in listOfShame: 
    #loops to the next row when the end of the current one is reached
     print(row) 
    # prints the new row
  print() 
  # prints a blank line between rows
    

listOfShame = [] 

while True: 
  name = input("What is your name? ")
  age = input("What is your age? ")
  pref = input("What is your computer platform? ")
  
  row = [name, age, pref] 

  listOfShame.append(row) 

  exit = input("Exit? y/n") 

  if (exit.strip().lower()[0] == "y"):
    break 

prettyPrint() 
# Call the prettyPrint subroutine instead of printing the list directly.
```

This code would produce an output like this

<img id="image" src="assets/day44_2.png" alt="Replit Workspace Overview" width="960">

There is a bit of weirdness. The rows are printing out, but they just look like a list with all those symbols. We need one loop to extract each row and one loop to extract each item from the columns.

### Prettier Printing?

👉 This version of `prettyPrint()` uses `fStrings` to further line up the tabs.

Note: this only shows the updated subroutine (not the entire code).

```python
def prettyPrint():
  print() 
  for row in listOfShame: 
    for item in row: 
      # item refers to each item in the column for that row
     print(f"{item:^10}", end=" | ") 
      # :^10 means 10 characters as the space with the data in the center. The end character has been changed to space vertical line space to make it look more like a table.
      
    print() 
    
  print()
```

This code would produce an output like this

<img id="image" src="assets/day44_3.png" alt="Replit Workspace Overview" width="960">

## Add or Remove?

We can add records, but let's expand to give the user the choice of whether to add OR remove. Do we want to remove the entire row or just one item?

We ask the user to choose between adding and removing. If they choose remove, we:
- ask for a name on the list (make sure it is spelled correctly)
- extract each row, one at a time, from the list
- check the row to see if it contains the name
- if the name is in the row, use the `.remove()` method to remove the whole row, not just the name.

👉 In the code below, I've only shown the loop that works with the list. I've left out the `prettyPrint` subroutine so we can focus on the changes. Again, check the comments for explanations.

```python

listOfShame = [] 

while True: 
  menu = input("Add or Remove?") # Gives the user a choice prompt and stores their input.

  if(menu.strip().lower()[0]=="a"): # Uses selection to run the 'add' code if user inputs 'a'. I've "sanitized" the input here too.
    
    name = input("What is your name? ")
    age = input("What is your age? ")
    pref = input("What is your computer platform? ")
    
    row = [name, age, pref] 
  
    listOfShame.append(row) 
    # All the 'add' code is now indented, so it's part of the 'add' branch and will only run if the user enters 'a'.

  else: # If the user doesn't choose 'a', run this new remove code instead.
    name = input("What is the name of the record to delete?") # Get the input of a name
    for row in listOfShame: # Use a loop to extract one row at a time
      
      if name in row: # Check if the name is in the extracted row.
        listOfShame.remove(row) # remove the whole row if name is in it

  prettyPrint()
```

## Fix My Code

👉 Try and fix this code which is full of errors.

First, delete any other code in your `day44.py` file. Copy each code snippet below into `day44.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

### My Remove Doesn't Work And There's No Error?

👉 Add a record to this code and then try to remove it. Why is the record still there?


```python

listOfShame = [] 

while True: 
  menu = input("Add or Remove?") 

  if(menu.strip().lower()[0]=="a"): 
    
    name = input("What is your name? ")
    age = input("What is your age? ")
    pref = input("What is your computer platform? ")
    
    row = [name, age, pref] 
  
    listOfShame.append(row) 
    

  else: 
    name = input("What is the name of the record to delete?") 
    
    if name in listOfShame: 
      listOfShame.remove(name) # remove the whole row if name is in it


  print(listOfShame)
```

<details>
<summary>👀 Answer</summary>

I did not use a loop to extract each row at a time and then check each item for a matching name. Therefore, the code never finds an exact match for 'name', and doesn't remove anything.

I only included the changes to make after the 'else' statement, not the entire code.

```python
    for row in listOfShame: # Use a loop to extract one row at a time
      
      if name in row: # Check if the name is in the extracted row.
        listOfShame.remove(row) # remove the whole row if name is in it

  print(listOfShame)
```

</details>

# 👉 Day 44 Challenge

It's time for more bingo! You can reuse your code from day 43, but this time add the following features:
1. Repeatedly ask the user what number comes up next.
2. Check the bingo card to see if the number picked matches one on the card.
3. If the bingo card is all 'X's, then the user has won.

Example:

<img id="image" src="assets/day44_4.png" alt="Replit Workspace Overview" width="960">

<details>
<summary>💡 Hints</summary>

- Create a subroutine called `createCard` to clean up some of the code from Day 43.
- Use a variable and loop to store how many x's there are on the card. Add one every time a number is replaced.
- Check the variable every time to see if it has reached the magic winning number.

</details>


## Solution (No Peeking!)

<a href="https://youtu.be/ee8SR2FKMR4?si=rpidRoiuEx-JYlSY" target="_blank">Solution video</a>

<details>
<summary>👀 Answer</summary>

```python
import random

bingo = []
exes = 0
print("\033[33mAlises Bingo Card Generator ⭐️")
print()

def generateNumber():
    return random.randint(1, 90)

def prettyPrint(userInput):
    print(" ┌───────────┬───────────┬───────────┐")
    for i, row in enumerate(bingo):
      is_last_row = i == len(bingo) - 1  
      print(" │", end=" ")
      for j, number in enumerate(row):
          if number == "⭐️BINGO⭐️":
              print(number.center(9), end=" │ ")
          elif userInput == number:
              row[j] = "X"
              print(str(row[j]).center(9), end=" │ ")
          else:
              print(str(number).center(9), end=" │ ")

      print("\n", end="")
      if not is_last_row:
          print(" ├───────────┼───────────┼───────────┤")
      else:
          print(" └───────────┴───────────┴───────────┘")

numbers = []
for i in range(8):
    numbers.append(generateNumber())

numbers.sort()
bingo =  [ [numbers[0], numbers[1], numbers[2]],
           [numbers[3], "⭐️BINGO⭐️", numbers[4]],
           [numbers[5], numbers[6], numbers[7]], ]

for row in bingo:
  for number in row:
    userInput = int(input("What is next number? "))
    prettyPrint(userInput)

exes = 0
for row in bingo:
  for item in row:
    if item=="X":
      exes+=1
      
if exes == 8:
  print("You have won")
else:
  print("Next time")
```

</details>