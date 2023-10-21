num="34567"

  
l3=[int(x) for x in str(num)]
l4=[]
max1=""
for i in l3:
    if i % 2 !=0:
        l4.append(i)
        m=max(l4)
        string=str(m)

    else:
        print("")
print(string)
