# 4. Simple username validator   
# Task: Reject a username if it is longer than 10 characters
# or contains spaces; otherwise accept it.

a=input("enter username: ")
if len(a)>10 or " " in a:
    print('wrong username')
else:
    print("correct")