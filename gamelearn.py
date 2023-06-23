import random

y = 0
x = 5
def fun(x):
    for i in range(1):
        x = random.randint(0,11)
        print(x)

        if x < y:
            print('x is less than y')
        elif x > y:
            print('x is greater than y')
        else:
            print('x and y are equal')
fun(x)

while y != x :
    y = y +1
    fun(x)
