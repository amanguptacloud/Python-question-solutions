# 1. Name formatter
# Task: Ask for a full name and print a cleaned version with the first letter capitalized
#  and leading/trailing spaces removed.

a=input("enter full name")
a=a.strip()
a=a.capitalize()
print(a)