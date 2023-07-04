fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
import re
inp = input('Write regular espression: ')
for line in fhand :
    line = line.rstrip()
    x = re.findall(inp, line)
    
    if len(x) > 0 :
        print(x)
    