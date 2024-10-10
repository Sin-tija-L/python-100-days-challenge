# 👉 Day 54: Comma-Separated Values

<a href="https://youtu.be/FhThwQ0BCfY" target="_blank">📹 Dāvida video</a>

**To run this day's code use terminal and run the file 😎**

CSV files are a way of storing a spreadsheet as a text file. Every value in the file is separated by a comma.

Hence the name...

Look, it's basically a spreadsheet.

### Opening A CSV File

Fortunately, CSV files are so common that Python already has built-in libraries for working with them.

👉 The csv file 'January.csv' has been added for you. Let's see what happens:

```python
import os
import csv  # Imports the csv library

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the 'files/January.csv' file
file_path = os.path.join(script_dir, "files", "January.csv")

# Open and read the CSV file from the 'files' directory
with open(file_path, "r") as file:  # Opens the csv file
    reader = csv.reader(file)  # Reads the contents of the csv file into the 'reader' variable

    for row in reader:  # Loop to output each row in the 'reader' variable one at a time
        print(row)
```

This works, but the output isn't very pretty. And we like pretty.

<img id="image" src="assets/day54_1.png" alt="Replit Workspace Overview" width="960">


### Make it Beautiful!

👉 Let's use `join`. It allows us combine lists in a more interesting way.

```python
import os
import csv  # Imports the csv library

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the 'files/January.csv' file
file_path = os.path.join(script_dir, "files", "January.csv")

# Open and read the CSV file from the 'files' directory
with open(file_path, "r") as file:  # Opens the csv file
    reader = csv.reader(file)  # Reads the contents of the csv file into the 'reader' variable

    for row in reader:  # Loop to output each row in the 'reader' variable one at a time
        print (", ".join(row)) # adds a comma and space and then joins data, you could try joining with tabs too with `\t`
```


### Filter the Output

👉 The trick is to treat the CSV like a dictionary, using the `csv.DictReader()` function. In the code below, I've filtered it so that it only shows the net total from each day.

```python
import os
import csv  # Imports the csv library

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the 'files/January.csv' file
file_path = os.path.join(script_dir, "files", "January.csv")

# Open and read the CSV file from the 'files' directory
with open(file_path, "r") as file:  # Opens the csv file
    reader = csv.DictReader(file) # Treats the file as a dictionary 

    for row in reader:  # Loop to output each row in the 'reader' variable one at a time
        print (row["Net Total"])
```
<img id="image" src="assets/day54_2.png" alt="Replit Workspace Overview" width="960">


👉 Now let's see if we can add the net totals from each day to create a total. Note that I've cast the data as a float because our library will treat it as text.

```python
import os
import csv  # Imports the csv library

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the 'files/January.csv' file
file_path = os.path.join(script_dir, "files", "January.csv")

# Open and read the CSV file from the 'files' directory
with open(file_path, "r") as file:  # Opens the csv file
    reader = csv.DictReader(file) # Treats the file as a dictionary 

    total = 0
    for row in reader:  # Loop to output each row in the 'reader' variable one at a time
        print (row["Net Total"])
        total += float(row["Net Total"]) # Keeps a running total

print(f"Total: {total}") #Outputs
```

**Try it out!**


## Common Errors

First, delete any other code in your `day54.py` file. Copy each code snippet below into `day54.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

👉 What's the problem here?

```python
import os
import csv

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "files", "January.csv")

with open(file_path, "r") as file:
    reader = csv.DictReader(file) 
  
    total = 0
    for row in reader: 
      print (row["Net Total"])
      total += row["Net Total"] 

print(f"Total: {total}")
```

<details>
<summary>👀 Answer</summary>

- Data read is treated as text. To perform calculations, we need to cast it. In this case, as a float.

```python
import os
import csv

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "files", "January.csv")

with open(file_path, "r") as file:
    reader = csv.DictReader(file) 
  
    total = 0
    for row in reader: 
      print (row["Net Total"])
      total += float(row["Net Total"])

print(f"Total: {total}")
```

</details>

---

👉 What's the problem here?

```python
import os
import csv

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "files", "January.csv")

with open(file_path, "r") as file:
    reader = csv.DictReader(file) 
  
    total = 0
    for row in reader: 
      print (", ".join(row["Net Total"]))
      total += float(row["Net Total"])

print(f"Total: {total}")
```

Did you get this output?

<img id="image" src="assets/day54_3.png" alt="Replit Workspace Overview" width="960">

<details>
<summary>👀 Answer</summary>

The join command has been applied to a string. It's joining those individual characters with a comma between each one.

This won't break your code, just make the output look a bit weird. Removing the `join()` command fixes this.

```python
import os
import csv

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "files", "January.csv")

with open(file_path, "r") as file:
    reader = csv.DictReader(file) 
  
    total = 0
    for row in reader: 
      print(row["Net Total"])
      total += float(row["Net Total"]) 

print(f"Total: {total}")
```

</details>


## Fix My Code

👉 Try and fix this code which is full of errors.

First, delete any other code in your `day54.py` file. Copy each code snippet below into `day54.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

```python
import os
import csv

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "files", "January.csv")

with open(file_path, "r") as file:
    reader = csv.DictReader(file) 
  
    total = 0
    for row in reader: 
      print(", ".join(row["Net Total"]))
      total += row["Net Total"]

print(f"Total: {total}")
```

<details>
<summary>👀 Answer</summary>

```python
import os
import csv

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "files", "January.csv")

with open(file_path, "r") as file:
    reader = csv.DictReader(file) 
  
    total = 0
    for row in reader: 
      print(row["Net Total"])
      total += float(row["Net Total"]) 

print(f"Total: {total}")
```

</details>


## 👉 Day 54 Challenge

I've given you a CSV file called 'Day54Totals.csv' (look at your file tree) that contains multiple pieces of data in the fields 'cost' and 'quantity' of items sold. How much money did this shop earn in a day?

Your program should:
1. Read the CSV file in.
2. Multiply the cost by the quantity.
3. Add it all together to calculate how much money the shop made in a day.

**Example:**

<img id="image" src="assets/day54_4.png" alt="Replit Workspace Overview" width="960">

<details>
<summary>💡 Hints</summary>

- Use the dictionary approach to loading your file.
- Take in 2 different values.
- Cast them in 2 different ways.

</details>


## Solution (No Peeking!)

<a href="https://youtu.be/FhThwQ0BCfY" target="_blank">Solution video</a>

<details>
<summary>👀 Answer</summary>

```python
import os
import csv

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "files", "Day54Totals.csv")

with open(file_path, "r") as file:
    reader = csv.DictReader(file) 
    total = 0

    print("🌟Shop $$ Tracker🌟\n")
    for row in reader: 
      total += float(float(row["Cost"]) * float(row["Quantity"]))
  
print(f"Your shop took £{total:.2f} pounds today.")
```

</details>