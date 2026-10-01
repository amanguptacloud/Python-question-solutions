# 4. Skip and stop exercise   
# Task: Print numbers from 1 to 50, skip multiples of 3,
# and stop completely when you reach 41.

for i in range(1,50):
    if i==41:
        break
    if i%3!=0:
        print(i)
    elif i%3==0:
        continue