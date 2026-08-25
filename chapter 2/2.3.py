# 3. Pass/fail calculator  [Required]
# Task: Take three subject marks and calculate total, average percentage,
#       and whether the student passes a rule you define explicitly.

a=int(input("enter marks of sub 1: \n"))
b=int(input("enter marks of sub 2: \n"))
c=int(input("enter marks of sub 3: \n"))

d=a+b+c

print("total marks: ",d,"\n")
print("average percentage: ",d/3,"%")
if d>=120:
    print("pass\n")
else:
    print("fail\n")