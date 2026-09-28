# 2. Prime checker   
# Task: Read an integer and determine whether it is prime.

a=int(input("enter number: "))
prime=1
if a<2:
    print("not prime")
    exit()
elif a<4:
    print("prime number")
    exit()
for i in range (2,(a//2)+1):
    if a%i==0:
        prime=0
        break
if prime==1:
    print("prime number")
elif prime==0:
    print("not prime")