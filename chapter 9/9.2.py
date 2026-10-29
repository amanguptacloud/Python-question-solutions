# 2. High-score updater   
# Task: Write a program where game() returns a score.
# Read hi-score.txt and replace the stored score only when the new score is higher.

import random

def game():
    score=random.randint(1,69)
    return score

score=game()

with open("chapter 9/hi-score.txt")as f:
    oldsc=f.read()
if oldsc=="":
    print("Your new high score is:",score)
    score=str(score)
    with open("chapter 9/hi-score.txt","w")as f:
        f.write(score)
        exit()
oldsc=int(oldsc)
if oldsc>=score:
    print("your score is:",score)
elif oldsc<score:
    print("New high score is:",score)
    score=str(score)
    with open("chapter 9/hi-score.txt","w")as f:
        f.write(score)