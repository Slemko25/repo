fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
word = str(input('Wright a word you serching for: '))

count = 0

for line in fhand :
    line = line.rstrip()
    if line.find(word) == -1 : continue
    
    if not line.startswith('Received'): continue
    count = count + 1
    print (line)
    
    
print('Income messeges from', word, 'is', count)