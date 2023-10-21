import random
count=0

for i in range(1,10):
    
    no=int(input("enter the no you want between 1 to 5 = "))
    guess=random.randint(1,5)
    if(no==guess): 
       count+=1 
       print(guess)
       print("points are==",count)
    else:

      count-=1
      print(guess)
      print("points are==",count)
    
    
