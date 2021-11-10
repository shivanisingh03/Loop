# 9. Write a program to display all even numbers that fall between two numbers (exclusive both numbers)
# entered by the user.


a=int(input("enter the first number "))
b=int(input("enter the second number "))
for i in range(a,b+1):
    if i%2==0:
        print(i,end=" ")