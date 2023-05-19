#For example, here’s how you could count the total number of shares for each stock name in earlier data:

portfolio = [
 ('ACME', 50, 92.34),
 ('IBM', 75, 102.25),
 ('PHP', 40, 74.50),
 ('IBM', 50, 124.75)
]
total_shares = { s[0]: 0 for s in portfolio } # dictionary comprehension
for name, shares, _ in portfolio:
 total_shares[name] += shares
 print(total_shares[name])
# total_shares = {'IBM': 125, 'ACME': 50, 'PHP': 40}
print(total_shares)

#solution 2
from collections import Counter
total_shares = Counter()
for name, shares, _ in portfolio:
 total_shares[name] += shares
# total_shares = Counter({'IBM': 125, 'ACME': 50, 'PHP': 40})


#Using a dictionary comprehension create a dictionary with n associated to the nth prime number for the 
#first k primes. K is provided by the user and is not part of the comprehension.
#Using a dictionary comprehension create a dictionary with n associated to the nth prime number for the 
#first k primes. K is provided by the user and is not part of the comprehension.

def isPrime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

n = 10
prime_list = [i for i in range(1,n**2) if isPrime(i)]

prime_dict = {i:prime_list[i-1] for i in range(1,n+1)}
print(prime_dict)

#Shallow copy: A shallow copy creates a new object that is a copy of the original object,
#but the contents of any mutable objects within the original object are not copied. Instead, 
#the new object contains references to the same mutable objects as the original object. Therefore,
#if you modify one of the mutable objects in the new object, the same change will be reflected in the original object as well.
#Shallow copy is done using the copy() method or the slice operator ([:]).

#Deep copy: A deep copy creates a new object that is a complete copy of the original object,
#including any mutable objects within the original object. Therefore,
#if you modify one of the mutable objects in the new object, the original object will remain unchanged.
#Deep copy is done using the deepcopy() method from the copy module.
#Shallow copy example
original_list = [1, 2, [3, 4]]
shallow_copy = original_list.copy()
shallow_copy[2].append(5)
print(original_list)    # Output: [1, 2, [3, 4, 5]]
print(shallow_copy)    # Output: [1, 2, [3, 4, 5]]

# Deep copy example
original_list = [1, 2, [3, 4]]
deep_copy = copy.deepcopy(original_list)
deep_copy[2].append(5)
print(original_list)    # Output: [1, 2, [3, 4]]
print(deep_copy)    # Output: [1, 2, [3, 4, 5]]

#Dictionaries and **kwargs in Python functions
def my_func(**kwargs):
 for key, value in kwargs.items():
    print(f"{key}: {value}")
my_func(apple=3, banana=5, orange=2)

def z(a,*b,**c): # recall the order 
    print(type(a),type(b),type(c))
    print(a,b[1],c,sep='\n')
    print(len(c),list(c.items()))
    g=list(c.items())
    c[g[0]]=156
    print(c.items())
    print (type(c.items()))
    d=[i for i in c.keys()]
    print(c[d[0]])
    print()
    z=list(c)
    print(c[list(c)[0]])
    print()
    for i in iter(c):
        print(i)
 
 
z(12,3,4,5,k=87,l=19)

#Write a function, signature(n) that and returns a string with same letters in lexicographic order.
#For example, signature(stop) ➔ opst
def signature(n):
    """Returns a string with the letters of the input string sorted in lexicographic order."""
    return ''.join(sorted(n))

#Scrabble Descrambler – Very Lite

word_list = []
with open("C:/Users/Owner/OneDrive/Desktop/Python Code/text file/wordlist.txt") as file:
  for line in file:
    #get rid of the newline character
    current_word = line.strip()
    sorted_letters = "".join(sorted(current_word))
    print(sorted_letters)
    #word_list.append((sorted_letters, current_word))

#TASK 3: Sort the list of tuples created in step 2 by the signature.

sorted_words = sorted(word_list, key =  lambda x : x[0])
print(sorted_words)

# TASK 4: Go through the list created in step 3 and create a Python dictionary where for each entry, the key is the
# signature and the associated value is a list of all words with the same signature.

# so we want a dictionary where the key is the letters in alphabetical order
# and the value is a list of all words that can be formed with those letters
# example: the key OPTS should have [STOP, POTS, TOPS, etc]

word_dict = {}
for letters, word in sorted_words:
  # if the list exists, return it. if not, return an empty list that we can work with
  word_list = word_dict.get(letters, [])
  word_list.append(word)
  word_dict[letters] = word_list

