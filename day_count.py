fname = input('Write file name: ')
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()

count = 0
d = {}

for line in fhand:
    if not line.startswith('From'): continue

    words = line.rstrip()
    words = line.split()
    
                
    if len(words) > 2:
        day = words[2]
        
    d[day] = d.get(day, 0)+1
    print(d)
    
    
        
    
    