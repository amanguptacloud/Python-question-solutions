# 3. First n natural numbers   
# Task: Read n and calculate the sum of the first n
# natural numbers using a while loop.

a=int(input("value of n: "))
sum=0
x=1
while(x<a+1):
    sum+=x
    x=x+1
print("Result:",sum)
