#rock=1 paper=2 scissor=3
import random
print("   ROCK PAPER SCISSOR    ")
print("rock=1 \npaper=2\nscissor=3")
a=int(input("enter your choice="))
b=random.randint(1,3)

#choice selection
def choice(b):
    if b==1:
     return "rock"
    elif b==2:
     return "paper"
    else:
     return "scissor"
pc=choice(a)
cc=choice(b)
print("your choice=",pc)
print("compueter's choice=",cc)

#game fuctioning
if a==b:
  print("DRAW!")
elif a==1:
  if a==1 and b==3:
    print("You Win")
  else:
    print("You Loose")
elif a==2:
  if a==2 and b==1:
    print("You Win")
  else:
    print("You Loose")
elif a==3:
  if a==3 and b==2:
    print("You Win")
  else:
    print("You Loose")
  