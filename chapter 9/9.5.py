# 5. File copy + compare   
# Task: Create a program that copies one text file to another and
# then checks whether the two files contain identical text.

with open("chapter 9/file1.txt") as f:
    content1=f.read()
with open("chapter 9/file2.txt","w")as f:
    f.write(content1)

with open("chapter 9/file2.txt")as f:
    content2=f.read()

if content1==content2:
    print("both contains identical text")
else:
    print("non identical text")