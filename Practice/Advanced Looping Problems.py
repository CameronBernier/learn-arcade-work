# Problem 1
print("#1")
i = 1
while i <= 10:
    print("*", end=" ")
    i += 1

print()
print()

# Problem 2
print("#2")
for row in range(10):
    print("*", end=" ")
print()
for row in range(5):
    print("*", end=" ")
print()
for row in range(20):
    print("*", end=" ")
print()

print()

# Problem 3
print("#3")
for row in range(10):
    print()
    for column in range(10):
        print("*", end=" ")

print()
print()

# Problem 4
print("#4")

for row in range(10):
    print()
    for column in range(5):
        print("*", end=" ")

print()
print()

# Problem 5
print("#5")
o = 0
p = 0
while o < 5:
    print(' ')
    o += 1
    p = 0
    while p < 20:
        print(end=' *')
        p += 1
print()
print()

# Problem 6
print("#6")
q = 0
w = 0
while q < 10:
    print(' ')
    q += 1
    w = 0
    while w < 10:
        number = str(w)
        print(' ', end=number)
        w += 1

print()
print()

# Problem 7
print("#7")
row = -1
column = 0
while row < 9:
    print(' ')
    row += 1
    column = 0
    while column < 10:
        number1 = str(row)
        print(' ', end=number1)
        column += 1

print()
