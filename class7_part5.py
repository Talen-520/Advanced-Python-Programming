import random

#Ask the user for three integer n and m and k, where k>m*n.
#Create a two dimensional table (list of lists) x of size n*m. Populate the list with n*m unique random
#integers in the range 1 through k.
"""
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
"""