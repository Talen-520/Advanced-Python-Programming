"""
import math#math module
a=math.sqrt(9)

from math import sqrt#import sqrt function from math module
a=sqrt(9)

from math import *#import all the functions from math module
a = sqrt(9) #works

print(a)
"""


#Write a function is_even(x) which returns True if x is even and False otherwise.
"""
def is_even(x):
    if(x%2==0):
        return True
    else:
        return False
print(is_even(2))
"""
#Write a function is_leap(x) which returns True if x is a leap year and False otherwise.Answer:
"""
def is_leap(x):
    if(x%4==0):
        return True
    else:
        return False
print(is_leap(2000))
"""

#Write a function is_prime(x) which returns True if x is a prime number and False otherwise.
"""
def is_prime(x):
    for i in range(2,x):# x = 20,i = 2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19
        if(x%i==0):
            return False
    return True
print(is_prime(2))
"""
#Write a program to ask the user for two integers, first and last. Write a program to print out all the 
#primes between first and last (inclusive), five values per line.
"""
inPut = int(input("Enter two integers, first and last,first is : "))
inPut2 = int(input("last is : "))
count = 0
def is_prime(x):
    if x < 2: 
        return False
    for j in range (2,int(x**0.5) + 1):
         if x%j==0:
            return False
    return True

for i in range (inPut,inPut2+1,1):
    if(is_prime(i)):
        print(i,end=" ")
        count+=1
        if(count%5==0):
            print()
"""


#Write a function sum_of_digits(n) which returns the sum of the digits of n.
"""
def sum_of_digits(n):
    sum = 0
    while(n>0):
        sum+=n%10
        n//=10
    return sum

print(sum_of_digits(1234))
print(sum([1,2,3,4,5]))
"""

#Write a function my_bin(n) which converts an integer number to a binary string representation of n.
#But Leave out the leading ‘0b’ returned by the built in function bin
"""
def my_bin(n):
    a = bin(n)
    b = a[2:]
    return b
print(my_bin(10))
"""
#without bin()
"""
def my_bin(n):
    myBinaryNumber = ''
    while(n > 0):
        if n%2 == 0:
            myBinaryNumber = '0' + myBinaryNumber
        else:
            myBinaryNumber = '1' + myBinaryNumber
        n //=2
    return myBinaryNumber
print(my_bin(10))
"""
#Given a list, print the elements of that list in reverse order. Do this in two ways.

#solution 1
"""
a=[1,2,3]
a.sort(reverse=True)
print(a)
"""
#solution 2
"""
a=[1,2,3]
for i in range(len(a)-1,-1,-1):
    print(a[i])
"""
"""
array = [5,2,3,9,10,1]
b=sorted(array)
#array.sorted()
print(b)
"""

#solution 3
"""
ary=[1,2,3,4,5]
for i in range(1,len(ary)+1):
    print(ary[-i])
"""
#lambda Expressions

#print(sorted("This is a test string from Andrew".split(), key=str.lower))

#student_tuples = [('john', 'A', 15),('jane', 'B', 12),('dave', 'B', 10),]
#print(sorted(student_tuples, key=lambda student: student[2]) )

#Explain the result:
"""
a=[1,2,3]
print(a.sort(reverse=True)==sorted(a,reverse=True))
"""

#Change element with a 50 to 500.
"""
a=[[10,20,30],[40,50,60],(70,80,90)]
a[1][1]=500
print(a)
"""
#print out in this way
"""
for i in range(3):
    for j in range(3):
        print(format(a[i][j],">6d"),end=' ')
    print()
"""

#Create a 4X4 array and initialize each of the elements to 0.
"""
a=[]
for i in range(4):
    a.append(4*[0])
    #[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    #4*[8] = [[8, 8, 8, 8], [8, 8, 8, 8], [8, 8, 8, 8], [8, 8, 8, 8]]
print(a)
"""
#extend
"""
a=[1,2,3]

print(a+[4])
a=4*[8]
print(a)
"""
#Make sure that you can explain each of the following:
"""
a=3*3*[[0]]#3*3*[[0]] = 3*3*[[0, 0, 0, 0]]
print(a)
a=3*3*[0]#3*3*[0] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
print(a)
#third example
a=3*[3*[0]]#3*[3*[0]] = [3*[0], 3*[0], 3*[0]]
print(a)
"""
#The fourth example (below). Does this produce the same result as third example above?
"""
a=[]
for i in range(3):
    a.append(3*[0])
print(a)
"""
#However, internally they are represented very differently.
