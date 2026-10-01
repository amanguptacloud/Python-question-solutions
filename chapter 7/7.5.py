# 5. Factorial   
# Task: Calculate n! using a for loop and
# then test the program on 0, 1, 5, and a larger value.

a=int(input("enter input: "))
fact=1
for i in range(1,a+1):
    fact=fact*i
print("result: ",fact)