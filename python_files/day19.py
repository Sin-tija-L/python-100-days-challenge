loan = 1000
for i in range(10):
  loan += loan * 0.05
  print("Year", i+1, ":", round(loan, 2))