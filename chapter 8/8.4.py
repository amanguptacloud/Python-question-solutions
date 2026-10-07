# 4. Recursive sum   
# Task: Write a recursive function that returns the sum of the first n natural numbers.

def add(a):
    if a<1:
        return 0
    else:
        return a+add(a-1)

a=int(input("enter range:"))

print(add(a))