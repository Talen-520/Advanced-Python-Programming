#no static keyword in python
#function that returns next pos even int (using globals)

#Write a function f with the following behavior: each time f is called it returns the next positive even 
#integer. So, the first time it is called it returns 2, the next time 4 and so on.
x = 0
def f():
    global x
    x+=2
    return x
print(f())#2
print(f())#4    
print(f())#6
#Now do it without global variables.
def even_numbers():
    n = 2
    while True:
        yield n #yield is like return but it returns a generator object, w
        n += 2

next_num = even_numbers()
print(next(next_num))#2 
print(next(next_num))#4 second time back to yield n, then go to next line n+=2 then go back to yeid n
#第二次next()时，再次返回yield n =》再次返回n+=2=》再次返回yield n 然后print 4 yield
# 后面的过程会被全部执行然后再返回yeild n

#yield is used instead of return in generator functions 
#because it allows the function to generate a series of values one at a time,
#instead of returning them all at once.

#the main difference between a generator and a generator object is that the generator is the 
#function itself, while the generator object is the iterable object that is produced by the generator 
#function. The generator function is the blueprint for the generator object, defining how values should 
#be generated and returned, while the generator object is the actual instance of the generator, used to 
#iterate over and generate the values.

def even_numbers(n):
    i = 0
    while i < n:
        yield i
        i += 2
even_gen = even_numbers(10)#
for num in even_gen:
 print(num)#0, 2, 4, 6, 8 at once


def countdown(n):
 print('Counting down from', n)
 while n > 0:
    yield n
    n -= 1
for x in countdown(10):
 print('T-minus', x)#T-minus 10, T-minus 9, T-minus 8, T-minus 7, T-minus 6, T-minus 5, T-minus 4, T-minus 3, T-minus 2, T-minus 1 at once

c = countdown(10)
print(c)#<generator object countdown at 0x0000020F4F6F7C80>
print(next(c))#10
print(next(c))#9


#Write a generator that will yield the “next” prime number each time that it’s called.
def next_prime():
    n = 2
    primes = []
    while True:
        is_prime = True 
        for p in primes:
            if n % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)#[2,3,5,7,11,13,17,19,23,29] only primes are appended, so next time the for loop runs, it will only check if n is divisible by the primes in the list
            yield n
        n += 1
prime_generator = next_prime()
for _ in range(10):
    print(next(prime_generator))



#Write a generator that will yield the “next” leap year each time that it’s called.

#The year must be evenly divisible by 4;
#If the year can also be evenly divided by 100, it is not a leap year;
#but If the year can also be evenly divided by 100, it is not a leap year;
#能被4 整除， 不能被100整除除非能被400整除

def leap_year():
    x = 4
    while True:
        if (x%4 == 0 and x%100 != 0) or x %400 ==0:
            yield x
        x+=4
x = leap_year()
for _ in range(100):
    print(next(x))

#Using a generator, create a dictionary such that d[i] is mapped to the ith prime number. 
#Can you also do this with a dictionary comprehension?

def prime_generator():
    x = 2
    list = []
    while True:
        is_prime = True
        for i in list:
            if x % i ==0:
                is_prime = False
        if is_prime:
            list.append(x)
            yield x
        x+=1
p = prime_generator()
d = {i:next(p) for i in range(1,11)}
print(d)

#Write a generator get_oct() that will produce the next octal number each time it’s called. The value 
#should be a string, so that when the octal number 20 is produced (this is the octal representation for 
#the decimal 16) the generator will return ‘20’
def get_oct():
 current_dec = 1
 while True:
   yield str(oct(current_dec))[2:]
   current_dec += 1
#num = 16
#oct_num = oct(num)
#print(oct_num)   # Output: '0o20'

n = get_oct()
for x in range(100):
 print(next(n))



#Write a generator that produces “serial numbers” according to the following rule: a serial number is a 
#ten-character string where
#• the first two characters are upper-case alphabetic and
#• the following eight are numeric. 
#The alphabetic portion will be all strings from AA through ZZ in lexicographic order (AA,AB,AC 
#…). For each alphabetic prefix, the numeric part will be all strings 00000000 – 99999999. So we 
#have AA00000000, AA00000001 …ZZ99999999.
def serial_numbers():
  init_letter = 'AA'
  init_digit = 00000000
  count = 0
  while count<=9999999999:
    yield init_letter + str(init_digit).zfill(8) #padding from left with 0, 8 digital number
    init_digit+=1
    if init_digit == 100000000:
      init_digit ==0
      init_letter[1] = chr(ord(init_letter[1])+1)
      if init_letter[1] == chr(ord('Z')+1):
        init_letter[1] ='Z'
        init_letter[0] = chr(ord(init_letter[0])+1)
    count+=1

a = serial_numbers()
print(next(a))
print(next(a))

#Write a generator that monitors a device that periodically sends either a 1 or a 0. The generator keeps 
#track of the number of zeros between receiving a 1. They call that number the gap. Each time a value 
#is received the generator yields the gap.
#For example, say the received sequence is:
#runs=[1,1,0,1,1,0,0,0,1,1,1,1,0,1,0,0,1]
#then the generator will output:
#[0, 0, 1, 0, 3, 0, 0, 0, 1, 2, 0]
#Write the generator

def monitor(n):
  gap = 0
  for i in range (len(n)):
    if n[i] == 0:
      gap+=1

    else:#n[i]==1
      yield gap
      gap = 0

runs=[1,1,0,1,1,0,0,0,1,1,1,1,0,1,0,0,1]
a=monitor(runs)
for gap in a:
  print(gap,end=' ')

#Referring to the problem above. Imagine that the sequence of 1s and 0s represents the state of some 
#security sensor, 1 if available, zero if not. If the gap between 0s exceeds some user defined n, the 
#generator should return a warning and return. Write the modified generator.

def monitor(n,j):
  gap = 0
  count =0
  for i in range (len(n)):
    if n[i] == 0:
      gap+=1
      count+=1
      if(count>=j):
        yield 'warning'

    else:#n[i]==1
      yield gap
      gap = 0

runs=[1,1,0,1,1,0,0,0,1,1,1,1,0,1,0,0,1]
a=monitor(runs,3)
for gap in a:
  print(gap,end=' ')


#problem here is no loop to continue generate vaule
def even_numbers1():
  i = 0
  yield i 
  i += 2
even=even_numbers1()
for _ in range(10):
  print(next(even)) 


#countdown
class countdown:
 def __init__(self, start):
  self.start = start
 def __iter__(self):
  n = self.start
  while n > 0:
    yield n
    n -= 1
c = countdown(5)   # create a countdown object starting at 5
for i in c:        # iterate over the countdown values
    print(i)

