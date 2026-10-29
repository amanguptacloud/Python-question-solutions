# 3. Word censor   
# Task: Read a text file, replace every occurrence of “Donkey” with “#####”,
# and write the updated content back to the same file.

with open("chapter 9/file.txt")as f:
    content=f.read()
content=content.replace('Donkey','#####')
with open("chapter 9/file.txt","w")as f:
    f.write(content)