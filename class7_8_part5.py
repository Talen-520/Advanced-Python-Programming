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
def 
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