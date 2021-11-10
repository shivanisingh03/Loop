# 1. Write a program to print the following using while loop 
# a. First 10 Even numbers
# b. First 10 Odd numbers
# c. First 10 Natural numbers
# d. First 10 Whole numbers


i=1
while i<=10:
    if i%2==0:
        print("even",i)
    if i%2!=0:
        print("odd",i)
    print("Whole numbers",i)
    print("Natural numbers",i)
    i+=1

    