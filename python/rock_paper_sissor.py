
import random

while True:
    print("rock,paper,sissor")
    choic=input("enter choice = ")
    module=["rock","paper","sissor"]
    action=random.choice(module)
    print(action)

    if choic==action:
        print("draw")
    elif (choic=="sissor"and action=="rock"):
        print("Sissors are broken Y0U LOST")

    elif(choic=="paper"and action=="sissor"):
        print("paper is cutted YOU LOST")
    elif(choic=="rock"and action=="paper"):
        print("rock is rolled YOU LOST")
    else:
        print("victory!!!!!!")

    stop=input("want to continue? (yes/no)")

    if(stop=="no"):
            break
    else:
            print("enter your choice")

   

     

