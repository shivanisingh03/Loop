n=int(input("enter no."))
i=1
sum=0
while i<=n//2:
    if n%i==0:
        sum+=i
    i+=1
if sum==n:
    print("perfect")
else:
    print("not perfect")







