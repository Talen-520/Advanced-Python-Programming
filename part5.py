import random

#Ask the user for three integer n and m and k, where k>m*n.
#Create a two dimensional table (list of lists) x of size n*m. Populate the list with n*m unique random
#integers in the range 1 through k.
'''
n=int(input('Enter a number n: '))
m=int(input("Enter another number m: "))
k=int(input("Enter a third number k>m*n: "))
solution_list=[]
for i in range(n):
    list=[]
    for i in range(m):
        list.append(random.randint(1,k))
    solution_list.append(list)
#num=n*[m*[random.randint(1, k)]]
print(solution_list)
#print(num)
'''

#Ask the user for three integer n and m and k, where k>m*n.
#Create a two dimensional table (list of lists) x of size n*m. Populate the list with n*m unique random integers in the range 1through k.
'''
myList = []
myset = set()
n=int(input('Enter a number n: '))
m=int(input("Enter another number m: "))
k=int(input("Enter a third number k>m*n: "))

while (myset.len<m*n):
    myset.add(random.randint(1,k))

for i in range(n):
    myList.append([])
    for j in range(m):
            myList[i].append(myset.pop())
print (myList)

'''




#Write a function get_row(x,i) which takes a square matrix (=table=list of lists) and returns a list containing the ith row of matrix X.
'''
def get_row(x,i):
    return x[i]
x=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
print(get_row(x,2))
'''
#Write a function get_col(x,i) which takes a square matrix (=table=list of lists) 
# and returns a list containing the ith column of matrix X
'''
def get_col(x,i):
    return [row[i] for row in x]
y = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
print(get_col(y,2))
'''
#Write a function to calculate and return the sum of all the elements on the “main diagonal” of the square two dimensional list x passed to it as an argument. 
#This is the diagonal going from the upper left to the bottom right
'''
def main_diagonal(x):
    Diagonal = []
    for i in range(0,int(len(x)*0.5)+1):
        Diagonal.append(x[i][i])
    return Diagonal
y = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
print(y)
print(main_diagonal(y))
print(sum(main_diagonal(y)))
#Like the problem above, calculate and return the diagonal sum, but for the elements along the diagonal going from the top right to the lower left.
def main_diagonal(x):
    sum = 0
    for i in range(len(x)):
        sum+=x[i][len(x)-i-1]
        print('the {i} row and col is ',x[i][len(x)-i-1])
    return sum
y = [[1,2,3],[4,5,6],[7,8,9]]
print(y)
print(main_diagonal(y))
#[0,2] [1,1] [2,0]
'''
#List Comprehensions
'''
a=[x**2 for x in range(1,101) if x % 2 == 0]
print(a)
#equvalent to 
a=[]
for x in range(1,101):
    if x%2==0: 
        a.append(x)
print(a)
'''
#dot
'''
x=[1,2,3]
y=[10,11,12]
z=sum([x[i]*y[i] for i in range(len(x))])
print(z)
'''
#Write a function dot(x,y) which takes two lists of equal length and returns the dot product of the two lists.
'''
def dot(x,y):
    return sum([x[i]*y[i] for i in range(len(x))])
'''

#Write a function sum_col(x,i) which takes a square matrix (=table=list of lists) and the sum of the
#items in the ith column of matrix X. Use a list comprehension.
'''
def sum_col(x,i):
    return sum([x[j][i] for j in range(len(x))])
y=[[1,2,3],[4,5,6],[7,8,9]]
print(sum_col(y,2)) #3+6+9=18
'''
#Write a function diag_diff(x,i) which takes a square matrix (=table=list of lists) and the difference of two main diagonals of matrix X. In other words, let d1 be the diagonal of X from upper left to bottom right,
#and d2 to be the diagonal from upper right to lower left. The function returns d1-d2. Use list comprehensions.
'''
def diag_diff(X, i):
    d1 = sum([X[j][j+i] for j in range(len(X)-i)])
    d2 = sum([X[j][len(X)-j-1+i] for j in range(len(X)-i)])
    return d1 - d2
'''

#Early versions of Python distinguished between int and long. 
#ints were represented natively on the hardware and longs were lists of integers.
#From version 3.0 and on all integer types are represented as longs.

#Write a function make_int (x: str) -> list:
#that takes a string of digits and returns a list of those digits. Use a list comprehension.
'''
def make_int(x):
    return [int(i) for i in x]
print(make_int('123456789'))
'''
#Write a function int_add(x,y) that takes two “integers” as represented above, and returns their sum.
#Note that these “integers” needn’t be the same size. 
# You can simplify your program by padding the shorter one with zeros (on the left).
#Note as well, there might be a final carry that will increase the answer by one digit more than the addends.
'''
def int_add(x,y):
    if len(x)>len(y):
        y.rjust(len(x),'0')
    else:
        x.rjust(len(y),'0')
    a = [int(i) for i in x]
    b = [int(i) for i in y]
    return [a[i]+b[i] for i in range(len(a))]
print(int_add('1111','11111'))
'''