# make sure it works
# for letters in word_dict:
#   if len(word_dict[letters]) > 3:
#     print(letters)
#     print(word_dict[letters])

# TASK 5: Finally, in a loop, ask the user for the six letters that they want to look up, and your program will return
# all valid six-letter Scrabble words matching the rquest.

user_letters = input("Enter your letters: ")

#no guarantee that the letters are sorted from the user!
sorted_user_letters = "".join(sorted(user_letters.upper()))

user_word_list = word_dict.get(sorted_user_letters, "no words available")

print(user_word_list)

#use the pickle function to save a list of numbers to a file:
import pickle

numbers = [1, 2, 3, 4, 5]
with open("numbers.pkl", "wb") as f:
 pickle.dump(numbers, f) # dump the object to a file 存储
 

with open("numbers.pkl", "rb") as f:
 restored_numbers = pickle.load(f) # load the object from the file 加载
print(restored_numbers)

#Here is another example. 
#We create our Scrabble dictionary and then pickle it for later use. 
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



import string


#open the file, get the contents into a list of tuples
word_list = []
with open("C:/Users/Owner/OneDrive/Desktop/Python Code/Advanced-Python-Programming/text file/templates/381p_inverted.txt") as file:
 line_number = 0
 index_dict = {}
 for line in file:
   line_number += 1
   table = str.maketrans('', '', string.punctuation) #remove punctuation 替换所有标点符号为空None
   current_line = line.lower().translate(table).split()
   #print("the current_line is",current_line, line_number)
   #output the current_line is ['four', 'score', 'and', 'seven', 'years', 'ago', 'our', 'fathers', 'brought', 'forth', 'on', 'this', 'continent', 'a', 'new', 'nation', 'conceived', 'in', 'liberty', 'and', 'dedicated', 'to', 'the', 'proposition', 'that', 'all', 'men', 'are', 'created', 'equal'] 1
   for word in current_line:
     if word in index_dict:
       index_dict[word].append(line_number)
     else:
       index_dict[word] = [line_number] 
for word, index_list in index_dict.items():
    print(word + ": ") #output four:
    print(index_list) # index_list range from 1 to 3
#output: for people
#people:
#[3, 3, 3]
#because the word people appears 3 times in line 3
#output: for it
#it:
#[2, 3, 3, 3, 3]
#because the word it appears 4 times in line 3 and 1 time in line 2

#maketran example, replace all punctuation with None
'''
import string
s = "Hello, world! This is a string with punctuation."
table = str.maketrans('', '', string.punctuation)
s = s.translate(table)
print(s)  # Output: Hello world This is a string with punctuation
'''
#index_dict[word].append(line_number)

#append example
'''
my_dict = {"key1": "value1", "key2": "value2", "key3": ["value3a", "value3b"]}
my_dict["key3"].append("value3c")
print(my_dict)
#output {'key1': 'value1', 'key2': 'value2', 'key3': ['value3a', 'value3b', 'value3c']}
'''

#another version:
# Part 1: Create a simplified inverted index
invertedDict = {}

# Read the text file
with open("C:/Users/Owner/OneDrive/Desktop/Python Code/Advanced-Python-Programming/text file/templates/381p_inverted.txt", "r") as f:
    # Loop over each line in the file
    for lineNum, line in enumerate(f, start=1):
        # Split the line into words
        words = line.split()
        # Loop over each word in the line
        for word in words:
            # Add the line number to the list for the word in the inverted index
            if word in invertedDict:
                invertedDict[word].append(lineNum)
            else:
                invertedDict[word] = [lineNum]
# Part 2: Define the squish function
def squish(x):
    # Create a dictionary to count the number of occurrences of each line number
    counts = {}
    for num in x:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    # Convert the dictionary to a list of tuples
    return list(counts.items())
# Part 3: Create a full inverted index with counts
invertedDict = {}

# Read the text file
with open("C:/Users/Owner/OneDrive/Desktop/Python Code/Advanced-Python-Programming/text file/templates/381p_inverted.txt", "r") as f:
    # Loop over each line in the file
    for lineNum, line in enumerate(f, start=1):
        # Split the line into words
        words = line.split()
        # Loop over each word in the line
        for word in words:
            # Add a tuple of (line number, count) to the list for the word in the inverted index
            if word in invertedDict:
                invertedDict[word].append((lineNum, 1))
            else:
                invertedDict[word] = [(lineNum, 1)]
print(invertedDict)