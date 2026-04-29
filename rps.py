# Rock, Paper, Scissors — Learn Python with a simple-but-fun game that everybody knows.
import random
options=["rock","paper","secisors"]
person1=random.choice(options)
person2=random.choice(options)

print("person 1: ",person1)
print("person 2: ",person2)

if person1==person2:
    print("stone paper secisor")
elif person1 =="rock" and person2 =="paper":
    print("paper won")
elif person1 =="rock" and person2 =="secisors":
    print("rock win")
elif person1 == "scisor" and person2=="paper":
    print("scisor won")
else:
    print("next chance:")