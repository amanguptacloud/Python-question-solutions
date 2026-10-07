# 2. Greatest of three function   
# Task: Create a function that receives three numbers and returns the greatest.

def greatest(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    elif c>=a and c>=b:
        return c

a,b,c=map(int,input("enter 3 numbers: ").split())

print(greatest(a,b,c))