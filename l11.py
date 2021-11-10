# 11. Write a program to find the sum of the digits of a number accepted from the user.

n=int(input("enter your digit "))
t=0
while n>0:
    d=n%10
    t=t+d
    n=n//10
print(t)