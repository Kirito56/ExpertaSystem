import random

def auth(i):
    for j in range(i):
        print(f'{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}')

auth(6)