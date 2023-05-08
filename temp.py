def signature(w):
    w1=list(w)
    w1.sort()
    w1=''.join(w1)
    return w1
#create or load?
mode=input("Create or Load C or L: ")
print()
if mode.upper()=='C':
# create a "Scrabble Dictionary"
    d={}
    print('Creating dictionary ... please wait.')
    f = open("C:/Users/Owner/OneDrive/Desktop/Python Code/Advanced-Python-Programming/text file/wordlist.txt",'r')
    print()
    sl = f.read()
    143
    z=sl.split(' ')
    print()
    for w in z:
        sig=signature(w)
        if sig not in d:
            d[sig]=[]
            d[sig].append(w)
        else:
            d[sig].append(w)
    f.close()
else:
    print('Unpickling dictionary ... please wait.')
    f=open('slwords','rb')
    d=pickle.load(f) # this “unpickles”
word=input("Please enter word: ")
print()
while word!='done':
    if len(word)!=6:
        print("word not 6 chars")
    else:
        word=word.upper()
        word=signature(word)
    if word in d:
        print(d[word])
    else:
        print(word,' not found.')
    word=input("Please enter word: ")
    print()
f=open('slwords','wb')
print('Pickling ... please wait.')
pickle.dump(d,f) # this pickles
f.close()
