# 26. Write a program to print the following series till n terms.
# 2 , 22 , 222 , 2222 _ _ _ _ _ n terms



n=int(input("enter you n number "))
a=2
c=1
while c<=n:
    print(a,end=" ")
    a=a*10+2
    c+=1





