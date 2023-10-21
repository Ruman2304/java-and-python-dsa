import random
while True:
 dice=input("roll the dice y/n = ")

 if dice=="y" :
    ran=random.randint(1,6)
    if ran==1:
      print("|   |")
      print("| 0 |")
      print("|   |")
    elif ran==2:
     print("|0  |")
     print("|   |")
     print("|  0|")
    elif ran==3:
      print("|0  |")
      print("| 0 |")
      print("|  0|")
    elif ran==4:
      print("|0 0|")
      print("|   |")
      print("|0 0|")
    elif ran==5:
      print("|0 0|")
      print("| 0 |")
      print("|0 0|")
    else :
      print("|0 0|")
      print("|0 0|")
      print("|0 0|")
 else:
  break