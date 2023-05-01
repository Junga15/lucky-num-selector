
import random

result = random.sample(range(1,45+1), k=6)
print(result)

print("===================================")

def get_lucky_nums():
    return random.sample(range(1,45+1), k=6)

if __name__ == '__main__':
    times = int(input('Enter nums(1-100): '))
    for _ in range(times):
        print(get_lucky_nums())

print("===================================")

list = []
ran_num = random.randint(0,9)

for i in range(6):
    while ran_num in list:
        ran_num = random.randint(0,46)
    list.append(ran_num)

print(list)
