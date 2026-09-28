# 1. Multiplication table   
# Task: Print the multiplication table of a user-entered number
# from 1 to 10 using a for loop.

tab=int(input("enter number:"))
for i in range(1,11):
    print(f"{tab}X{i}={tab*i}")