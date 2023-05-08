'''
x = int(input("enter your number"))
y = int(input("enter your 2nd number"))
if x > y :
    print(x)
else:
    print(y)
'''
'''
print largest of 5 number
x, y, z, h, z = [int(x) for x in input("Enter three values: ").split()]
large = x
if y > large:
    large = y
if z
'''

'''

x=1
y=2
z=3
if x > 9: 
    if y > 8: 
        print("x>9andy>8") 
    else: 
        if z >= 7: print("x<=9andz>=7")
else: print("x<=9andz<7")
'''

'''

inletter = 'N/A'
grade = input("enter your grade")
if grade > 90:
    inletter = 'A'
elif grade > 80:
    inletter = 'B'
elif grade > 70:
    inletter = 'C'
elif grade > 60:
    inletter = 'D'
else:
    inletter = 'F'
print(inletter)
'''

'''

num = int(input("Enter a 4 digit number: "))
if num > 9999 or num < 1000:
    print("ilegal input")
else: 
    dig1 = num % 10
    num //= 10
    dig2 = num % 10
    num //= 10
    dig3 = num % 10
    num //=10
    dig4 = num 
    if dig1 == dig4 and dig2 == dig3:
        print("palindron") 
    else:
         print("not a palindron")  
'''

'''
num = int(input("Enter a 3 digit number: "))
if num > 999 or num < 100:
    print("ilegal input")
else: 
    dig1 = num % 10
    num //= 10
    dig2 = num % 10
    num //= 10
    dig3 = num % 10
    print(dig1*100+dig2*10+dig3)
'''

'''

num = int(input("Enter a single digit number: "))
if num > 9 or num < 0:
    print("ilegal input")
else: 
    while num !=0:
        print(num)
        num-=1
'''
# output even number
'''
num = int(input("Enter a single digit number: "))
if num > 9 or num < 0:
    print("ilegal input")
else: 
    while num!=0:
        if num % 2 ==0:
            print(num)
    num-=1
'''
# print triangle
'''
count = 1
num = int(input("Enter a positive number between 1-10: "))
if num > 10 or num < 1:
    print("ilegal input")
else: 
    while count != num+1:
        print(count*"*")
        count+=1
    while count != 0:
        print(count* "*")
        count-=1

'''
# print sum of 1 to n
'''

num = int(input("Enter  a number 1-10: "))
count = 1
sum = 0
if num > 10 or num < 1:
    print("ilegal input")
else: 
    while count<=num:
        sum +=count
        count+=1
print(sum)
'''
#2 digit password
'''

a = int(input("Enter  2 digit password: "))
if a > 99 or a < 10:
    print("ilegal input")
else: 
    count = 0
    firstdig = a//10
    seconddig = a % 10
    while count != 4:
        if count == 3:
            print("too many tries,try again later")
            count += 1
        elif firstdig % 2 == 0 and seconddig % 2 == 0:
            print("correct")
            count = 4
        else:
            print("Invalid password. Try again")
            a = int(input())
            count += 1
'''

#ask a postive number and constuct output result backfoward 
'''

a = int(input("Enter  a positive number: "))
result = 0
if a % 10 == 0:
    print("invaild input")
else:
    while a !=0:
        #print(a%10)
        result = result*10 + a%10 
        a = a//10 
    print(result)
'''
a = int(input("Enter  a positive number: "))
i = 2
flag = "prime number"
if a<0:
    print("invaild input")
else:
    while(i!=(a/2)-1):
        if a%i == 0 :
            flag ="not prime number"
            i = a/2-1
        else:    
            i+=1
    print("This is ", flag)


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

#LEGB: Local, Enclosing, Global, Built-in
#First, Python looks for a local variable in the current function.
#If it doesn’t find one, it looks for an enclosing variable in the current scope.
#If it doesn’t find one, it looks for a global variable in the current module.
#If it doesn’t find one, it looks for a built-in variable in the built-in module.
#If it doesn’t find one, it raises an exception.

#What if I want to change the value of x, a local variable in the enclosing function? It’s not global, so the 
#global declaration won’t work. In Python 3, though, we have the nonlocal keyword. This keyword tells 
#Python: “Any assignment we do to this variable should go to the outer function, not to a (new) local 
#variable”; 
def foo():
   call_counter = 0 
   def bar(y):
      nonlocal call_counter
      call_counter += 1 
      return f'y = {y}, call_counter = {call_counter}'
   return bar
b = foo()
for i in range(10, 100, 10): 
   print(b(i)) 
 

#Keyword Arguments vs Positional Arguments 
#关键字参数和位置参数
#关键要key，位置则对应位置


def func(w, x, y, z):
 statements
# Keyword argument invocation
func(x=3, y=22, w='hello', z=[1, 2])

#the order of the arguments doesn’t matter as long as each required parameter gets a single value
#omit any of the required arguments or if the name of a keyword doesn’t match any of the parameter 
#names in the function definition, a TypeError exception is raised
#不能省或缺任何一个,否则会报错，顺序随意
def func(w, x, y, z):
 statements
func('hello', 3, z=[1, 2], y=22) # note z before y, but that’s OK
func(3, 22, w='hello', z=[1, 2]) # TypeError. Multiple values for w
func(3, 22, y='hello', z=[1, 2]) # This does work



#modify and reassign
def square(items):
 for i, x in enumerate(items):
   items[i] = x * x # Modify items in-place
a = [1, 2, 3, 4, 5]
square(a) # Changes a to [1, 4, 9, 16, 25]


print(a)


def sum_squares(items):
   items = [x*x for x in items] # Reassign "items" name
   return sum(items)
a = [1, 2, 3, 4, 5]
result = sum_squares(a)
print(a) # [1, 2, 3, 4, 5] (Unchanged)
print(result) # 55 (Sum of squares
print(a[2:])


a = list("hello")
print(a)#['h', 'e', 'l', 'l', 'o']


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
#print(sorted(student_tuples, key=lambda student: student[2]) ) #lambda element: element[2] is the same as lambda student: student[2],sort by ascending order

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
