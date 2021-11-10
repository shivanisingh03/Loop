b=0
for row in range(5,0,-1):
    b+=1
    for col in range(1,row+1):
        print(b,end="")
    print("")
