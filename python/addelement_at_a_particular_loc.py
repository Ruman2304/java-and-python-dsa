s = "codeleet"
s=list(s)
print(s)
indices = [4,5,6,7,0,2,1,3]

l3=[]
for i in indices:
    print(i)
    for j in range(len(s)):
        l3.insert(i,s[j])
k=str(l3)
print(k)
       
