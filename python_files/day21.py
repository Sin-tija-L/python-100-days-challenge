## Multiplication game

num = int(input("Enter a number: "))
score = 0

for i in range(1, 11):
    print(num, "x", i, "= ")
    result = int(input())
    if result == i * num:
        print("Correct!")
        score += 1
    else:
        print("Sorry, you're wrong. The answwer is ", i*num)
        
print("You scored", score, "out of 10.")