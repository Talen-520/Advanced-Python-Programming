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