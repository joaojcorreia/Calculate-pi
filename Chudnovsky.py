import decimal
import math


decimal.getcontext().prec = 100000
C = decimal.Decimal(426880*math.sqrt(10005))

u=decimal.Decimal(0)

oldu = decimal.Decimal(3)
pi = decimal.Decimal(3)

q = int(0)


while u != oldu:
    
    oldu = u

    u += decimal.Decimal(((decimal.Decimal(math.factorial(6*q))/(decimal.Decimal(math.factorial(3*q))*decimal.Decimal((math.factorial(q))**3)))*(545140134*q+13591409))/(decimal.Decimal((-262537412640768000)**q)))

    q += 1

    print (q)


pi = C/u

print(pi)
