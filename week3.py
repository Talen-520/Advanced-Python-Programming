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


