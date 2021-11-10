name="shivani singh "
s=""
i=0
s1=""
while i<len(name):
    s=s+name[i]
    if name[i]=="":
        break
    i=i+1
j=i
while j<len(name):
    s1=s1+name[j]
    j=j+1
print(s1,s)



