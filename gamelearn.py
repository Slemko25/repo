import random
x = None
y = None

while x == y :

    x = random.randint(0,2)
    print(x)
    y = random.randint(0,2)
    print(y)
              
    
    if x < y:
        print('x is less than y')
    elif x > y:
        print('x is greater than y')
    else:
        print('x and y are equal')
            
        
