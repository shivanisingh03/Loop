# 13. Write a proram to reverse the number accepted by the user.




number=int(input("enter your number "))
reverse=0
while number>0:
    reverse=(reverse*10+number%10)
    number=number//10
print("reverse",reverse)