#Write a function matrix_add(x,y) that takes two square “matrices” and returns their sum.

def matrix_add(x,y):
    return [[x[i][j]+y[i][j] for j in range(len(x))] for i in range(len(x))] #len(x) is the number of rows
x=[[1,2,3],[4,5,6],[7,8,9]]
y=[[10,11,12],[13,14,15],[16,17,18]]
print(matrix_add(x,y))

#Write a function matrix_mult(x,y) that takes two square “matrices” and returns their product.
def matrix_mult(x,y):
    result = []
    for i in range(len(x)):
        result.append([sum([x[i][j]*y[j][i] for j in range(len(x))]) for i in range(len(x))])
    return result

x=[[1,2,3],[4,5,6],[7,8,9]]
y=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix_mult(x,y))

#Write a function that reverses a string. Remember, a string is not mutable! Do it two ways.
#solution 1
def reserve_String(x):
    ans = ''
    for i in x:
        ans = i+ans
    return ans
print(reserve_String('123456789'))
#solution 2
def reserve_string2(x):
    answer=[]
    solution=''
    for i in x:
        answer.append(i)
    answer.reverse()#['9', '8', '7', '6', '5', '4', '3', '2', '1']
    for i in answer:
        solution+=i
    return solution
print(reserve_string2('123456789'))

x = [1, 2, 3, 4, 5]
y = x[::-1]
print(x[::-1])
print(y)
#add two numbers
"""
def addTwoNumbers(l1, l2):
        solution = []
        MaxLen = max(len(l1),len(l2))
        for i in range(0,MaxLen):
            fill = l1[i]+l2[i]
            print(fill)
            if fill > 9 and i == MaxLen-1:
                solution.append(fill-10)
                solution.append(1)
                print(solution,'1st')
            elif fill > 9:
                solution.append(fill-10)
                l1[i+1]=l1[i+1]+1
                print(solution,'2nd')
            else:
                solution.append(fill)
                print(solution,'3rd')
        return solution
a = [2,2,3]
b = [3,8,9]
print(addTwoNumbers(a,b))
"""

#find saddle point
my_array = [[2,0],[0,-2]]
saddlePoints = min(my_array[0])
print(saddlePoints)
result = "not found"
def findSaddlePoints(my_array):
    for i in range(len(my_array)):
        for j in range(len(my_array[i])):
            if i == 0 and my_array[i][j] == saddlePoints:
                x = i
                y = j
            if(i > 0):
                if(my_array[i][y] >= saddlePoints):
                    return result
    return (saddlePoints, x, y)
print(findSaddlePoints(my_array))












#Write a program to generate all the eight-digit base 8 integers from 00000000➔77777777
#What is a base eight integer

for i0 in range(8):
    for i1 in range(8):
        for i2 in range(8):
            for i3 in range(8):
                for i4 in range(8):
                    for i5 in range(8):
                        for i6 in range(8):
                            for i7 in range(8):
                                q=[i0,i1,i2,i3,i4,i5,i6,i7]
                                print(q)
def diagonal_threat(q):
    for i in range(8):
        for j in range(i+1,8):
            if abs(q[i]-q[j]) == j-i:
                return True
    return False
from itertools import permutations
candidates=permutations([0,1,2,3,4,5,6,7])
count=0
for p in candidates:
    if diagonal_threat(p):
        continue
    count+=1
    print('Solution number ', count,': ',p)
    print()


#Write a function clear(x) where x is a list of “words”. Each word is a string that might have either a ‘.’
#‘,’, or’;’ tacked on at the end. clear() will return a list with the original words stripped of the
#punctuation



#Write a function scrape(s) which take a string s representing the HTML of a web page and returns a
#list of all links found on the page. We recognize the beginning of a link by looking for ‘http://’.



#Modify the above program so that it writes the result to a file called averages.


#Unpacking Sequences and Iterables

print(divmod(10,2))
q=(10,2)
#print(divmod(q))  incorrect
print(divmod(*q))

a, b, c = (1, 2, 3)
print(a, b, c)
#1 2 3

a, b, c = "abc"
print(a, b, c)
#a b c

a, b, *c = range(5)
print(a, b, c)
#0 1 [2, 3, 4]

a, b, *rest = range(3)
a, b, rest
#0, 1, [2]
a, b, *rest = range(2)
a, b, rest
#0, 1, []

a, *body, c, d = range(5)
a, body, c, d
#0, [1, 2], 3, 4
*head, b, c, d = range(5)
head, b, c, d
#[0, 1], 2, 3, 4
#Note that the excess items get put into a list.
#In the context of parallel assignment, the * prefix can be applied to exactly one variable, but it can appear 
#in any position


#Nested Unpacking

metro_areas = [
 ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)), 
 ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
 ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
 ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
 ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]
