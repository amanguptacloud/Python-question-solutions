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