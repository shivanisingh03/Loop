# 34. Write a program to print only odd numbers from the given list using  a while loop . 
# L = [23, 45, 32, 25, 46, 33, 71, 90]


L = [23, 45, 32, 25, 46, 33, 71, 90]
i=0
while i<=len(L):
    if i%2!=0:
        print(L[i])
    i+=1
