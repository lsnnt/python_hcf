def calc_hcf(n1,n2):
    if n1 > n2:
        small = n2
    else:
        small = n1
    for i in range(1,small + 1):
        if((n1 % i == 0) and (n2 % i == 0)):
            result = i
    return result
number1 = int(input("ENTER FIRST NUMBER : "))
number2 = int(input("ENTER SECOND NUMBER : "))
print("THE HCF OF " ,number1, " AND " ,number2, " IS : " ,calc_hcf(number1, number2))