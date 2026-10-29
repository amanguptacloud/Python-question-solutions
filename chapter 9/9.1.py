# 1. Read and search a file   
# Task: Read poems.txt and report whether it contains the word “twinkle”.

with open("chapter 9/poems.txt") as f:
    poem=f.read()

print("poem in file is:\n",poem)
poem=poem.lower()
if 'twinkle' in poem:
    print("\n\n--twinkle is present in poem--")
else:
    print("\n\n--twinkle not present in poem--")