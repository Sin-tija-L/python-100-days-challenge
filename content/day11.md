# 👉 Day 11 Challenge


<a href="https://www.youtube.com/watch?v=pKRE-W9HGNs" target="_blank">Dāvida video</a>

## How many seconds are in a year?

Use the power of breaking a program down into its parts. We could Google this, but why not make a program for this instead.

<details>
<summary>Conversions</summary>
60 seconds = 1 minute

60 minutes = 1 hour

24 hours = 1 day

31 days = 1 month

12 months = 1 year

365 days = 1 year

366 day = 1 leap year (this is every four years)

Learn more about leap years <a href="https://spaceplace.nasa.gov/leap-year/en/" target="_blank">here.</a>

</details>

1. You can multiply a bunch of numbers to figure out how many seconds are in a year.

<details>
<summary>💡 Hint</summary>
Think about how the math would be different for a leap year.

</details>

2. Use input and if statements to add the extra day for leap year.


<details>
<summary>💡 Hint</summary>

Think about if you need `int` or `float` for your `input`.

</details>

 3. Make the computer do all the hard work and math for you. You do the thinking beforehand.

## Solution (No Peeking!)

<details>
<summary>👀 Answer</summary>

```python 
days_this_year = int(input("How many days are in this year?"))

days_in_year = 365
days_in_leapyear = 366
hours_in_day = 24
minutes_in_hour = 60
seconds_in_minute = 60


result = days_in_year * hours_in_day * minutes_in_hour * seconds_in_minute

leapyear_result = days_in_leapyear * hours_in_day * minutes_in_hour * seconds_in_minute


if days_this_year == 366:
  print("Number of seconds in a leap year are", leapyear_result)
else:
  print("Number of seconds in a year are", result)
```

</details>