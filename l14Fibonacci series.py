# 15. Write a program to print the Fibonacci series till n terms (Accept n from user)


n=int(input("enter the number "))
a=0
b=1
sum=0
count=1
while count<=n:
    print(sum,end=" ")
    count+=1
    a=b
    b=sum
    sum=a+b 


