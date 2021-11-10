# method 3

n=int(input("enter the number "))
for i in range(14):
    k=ord("A")+i
    for j in range(i+1):
        print(chr(k),end="")
        k+=1
    print()