print("entre two number to calculate hcf ")
number_first=int(input("enetr your first number "))
number_second=int(input("enetr your second number "))
while number_first%number_second!=0:
    remainder=number_first%number_second
    number_first=number_second
    number_second=remainder
print("HCF IS " ,number_second )
