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