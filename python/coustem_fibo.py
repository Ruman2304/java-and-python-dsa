l=[]
a=int(input("Enter the starting point:"))
b=int(input("enter no of terms"))
def fibonacci(n,a):
    if n < a:
        l.append(1)    
    else:
        sum=0
        for j in range(len(l)-1,len(l)-a-1,-1):
            sum+=l[j]
        l.append(sum)
    return l

for i in range(b):
    print(fibonacci(i,a))
print(l)
        