def main():
 print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
 #{} is a placeholder for a value that will be formatted and inserted into the string.
 #:15 in {name:15} and {lat:9.4f} specifies the width of the column, while the >9 in {latitude:>9} and {longitude:>9} specifies the text alignment.
 #> means right alignment, < means left alignment, ^ or no specified means center alignment.
 for name, _, _, (lat, lon) in metro_areas: 
    #_,_, means we are not interested in the second and third element, which will be skipped, 
    #and the fourth element is a tuple of two items with the coordinates, we unpack that into lat and lon.
    if lon <= 0: 
        print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')
        #f-string that includes the name of the metropolitan area, its latitude, and its longitude.
        #The :15 in {name:15} and {lat:9.4f} specifies the width of the column, while the >9 in {latitude:>9} and {longitude:>9} specifies the text alignment.
        #The 9.4f in {lat:9.4f} and {lon:9.4f} specifies the number of decimal places to include in the output.
print(main())

import string
import random
digits = string.digits
print(random.choice(digits))# 0-9
print(digits)#'0123456789'
random_number = ''.join(random.choice(digits) for _ in range(4))# 4 digits, _ is a dummy variable,it is not used, we just need to iterate 4 times
print(random_number)
print(''.join(('1','2')))#join() takes only one argument, so we need to use tuple

#Write a function that reverses a string. Remember, a string is not mutable! Do it two ways.
def reverse_string(s):
    return s[::-1]

def reverse_string(s):
    empty = ''
    for i in s:
        empty = i + empty
    return empty

#Write a function is_len(s,n) which returns True if string s is at least n characters long, and False
#otherwise


def is_len(s,n):
    if len(s) >=n:
        return True
    else:
        return False
print(is_len('hello', 5))
print(is_len('hello', 6))

#Write a function one_upper(s) which returns True if exactly one character in string s is capitalized, and
#False otherwise. You can assume that the string s contains only alphabetic characters and no blanks. You
#might want to consider other string functions from the documentation.
def one_upper(s):
    count = 0
    for i in s:
        if i.isupper():
            count+=1
    return count == 1

#Write a function clear(x) where x is a list of “words”. Each word is a string that might have either a ‘.’
#‘,’, or’;’ tacked on at the end. clear() will return a list with the original words stripped of the
#punctuation
def clear(x):
    result = []
    for i in x:
        result.append(i.replace('.','').replace(',','').replace(';',''))#this replace all the punctuation, not just one
    return result
a = ['hello,','world.','are;','you?']
print(clear(a))

#solution 2
def clear(x):
    result = []
    for i in x:
        result.append(i.rstrip('.,;'))
        #rstrip() removes the specified characters from the right side of the 
        #string.lstrip() removes the specified characters from the left side of the string.strip() removes the specified characters from both left and right sides of the string.
    return result

#Write a program that prompts the user for some integer n, and calculates the number of occurrences of 
#the digit ‘1’ in all the numbers from 1-n inclusive.
s=20
def count_ones(n):
    count=0
    for i in range(1,n+1):
        count+=str(i).count('1')
    return count
print(count_ones(s))

#open file and read
with open('C:/Users/Owner/OneDrive/Desktop/Python Code/text file/text.txt') as f:
    for line in f:
        print(line, end='') # end='' omits the extra newline

#Once control leaves this block, the file is automatically closed. If you don’t use the with statement, the 
#code would need to look like this:
f = open('C:/Users/Owner/OneDrive/Desktop/Python Code/text file/text.txt')
for line in f:
    print(line, end='') # end='' omits the extra newline
file.close()
#output.close() Manual close (done for you when file is collected)
#output.flush() Flush output buffer to disk without closing any File
#It’s easy to forget the extra step of calling close() so it’s better to use the with statement and have the file 
#closed for you

#If you want to read the file in its entirety as a string, use the read() method like this:
with open('data.txt') as file:
 data = file.read()


#Write a program to read this file and print out the students name followed by their average on all
#exams.
with open('C:/Users/Owner/OneDrive/Desktop/Python Code/text file/grades.txt') as f:
    for line in f:
        s = line.split()
        average = sum([int(s[i]) for i in range(1,len(s))])/(len(s)-1)
        print(format(s[0],'<7s'),'Average= ',format(average,'.2f'))
#Modify the above program so that it writes the result to a file called averages.
with open('C:/Users/Owner/OneDrive/Desktop/Python Code/text file/grades.txt') as f,open('C:/Users/Owner/OneDrive/Desktop/Python Code/text file/averages.txt','w') as averageFile:
    for line in f:
        s = line.split()
        average = sum([int(s[i]) for i in range(1,len(s))])/(len(s)-1)
        #print(format(s[0],'<7s'),'Average= ',format(average,'.2f'))
        averageFile.write(f"{s[0]:<7s} Average=  {average:.2f}\n")



