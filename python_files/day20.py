## List generator

start = int(input("Where to start: "))
end = int(input("Where to end: "))
incr = int(input("Step: "))

for i in range(start, end, incr):
    print(i)