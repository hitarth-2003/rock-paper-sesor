# Rock, Paper, Scissors — Learn Python with a simple-but-fun game that everybody knows.
import random
options=["rock","paper","secisors"]
person1=random.choice(options)
person2=random.choice(options)

print("person 1: ",person1)
print("person 2: ",person2)

if person1==person2:
    print("stone paper secisor")
else:
    print("next chance:")