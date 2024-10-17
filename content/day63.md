# 👉 Day 61: Multiple Files


<a href="https://www.youtube.com/watch?v=girsuXz0yA8" target="_blank">📹 Dāvida video</a>


By now, you have written some pretty big programs with lots of lines of code.

This can get pretty cumbersome to deal with. Lots of scrolling to find the right bit...

One of the ways to overcome this is to split the code into multiple files.

That's right. Your programs can consist of more than one python file. The main file will always run first, but you can put parts of your code into other files and bring them in to main.py by importing.

In fact, you've already done this whenever you've used `import random`, `import time`, `import os` and so on. It's just that on those occasions, you were importing code written by someone else.

Today, you'll create your own code file and import it into your main program.

👉 Let's start with a basic 'count to 10' program in the `day63.py` file.

```python
for i in range(10):
  print(i+1)
```

👉 Now let's move it to a new file.

In the files menu click on `python_files`, find the 'New File' and select it.

<img id="image" src="assets/day63_1.png" alt="day63 image" width="960">

Name the file `test63.py` - you **MUST** include the .py to specify that it's a python file.

<img id="image" src="assets/day63_2.png" alt="day63 image" width="960">

Cut and paste the code from `day63.py` to `test63.py`.

<img id="image" src="assets/day63_3.png" alt="day63 image" width="960">


By now, your `day63.py` file should have nothing in it.


👉 To run this code use terminal and run the file. Watch in amazement as nothing happens!

To run this code open new Terminal and type python `python_files/day63.py` or `python3 python_files/day63.py` and see the result! 🚀


Remember, Python runs the code in the `day63.py` file, which at the moment is empty. So we need to import the code.

👉 Go to your `day63.py` file and add this code.

```python
import test63 # No need for the .py
```

👉 Now run the code and watch the 'count to 10' program execute.


## It Can't Be That Easy? Can It?

Well....... no. Because we can't control **when** the 'count to 10' program runs. It just runs on import. In this example, it would run *before* the `print("Countdown")` code. Not ideal.

```python
import test63

print("Countdown")
```

### Try to insert more then one key and value

Column names and values both: In this method we will specify both the columns which we want to fill and their corresponding values as shown below:

<img id="image" src="assets/day61_1.png" alt="day61 image" width="960">


## Accessing Data

`!NB` Remove the `INSERT INTO myTable` statement from your `day61.py` file. If left together with the `SELECT` statement, it will add a new value to the table each time you run the script.

## Viewing All keys

You can retrieve and display all keys from table

```python
cursor.execute("SELECT key FROM myTable")
keys = cursor.fetchall()
    
if not keys:
    print("The table is empty.")
else:
    print("Keys in the table:")
    for key in keys:
        print(key[0])
```

This statement is used to retrieve data from an SQLite table and this returns the data contained in the table.

In SQLite the syntax of Select Statement is:

<img id="image" src="assets/day61_3.png" alt="day61 image" width="760">


## Viewing All values

You an retrieve and display all values from table

```python
cursor.execute("SELECT value FROM myTable")
values = cursor.fetchall()
    
if not values:
    print("The table is empty.")
else:
    print("Values in the table:")
    for value in values:
        print(value[0])
```


## Viewing All data

You can retrieve and display all data from the database:

```python
cursor.execute("SELECT * FROM myTable")
rows = cursor.fetchall()
for row in rows:
    print(f"{row[0]}\t{row[1]}\t{row[2]}")
```

This function fetches all data from the table and displays them.

## Viewing All ordered by 

The `ORDER BY` statement is a SQL statement that is used to sort the data in either ascending or descending according to one or more columns. By default, `ORDER BY` sorts the data in ascending order.

  - `DESC` is used to sort the data in descending order.
  - `ASC` to sort in ascending order.

<img id="image" src="assets/day61_4.png" alt="day61 image" width="760">


```python
cursor.execute("SELECT * FROM myTable ORDER BY key")
rows = cursor.fetchall()
for row in rows:
            print(f"{row[0]}\t{row[1]}\t{row[2]}")
```


### Please try to add DESC in query! 

<details>
<summary>👀 Answer</summary>

```python
cursor.execute("SELECT * FROM myTable ORDER BY key DESC")
rows = cursor.fetchall()
for row in rows:
            print(f"{row[0]}\t{row[1]}\t{row[2]}")
```

</details>


## Removing Data

To delete a specific row from table by its `key`, use the following function:

<img id="image" src="assets/day61_2.png" alt="day61 image" width="760">

```python
key = "test"
cursor.execute("DELETE FROM myTable WHERE key = ?", (key,))
conn.commit()
```


