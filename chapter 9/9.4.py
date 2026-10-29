# 4. Find line number   
# Task: Search a log file for the word “python” and print the line numbers where it appears.

with open("chapter 9/log.txt",)as f:
    content=f.readlines()
lineno=1
py='not'
for i in content:
    i=i.lower()
    if 'python' in i:

        print("Python present on line number:",lineno)
        py='found'
    lineno+=1
if py=='not':
    print("Python not present")