start=1
stop=2
n=stop
for row in range(2,6):
    for col in range(start,stop):
        n-=1
        print(n,end="")
    print()
    start=stop
    stop+=row
    n=stop