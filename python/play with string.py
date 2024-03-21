def string1(e):
    if len(e)>10:
            S=e[0]
            O=e[-1]
            I=str(len(e)-2)
            E=S+I
            E+=O
            
    else:
            E=e
            
    return E

a=int(input())
for i in range(a):
    print(string1(input()))
    
    