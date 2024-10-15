# 👉 Day 60: The Magic of Time....

<a href="https://youtu.be/c6EmFRVulOY" target="_blank">📹 Dāvida video</a>


On day 60, we're going to learn about time (not time travel). Sorry to disappoint.

This can be quite a complicated thing, because we humans don't have nice standardized time. Instead we have:
- 24 hour clocks
- AM and PM
- Months of differing lengths
- Leap years
- Leap seconds

And all sorts of oddities in our temporal framework.


### Unix Epoch

👉 Your computer (and all of the other ones) uses something called the **Unix epoch** to measure time.

It counts the amount of seconds elapsed since Jan 1st, 1970 (even when the power's off - there's a small battery on your motherboard that keeps this function running).

Then, it turns this into a meaningful format for you, you illogical human.


### datetime

To use the Unix epoch, we first need to import the **datetime** library

```python
import datetime
```

👉 Now I'm going to insert the date and assign it to a variable.

```python
import datetime

myDate = datetime.date(year=2022, month=12, day= 7)

print(myDate)

# This code outputs '2022-12-07'
```

<img id="image" src="assets/day60_1.png" alt="Replit Workspace Overview" width="960">


You **HAVE** to use the year -> month -> day format for your arguments. So Brits & Americans, put down your calendars and go find something else to argue about...

The reason for this format is that the elements get smaller (and less important) sequentially from left to right. This makes sorting much easier.


### Asking For A Date

👉 Let's use `datetime` to automatically get today's date.

```python
import datetime

today = datetime.date.today()

print(today)

# This code outputs the current date from your computer's clock.
```

Hmmm, remember when we were creating to-do lists and we had to manually input the date......


### Getting Date Input

👉 The easiest way to do this is to ask the user for day, month, and year in separate values.

```python
import datetime

day = int(input("Day: ")) # Get all input as numbers. We're not at text input for months yet.
month = int(input("Month: "))
year = int(input("Year: "))

date = datetime.date(year, month, day)

print(date)
        print (row["Net Total"])
```

**Try it out!**


### Delta Force

A common task in programs is to work out the difference between two dates, for example to calculate someone's age.

To do this, we use a time delta.

Delta is a computer science term that means the difference between two things.

A time delta is a difference in time. The time delta between when you were born and now is increasing all the time as you age.

👉 Here's some code that calculates a time delta between today and two weeks today to see what the date will be in two weeks.

```python
import datetime

today = datetime.date.today() # Today's date

difference = datetime.timedelta(days=14) # The difference I want

newDate = today + difference # Add today to the delta difference to see the date in 14 days time.

print(newDate)
```

<img id="image" src="assets/day60_2.png" alt="Replit Workspace Overview" width="960">


### If Statements With Dates

Provided you've formatted the date correctly, you can use the `>`, `==` and `<` comparison operators just like you can with integers.

👉 I can use this to tell me if I should be on vacation or not!

```python
import datetime

today = datetime.date.today() # Today's date

holiday = datetime.date(year = 2022, month = 10, day = 30) # The date of my holiday

if holiday > today: # If my holiday is in the future
  print("Coming soon")
elif holiday < today: #If my holiday date has passed
  print("Hope you enjoyed it")
else: # If my holiday date is today
  print("HOLIDAY TIME!")
```

**Try it out!**


## Common Errors

First, delete any other code in your `day60.py` file. Copy each code snippet below into `day60.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

👉 What's the problem here?

```python
import datetime

today = datetime.today()

print(today)
```

<details>
<summary>👀 Answer</summary>

Missed the `date` function from the second line.

```python
import datetime

today = datetime.date.today()

print(today)
```

</details>

---

👉 What's the problem here?

```python
import datetime

today = datetime.date(day = 1, year = 2023)

print(today)
```

<details>
<summary>👀 Answer</summary>

Missed the month.

```python
import datetime

today = datetime.date(day = 1, month = 10, year = 2023)

print(today)
```

</details>


## Fix My Code

👉 Try and fix this code which is full of errors.

First, delete any other code in your `day60.py` file. Copy each code snippet below into `day60.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.

```python
import datetime

today = datetime.today() 

holiday = datetime.date(year = 2022, day = 20) 

if holiday < today: 
  print("Coming soon")
elif holiday > today: 
  print("Hope you enjoyed it")
else:
  print("HOLIDAY TIME!")
```

<details>
<summary>👀 Answer</summary>

```python
import datetime

today = datetime.date.today() # Missed the .date 

holiday = datetime.date(year = 2022, month = 10, day = 20) # Missed the month

if holiday > today: # Logic error, checked if the holiday had passed
  print("Coming soon")
elif holiday < today:  # Logic error, checked if the holiday was in the future
  print("Hope you enjoyed it")
else:
  print("HOLIDAY TIME!")
```

</details>


## 👉 Day 60 Challenge

Today's challenge is an events countdown timer.

Your program should:
1. Automatically work out today's date.
2. Prompt the user to input the name and date of their event (year, month and day).
3. Work out the number of days until the event and output it.
4. If the event is happening today, insert some party emojis.
5. If the event was in the past, sad face emojis and tell the user how many days ago it was.

**Example:**

<img id="image" src="assets/day60_3.png" alt="Replit Workspace Overview" width="960">

<details>
<summary>💡 Hints</summary>

- Subtract today's date from the delta.
- What type of number will you get if the date has passed?

</details>


## Solution (No Peeking!)

<a href="https://youtu.be/KgIOfbC3Cvk" target="_blank">Solution video</a>

<details>
<summary>👀 Answer</summary>

```python
import datetime

print("🌟Event Countdown Timer🌟")
print()

event = input("What is the event you are looking forward to? ")

while True:
    try:
        year = int(input("What year is it? "))
        month = int(input("What month is it? "))
        day = int(input("What day is it? "))
        eventDay = datetime.date(year, month, day)
        break
    except ValueError:
        print("Please enter a valid date. Ensure the day, month, and year are numbers and the date exists.")

today = datetime.date.today()

if eventDay > today:
    days_left = (eventDay - today).days
    print(f"{days_left} days until {event}!")
elif eventDay < today:
    days_passed = (today - eventDay).days
    print(f"{days_passed} days since {event}.")
else:
    print(f"🎉🎉 {event} is today! 🎉🎉")
```

</details>