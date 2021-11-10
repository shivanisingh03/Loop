print("enter x for exit ")
print("enter the first and second number for find the lcm, hcf ")
number1=input()
if number1=="x":
    exit()
else:
    number2=input()
    num1=int(number1)
    num2=int(number2)
    tmp1=num1
    tmp2=num2
    while tmp2!=0:
        t=tmp2
        tmp2=tmp1%tmp2
        tmp1=t
    hcf=tmp1
    lcm=(num1*num2)/hcf
    print(hcf)
    print(lcm)