## Please note 
We can put the functions we looked at before inside other functions:

```python
def insert_data(key, value):
    cursor.execute("INSERT INTO myTable (key, value) VALUES (?, ?)", (key, value))
    conn.commit()

insert_data("test", "Hello World")
```
This revised version maintains the key points while improving clarity and readability. 


## Fix My Code

👉 Try and fix this code which is full of errors.

First, delete any other code in your `day61.py` file. Copy each code snippet below into `day61.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

```python
conn = sqlite3.connect('day61.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS myTable (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    key TEXT,
    value TEXT
)
''')
conn.commit()

def insert_data(key, value):
    cursor.execute("INSERT INTO myTable (key, value) VALUES (?, ?)", (key, value))
    conn.commit()

def print_keys():
    cursor.execute("SELECT key FROM myTable")
    key = cursor.fetchall()
    
    if not key
        print("The table is empty.")
    else:
        print("Keys in the table:")
        for key in key
            print(key)

insert_data("test3", "Hello World")
insert_data("test4", "Hello There")
print_keys()
```


<details>
<summary>👀 Answer</summary>

```python
import sqlite3 # no import

conn = sqlite3.connect('day61.db')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS myTable (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    key TEXT,
    value TEXT
)
''')
conn.commit()

def insert_data(key, value):
    cursor.execute("INSERT INTO myTable (key, value) VALUES (?, ?)", (key, value))
    conn.commit()

def print_keys():
    cursor.execute("SELECT key FROM myTable")
    keys = cursor.fetchall() # missing 's' from 'key'
    
    if not keys:  #missing colon
        print("The table is empty.")
    else:
        print("Keys in the table:")
        for key in keys:  #missing colon
            print(key[0]) # Only key column data, but we need a value

insert_data("test3", "Hello World")
insert_data("test4", "Hello There")
print_keys()
```

</details>

## 👉 Day 61 Challenge

###  Someone is wrong on the Internet!
Today, we're going to fix the major malfunction with social media - other people and their stupid opinions- and create a Twitter for one!

I know you like to hear the sound of your own voice!

Your program should:
1. Display a menu - `Add` or `View` tweets.
2. `'Add'` should:
  - Get the tweet input.
  - Store it to the database with the current timestamp as the key value.
3. `'View'` should:
  - Show the tweets in reverse chronological order.
  - Show 10 tweets at a time.
  - Prompt the user to show another 10 tweets (yes or no).
  - A 'no' choice goes back to the menu.
4. `'Exit'` should:
  - close menu.
  
Timestamp Code:

```python
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
```

<details>
<summary>💡 Hint</summary>

- Use the `datetime` library to get the current timestamp.
- Use the `conn.close()` to close menu
- Use the `os` library to clear the console between each 10 tweets shown.


</details>

## Solution (No Peeking!)

<details>
<summary>👀 Answer</summary>

```python
import sqlite3
import datetime, os, time

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('day61.db')
cursor = conn.cursor()

# Create a table to store tweets if it doesn't already exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS tweets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    tweet TEXT
)
''')
conn.commit()

def addTweet():
    tweet = input("🐥 > ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    cursor.execute('''
    INSERT INTO tweets (timestamp, tweet)
    VALUES (?, ?)
    ''', (timestamp, tweet))
    
    conn.commit()
    time.sleep(1)
    os.system("clear")

def viewTweet():
    cursor.execute('SELECT * FROM tweets ORDER BY id DESC')
    tweets = cursor.fetchall()

    counter = 0
    for tweet in tweets:
        print(f"{tweet[1]}: {tweet[2]}")
        counter += 1
        if counter % 10 == 0:
            carryOn = input("Next 10?: ")
            if carryOn.lower() == "no":
                break
    time.sleep(1)
    os.system("clear")

def deleteTweet():
    tweet_id = input("Enter the ID of the tweet to delete: ")
    cursor.execute('DELETE FROM tweets WHERE id = ?', (tweet_id,))
    conn.commit()
    print(f"Tweet with ID {tweet_id} deleted.")
    time.sleep(1)
    os.system("clear")

while True:
    print("❌ Tweeter ❌ ")
    menu = input("1: Add Tweet\n2: View Tweets\n3: Delete Tweet\n4: Exit\n> ")
    
    if menu == "1":
        addTweet()
    elif menu == "2":
        viewTweet()
    elif menu == "3":
        deleteTweet()
    elif menu == "4":
        print("Exiting the program...")
        conn.close()
        break
    else:
        print("Invalid option, please choose 1, 2, 3, or 4.")
```

</details>

Šajā uzdevumā run pogu neizmantojam. 