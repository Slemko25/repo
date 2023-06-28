fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

text = dict()

for word in fhand :
    word = word.rstrip()
    word = word.lower()
    word = word.split()

    for c in word :
        text[c] = text.get(c, 0) + 1
print(text)

bigcount = None
bigword = None
for c, text in text.items():
    if bigcount is None or text > bigcount :
        bigword = c
        bigcount = text
print(bigword,':', bigcount)        


