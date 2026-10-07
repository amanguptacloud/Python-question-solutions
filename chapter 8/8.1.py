# 1. Reusable calculator functions   
# Task: Write separate functions for add, subtract, multiply,
# and divide. A main section should call them for user-entered numbers.

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multi(a,b):
    return a*b

def divide(a,b):
    return a/b

a=int(input("enter value of a:"))
b=int(input('enter value of b:'))
opera=input("enter operation(+,-,x,/): ")

match opera:
    case '+':
        print(add(a,b))
    case '-':
        print(sub(a,b))
    case 'x':
        print(multi(a,b))
    case '/':
        print(divide(a,b))