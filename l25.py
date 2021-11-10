# 35. Write a program to print all the factors of a number using a while loop .


number = int(input("Please Enter any Number: "))

value = 1
print(number)

while value <= number:
    if number % value == 0:
        print(value)
    value = value + 1
