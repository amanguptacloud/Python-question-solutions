# 2. Unique-number collector   
# Task: Take eight numbers from the user
#  and print each unique number only once.

a=set(map(int,input("enter 8 numbers: ").split()[:8]))
print(a)
a=list(a)
a.sort()
print(f"sorted amount:{a}")