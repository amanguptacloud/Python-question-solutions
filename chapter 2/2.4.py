# 4. Remainder and divisibility checker
# Task: Take two integers and report the remainder
#       and whether the first is divisible by the second.

a=int(input("enter 1st number: \n"))
b=int(input("enter 2nd number: \n"))

result=a%b
print("remainder: ",result)
if result==0:
    print(a,"is divisible by",b)
else:
    print(a,"is not divisible by",b)