#name = input("what is your name?")
#print("hello",name,sep = '')
#in python, space is default between variable,+ or sep ='' could eliminate it

# python is interperted language
# sep default is space

#part 2
#print("what is temperature in Fahrenheit")
#Fahrenheit = int(input())
#centigrade = (Fahrenheit-32)/1.8
#print("temperature in centigrade is",centigrade)

#part 3
#for i in range(5):
 #   print(i,'hello')

#part 4
from turtle import *
#penup()
#pendown()
#forward(n) - move n positions in the direction the turtle is pointing
#back(n) -
#right(n) - rotate the turtle n degrees in clockwise direction
#left(n)

#squre
'''
for i in range(16): 
    if i % 4 ==0:
        right(90)
        pendown()
        forward(100) 
        #penup() 
        #forward(25)
    else :
        pendown()
        forward(25) 
        #penup() 
        #forward(25)
'''
#triangle
'''
for i in range (3):
    right(120)
    pendown()
    forward(100) 
for i in range (3):
    left(120)
    pendown()
    forward(100) 
#六边形
for i in range (6):
    right(60)
    pendown()
    forward(100) 
'''

#circle  圈圈⭕️

#for i in range (360):
 #   right(1)
  #  #pendown()
   # forward(2)    

#⭐️
'''
for i in range (5):
    pendown()
    forward(100) 
    right(144)
'''

#内置三角形
'''
for i in range (100):
    forward(10+5*i)
    right(120)
    '''
# The Python “sum” program
'''
print("Welcome to the addition program.")
print("You can enter values for x and y and I will calculate ")
print("and display the sum.") 
print() # prints a blank line
x=input("Please enter a value for x (entering 'done' terminates the program): ")
while x !='done': # this a ‘while loop’. It’s an example of “control”. 
    x=int(x)
    y=int(input("Please enter a value for y: ")) 
    sum=x+y
    print("The sum of ",x," and ",y," is: ",sum) 
    print()
    x=input("Please enter a value for x (entering 'done' terminates the program): ")
print()
print("Thanks for trying our program!")
'''

print(3*'hello')