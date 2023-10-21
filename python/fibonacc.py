def fibo(n):
    if n<= 1:
        return n
    else:
        return (fibo(n-1)+fibo(n-2))

no=int (input("enter range = "))
if no<=1:
    print("pls enter positive int")
else:
   for i in range(no):
    print(fibo(i))


    