# 3. Temperature converter   
# Task: Create functions for Celsius→Fahrenheit and Fahrenheit→Celsius. Let the user choose the direction.

def c2f(c):
    F = (c * 9/5) + 32
    return F
def f2c(f):
    C = (f - 32) * 5/9
    return C

a=input("which operation (c2f or f2c?):")
match a:
    case 'c2f':
        c=int(input("enter celcius:"))
        print(c2f(c))
    case 'f2c':
        f=int(input("enter fahrenheit:"))
        print(f2c(f))
    case _:
        print("wrong input, try again.")