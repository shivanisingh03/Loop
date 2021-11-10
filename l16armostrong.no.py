# 17. Write a program to check whether a number is Armstrong or not. (Armstrong number is a number that 
# is equal to the sum of cubes of its digits, for example : 153 = 1^3 + 5^3 + 3^3.)

number=int(input("enter your number "))
sum=0
temp=number
while temp>0:
    r=temp%10
    sum=sum+r**3
    temp=temp//10
if sum==number:
    print("Armstrong number ")
else:
    print("Not Armstrong number ")
