# 1. Marks manager
# Task: Read six student marks into a list, 
#    print the original list, then print the sorted list and highest/lowest mark.

lst=[]
lst=input("enter 6 marks seperated by marks").split()
mark=list(map(int,lst))
print(mark)
mark.sort()
print(mark)
print(max(mark))
print(min(mark))