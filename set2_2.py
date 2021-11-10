# Question 2
# Ek program banao jo 1 se 100 tak ke numbers ke saath yeh kare: 1. Jo 3 se divisible hain unki jagah "Nav" print kare 2. 
# Jo 7 se divisible hain unki jagah "Gurukul" print kare 3. Jo 3 aur 7 dono se divisible hain, unki jagah "NavGurukul" print 
# karein 4. Jo upar wale teen cases mein nahi aate, unki jagah sirf number print karvao.

a=1
while a<=100:
    if a%3==0:
        print(a,"NAV")
    if a%7==0:
        print(a,"GURUKUL")
    if a%3 and a%7:
        print(a,"NAVGURUKUL")
    a=a+1



