
#part 3
# Ask the user for a positive integer n
"""
n = int(input("Enter a positive integer: "))
# Check if n is positive
if n > 0:
    for i in range(1, n + 1):
        print(i)
else:
    print("Invalid input. Please enter a positive integer.")
"""

#Write a program that asks the user for a positive integer n. It then prints the numbers n down to1,one per line.
#n = int(input("Enter a positive integer: "))
#for loop
"""
if n > 0:
    for i in range(n,0,-1):
        print(i)
else: 
    print("error")
"""
#while
"""
while(n>0):
    print(n)
    n-=1
"""

#Write a program that asks the user for a positive integer n (>= 2). It then prints the even numbers in the range 1 to n, one per line. 
"""
n=int(input("enter a postive integer "))
i = 2
while(i<=n):
    print(i)
    i+=2
"""

#Write a program that asks the user for a positive integer n. Calculate and print the productof the integers1 through n
#for loop
"""
n=int(input("enter a postive integer "))
result = 1
for i in range(1,n+1):
    result = result * i
print(result)
"""
#Write a program that asks the user for a positive integer n. Calculate and print the sum of the odd integers in the range 1 through n. 
"""
n=int(input("enter a postive integer "))
result = 0
for i in range(1,n+1):
    if(i%2!=0):
        result = result + i
print(result)
"""
#Generate and print all numbers between 1 and 1000 such that the sum of the digits equals 20.
"""
for i in range(1,1001,1):
    if(i>99):
        if(i%10+(i//10)%10+i//100 == 20):
            print(i)
            """
#Generate and print all prime numbers between 1 and 100.  
"""
for i in range(2,101):
    is_Prime = True
    for j in range(2, int(i**0.5)+1):
        if(i%j==0):
            is_Prime = False
            break
    if is_Prime:
        print(i)
"""
#Write a program using for loops to print the following: 
"""
for i in range(1,5):
    for j in range(1,5):
        print('(',i,',',j,')',end='')   
    print('\n')
    """
#Write a program, using for loops, to generate the following output. 
"""
for z in range(1,10):
    print((z-1)*' ',end="")
    for i in range(z,9):
        print(i,end="")
    print(9,end="")
    for i in range(8,z-1,-1):
        print(i,end="")
    print('\n')
"""
#The continue statement is used to skip the remaining code inside a loop for the current iteration only. Loop does not terminate but continues on with the next iteration.
"""
for i in range(1,5):
    for j in range(1,5):
        if (i+j)%2 == 0:
            continue #skip the rest of the code in the loop, print the next iteration
        print('(',i,',',j,')',end=' ')
    print()#print a new line
"""

#break statement is used to terminate the loop containing it. Control of the program flows to the statement immediately after the body of the loop.
"""
for i in range(1,5):
    for j in range(1,5):
        if (i+j)%2 == 0:
            break #skip the rest of the code in the loop, print the next iteration
        print('(',i,',',j,')',end=' ')
    print()
"""
#for n in range(1, 10):
#    print(f'2 to the {n} power is {2**n}')

#for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
#    print(f'2 to the {n} power is {2**n}')
"""
message = 'Hello World'
# Print out the individual characters in message
for c in message:
    print(c)
"""

"""
names = ['Dave', 'Mark', 'Ann', 'Phil']
# Print out the members of a list
for name in names:
    print(name)
"""
"""
prices = { 'GOOG' : 490.10, 'IBM' : 91.50, 'AAPL' : 123.15 }
# Print out all of the members of a dictionary
for key in prices:
    print(key, '=', prices[key])
    """