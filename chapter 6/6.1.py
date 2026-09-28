# 1. Greatest of four   
# Task: Read four numbers and print the greatest one.
# Do not use max().

greatest=int(input('enter number: '))
for i in range(3):
    a=int(input("enter number:"))
    if(a>greatest):
        greatest=a
print("greates number is: ",greatest)