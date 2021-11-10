# Question 5
# 11 logon ka weight input le aur fir average weight print kare. Aur fir yeh bhi check kare ki kya Average weight 5 ka multiple 
# (Yaani 5 se bhaag karne par shesh 0 bachta hai) hai ya nahi? Note: Isme aapko input ka use karna padega. Aap loop ke andar raw 
# input ka use kar ke 11 baar raw_input le sakte ho.


i=1
sum=0
while i<=11:
    num=int(input("enter your number "))
    sum=sum+num
    # i+=1
# print(sum/11)
    if sum%5==0:
        print("yes")
    else:
        print("not")
    i+=1
print(sum)


















