import random

negativeTemp = 0
for i in range(7):
    temp = random.randint(-10, 10) # [-10;10]
    if temp < 0:
        negativeTemp += 1

print(negativeTemp)