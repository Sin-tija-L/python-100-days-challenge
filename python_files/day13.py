testName = input("What's the name of the test?")
maxScore = int(input("What's the maximum score?"))
myScore = float(input("What's your score?"))

myPercent = round((myScore / maxScore * 100), 2)

myGrade = ""

if myPercent >= 90:
    myGrade = "A+"
elif myPercent >= 80 and myPercent < 90:
    myGrade = "A"
elif myPercent >= 70 and myPercent < 80:
    myGrade = "B"
elif myPercent >= 60 and myPercent < 70:
    myGrade = "C"
elif myPercent >= 50 and myPercent < 60:
    myGrade = "D"
else:
    myGrade = "U"
    
print("For your test", testName, "you scored", myPercent, "% and got", myGrade, ".")