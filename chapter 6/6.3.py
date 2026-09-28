# 3. Spam detector   
# Task: Given a comment, detect whether it contains any of the handbook’s spam phrases
# and print “Spam” or “Not spam”.

a=['click this','click here','on link']
b=input("enter comment: ")
if a[0] in b:
    print("spam")
elif a[1] in b:
    print("spam")
elif a[2] in b:
    print("spam")
else:
    print("not a spam")

