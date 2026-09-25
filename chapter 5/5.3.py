# 3. Student marks dictionary   
# Task: Store three students and their marks in a dictionary,
#  then update one student’s marks and print all key-value pairs.

a={
    "Aman":94,
    "Rahut":89,
    "Harry":87
}
nm,mr=input("enter student name and marks: ").split()
mr=int(mr)
a.update({nm:mr})
print(a.items())