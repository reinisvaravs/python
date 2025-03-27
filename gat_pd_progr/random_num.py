import random

x = random.randint(3, 9)      # 6 (int: a-b) 
x = random.random()           # 0.679 (0-1)
x = random.uniform(1.5, 1.8)  # 1.74 (float: a-b)
x = round(random.uniform(1.5, 1.8), 1)  # 1.6 rounds to 1 dec points


