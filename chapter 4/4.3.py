# 3. List total and count   
# Task: Given a list of numbers, calculate its sum without using sum(),
# and count how many values are zero.

lst = [3,6,7,3,7,0,4,0]
result =0
for i in range (len(lst)):
    result = result + lst[i]

print("sum of numbers: ",result)
count =0
for i in range(len(lst)):
    if lst[i]==0:
        count+=1
print("Number of zeroes in list: ",count)