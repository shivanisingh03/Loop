# 12. Write a program to find the product of the digits of a number accepted from the user.

n=int(input("enter the number "))
t=n
sum=1
while t!=0:
    r=t%10
    sum=sum*r
    t=t//10
print(sum)


