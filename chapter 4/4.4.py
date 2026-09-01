# 4. Tuple immutability experiment   
# Task: Create a tuple, try to change one element,
#       and then rewrite the code so the data can be changed safely using a list.

# tpl=(2,"apple","egg",43,'a')
# print(tpl)
# tpl[3]=23
# print(tpl)
# This causes TypeError because tuples are immutable.

lst=["apple","egg",2,54,3.5]
print(lst)
lst[4]=34
print(lst)