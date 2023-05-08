'''
#code segment 
#run time stack, automitic like int c;
#heap example: a = new int (10) ------new to allocate memory 
#python: everything is object on the heap

dir(int)
# expression example: x=1
1.Value ------x=5, value is x,return the name of left hand side
2.side effect ------when we assing new value for x, it will be change to new value like x = 4


:= is vaild operator that allows for assignment of variable within operation
print(a:=9) # a is asigned 9, then print a
a
-> return 9
'''

#round(0.5) = 0 , banker's algorithm, rounded to nearest integer 2.5 = 2   3.5 = 4
#Write a program that asks the user to enter an integer. Your program should “echo” the input and print True if the number is even and False if the number is odd.

#x=int(input("enter a number"))
#print(x,bool(not x%2))

#Write a program that asks the user to enter an integer. Your program should “echo” the input and print EVEN if the number is even and ODD if the number is odd.
#x=int(input("enter a number"))
#print(x,(x%2==0)*"even" + (x%2!=0)*"odd")

'''
x = int(float(input("enter your number"))*100)
print("half dolloar",x//50)
x%=50
print()
q=x//25
x%=25

d=x//10
x%=10

n=x//5
p=x%5
'''
'''
#python salary  
h = eval(input("hours worked: ")) #hour
r = eval(input("your hourly rate: "))# $/hour
print("your salary base on straight pay, overtime pay, total pay is  ",m:=(h<40)*(r*h)+(h>40)*(r*40),n:=(h>40)*(r*1.5*(h-40)) ,m+n )
#straight pay = m:=(h<40)*(r*h)+(h>40)*(r*40)
#overtime pay = n:=(h>40)*(r*1.5*(h-40))
#total pay = m+n
'''

#unpacking --- x,y,z = 1,2,3
#swap --- x,y = y,x 
'''
intput = int(input("your number "))
if intput % 2 ==0:
    print("even")
if intput % 2 ==1:
    print("odd")
#else:
#   print("odd")
number = "odd"
if intput % 2 == 0
    intput == "even"
print(intput)
'''
intput = int(input("enter a number 1,2 or 3:  "))
v = "ERROR"
if intput == 1:
    print("red")
if intput == 2:
    print("green")
if intput == 3:
    print("blue")
else:
    print("ERROR")
