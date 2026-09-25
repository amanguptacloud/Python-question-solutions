# 1. Mini dictionary lookup   
# Task: Create a dictionary of 5 Hindi words mapped to English meanings.
#  Ask the user for a word and print its meaning, or a clear “not found” message.

word={
    "billi":"cat",
    "chuha":"mouse",
    "bhai":"brother",
    "behen":"sister"
}

a=input("enter word: ")
if(a not in word):
    print("not found")
else:
    print(word[a])