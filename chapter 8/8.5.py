# 5. Pattern function   
# Task: Write a function that prints a descending star pattern for n lines.

def star(n):
    for i in range(n,0,-1):
        print("*"*i)

a=int(input("enter n:"))
star(a)