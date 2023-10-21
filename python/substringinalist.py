s = "dfa12321afd"

s=list(s)
l3=[]
for i in range(len(s)):
            if s[i].isnumeric():
                l3.append(int(s[i]))
                print(l3)
                l4=set(l3)
                l4.remove(max(l4))
            
print(max(l4))
           
         
            