import math
import random

for i in range(3,33, 5):
    print(i)
print("new loooooooooop")

for l in range(100,50,-2):
    print(l)
print("While looooop")

j = int(1)
while j != 0 :
        j = (int(input( "give me a number. Type 0 to quit")))
        print(j*2)
print("Medium----------------------------------------------------------------------------")


num = 0
choice = 'a'
def monstergen():
    mob = random.randrange(1,100)
print("Lets go monster hunting")

if num<10:
    print("Omg is a random witch")
elif num<20:
     print("A zombie has spawned in to eat you ")
elif num < 30:
     print("Skalatron is coming for you")
elif num < 40:
     print("Spiader")
     choice = 'a'
while choice != 'q':
    print((input("Press random number and press q to quit")))
    

    
