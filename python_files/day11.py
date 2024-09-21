sec_per_day = 60 * 60 * 24
long_month = 31 * sec_per_day
short_month = 30 * sec_per_day

year = int(input("Which year you want to count? "))

if year % 4 == 0 and year % 100 != 0:
    sec_total = 7 * long_month + 4 * short_month + 29 * sec_per_day
    print(year, "is a leap year, so there are", sec_total, "seconds in this year.")
elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    sec_total = 7 * long_month + 4 * short_month + 29 * sec_per_day
    print(year, "is a leap year, so there are", sec_total, "seconds in this year.")
else:
    sec_total = 7 * long_month + 4 * short_month + 28 * sec_per_day
    print(year, "is not a leap year, so there are", sec_total, "seconds in this year.")