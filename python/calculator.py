
print("1 for addition")
print("2 for subtraction")
print("3 for division")
print("4 for multiplication")

def add(a,b):
  return  a+b
def sub(a,b):
   return a-b
def multi(a,b):
      return  a*b
def div(a,b):
    return a/b

while True:
     no1= int(input("enter no 1= "))
     no2=int(input("enter no 2 = "))
     choice=input("enter choice(1,2,3,4) = ")

     if choice=='1':
         print("addition = ",add(no1,no2))
     elif choice=='2':
         print("subtration",sub(no1,no2))
     elif choice=='3':
         print("multiplication", multi(no1,no2))
     elif choice=="4":
         print("division",div(no1,no2))
     else:
         print("pls else valide exoression")
         

     cont=input("continue ? ")
     if cont=="no":
         break
     else:
         print("enter valid arg")
         
         
      
             



        

    
       
     




