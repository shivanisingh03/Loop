# 19. Write a program to add first n terms of the following series using a while loop :
# 1/1! + 1/2! + 1/3! + …….. + 1/n!


n=1
num=(1/n)
sum=0
while n<=20:
    print(num)
    sum+=num
    n+=1
print(sum)



