# 2. Fruit list from user   
# Task: Ask the user for seven fruits and store them in a list.
#       Print them one per line with numbering.

fruit=input("enter 7 fruit name seperated by space: ").split()
for i in range(len(fruit)):
    print(i+1,fruit[i])