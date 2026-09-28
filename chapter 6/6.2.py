# 2. Grade calculator   
# Task: Take marks and print 
# the grade using the handbook’s grade bands.

a=int(input("enter marks:"))
if a<0 or a>100:
    print('Wrong input.')
    exit()
elif a>=90:
    print("Grade:A")
elif a>=80:
    print("Grade:B")
elif a>=70:
    print("Grade:C")
elif a>=60:
    print("Grade:D")
elif a>=40:
    print("Grade:E")
else:
    print("Fail")