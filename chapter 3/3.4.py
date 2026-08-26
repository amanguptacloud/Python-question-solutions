# 4. Text analyzer  [Stretch]
# Task: Given a sentence, report its length, number of spaces,
#       number of occurrences of the letter “a”,
#       and the position of the first “python” occurrence if present.

sent=input("give sentence: ")
print("length of sentence: ",len(sent))

print("number of spaces: ",sent.count(" "))

print("number of a: ",sent.count("a"))

a=(sent.find("python"))

if a==-1:
    print("Python not found")
else:
    print("Position of first occurence of python: ",a)