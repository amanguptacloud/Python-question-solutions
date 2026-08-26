# 2. Double-space detector and fixer  [Required]
# Task: Take a sentence, detect whether it contains double spaces,
#  then create a corrected version with single spaces.

a=input("give input: ")
if "  " in a:
    print("double space found")
else:
    print("double space not found")
a=a.replace("  "," ")
print(a)

# second method
b=input("give input: ")
if "  " in b:
    print("double space found")
else:
    print("double space not found")
b=b.replace("  "," ")
print(b)