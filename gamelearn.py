import random

y = 0
for i in range(10):
    x = random.random()

if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')
