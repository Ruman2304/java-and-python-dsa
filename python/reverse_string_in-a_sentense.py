s = "Let's take LeetCode contest"
l2=s.split(" ")
l3=[]
for i in l2:
    l3.append(i[::-1])
    k=" ".join(l3)
    print(k)

        