# 3. Username validator  [Required]
# Task: Ask for a username and reject it if it contains spaces or is shorter than 5 characters.
#  Otherwise accept it.

name=input("enter username: ")
a=len(name)
if " " in name:
    print("spaces not allowed")
elif a<5:
    print("length should be atleast 5 character.")
else:
    print("accepted")