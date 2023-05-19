#在Python中，装饰器（decorator）是一种用于修改函数或类的功能的语法构造。它们允许您在不改变函数本身的情况下修改函数的行为。
#装饰器实际上是一个函数，它接受一个函数作为输入，并返回一个新函数。新函数通常会包装或修改原始函数，从而实现所需的功能
#A decorator in Python is a way of modifying or extending the behavior of a function or class without changing its source code.
# Decorators are used to add functionality to an existing function or class, and they do this by wrapping the original function or class with another function. 
#In Python, decorators are implemented using the @decorator_name syntax.
import functools
def my_decorator(func):
  """ decor"""
  @functools.wraps(func)
  def wrapper(*args, **kwargs):
    """ wrapper"""
    print("Before the function is called.")
    result = func(*args, **kwargs)
    #print(result)
    print("After the function is called.")
    return result
  return wrapper
@my_decorator
def my_function(x,y):
 """ my func"""
 return x+y
def abe(x,y):
  """ sec func"""
  return x**y
z=my_function(2,3)
print(z,my_function.__name__) # Output: "my_function"
print(z,my_function.__doc__) #my func
print(z,my_decorator.__doc__)#decor
print(z,my_decorator.__name__)#my_decorator
e=my_function(2,4)
c = abe(2,3)
print(c)
print(abe.__doc__)
@my_decorator
def abc(x,y):
  """ 3rd func"""
  return x-y
d = abc(2,3)
print(d)

