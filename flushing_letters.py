import time

for b in 'Write name of the file: ':
    print(b,end='', flush=True)
    time.sleep(0.05)
    
op = input()
with open(op, 'r+') as o:


    for i in o:
        s= i.rstrip()
        print('')
        for l in s:
            for a in l:
                
                print(a, end='', flush=True)
            
                time.sleep(0.05)

