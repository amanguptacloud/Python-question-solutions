# Rock, paper scissor game.

"""
1=rock
2=ppr
3=scissor"""

import random
computer= random.choice([1,2,3])

yourstr=input("enter your choice(r,p,s):")
yourstr=yourstr.lower()
yourstr=yourstr.strip()
if yourstr not in ['r','p','s']:
    print("wrong input,try again")
    exit()
yours = {'r':1, 'p':2, 's':3}
reverse={1:'rock',2:'paper',3:'scissor'}

you=yours[yourstr]
print(f"you={reverse[you]},computer:{reverse[computer]}")

if computer==you:
    print("draw")
else:
    if computer == 1 and you==2:
        print("you won!")
    elif computer==1 and you==3:
        print("you lose!")
    elif computer==2 and you == 1:
        print("you lose!")
    elif computer==2 and you==3:
        print("you win!")
    elif computer==3 and you==1:
        print("you won!")
    elif computer==3 and you==2:
        print("you lose!")