# 20. Write a program to check whether a string value is palindrome or not.




str=input("enter the string value ")
rev=""
i=len(str)
while i>0:
    rev+=str[i-1]
    i=i-1
# print(rev)
if rev==str:
    print("The number is palindrome!")
else:
    print("Not a palindrome!")
