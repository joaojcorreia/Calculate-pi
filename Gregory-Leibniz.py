import decimal

decimal.getcontext().prec = 200
pi = decimal.Decimal(4)
oldpi = decimal.Decimal(0)
i = 1
k = 3

while pi != oldpi:
    
    oldpi = pi
    
    pi += -decimal.Decimal(4/k) + decimal.Decimal(4/(k+2))

    i += 1 
    k += 4
 
    print(decimal.Decimal(pi))

print(pi)


