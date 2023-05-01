
import random

list = []
ran_num = random.randint(0,9)

for i in range(6):
    while ran_num in list:
        ran_num = random.randint(0,9)
    list.append(ran_num)

print(list)
