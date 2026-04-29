# Rock, Paper, Scissors — Learn Python with a simple-but-fun game that everybody knows.
import random
options=["rock","paper","secisors"]
person1=random.choice(options)
person2=random.choice(options)

print("person 1: ",person1)
print("person 2: ",person2)

if person1==person2:
    print(" play again ! rock paper secisor")
else:

    if person1 =="rock" and person2 =="paper":
        print("person 2  won he have paper")
    
    elif person1 =="rock" and person2 =="secisors":
        print("person 1 win he have rock")
    
    elif person1 == "secisors" and person2=="paper":
        print("person 1 win he have secisors")
    
    elif person1 == "secisors" and person2=="rock":
        print("person 2 win he have rock")
    
    elif person1 == "paper" and person2=="secisors":
        print("person 2 win he have secisors")
    
    elif person1== "paper" and person2=="rock":
        print("person 1 win he have paper")

