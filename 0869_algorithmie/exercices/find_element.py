import random

def find(needle:int, stack:list):
    return stack.__contains__(needle)

stack = []
NEEDLE = 42

for i in range(random.randrange(1, 1000)):
    stack.append(random.randint(0, 10000))

print(find(NEEDLE, stack))