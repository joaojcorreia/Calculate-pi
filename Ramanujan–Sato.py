import decimal
import math


decimal.getcontext().prec = 7000
A = decimal.Decimal((212175710912*(math.sqrt(61)))+1657145277365)
B = decimal.Decimal((13773980896272*(math.sqrt(61)))+107578229802750)
C = decimal.Decimal((5280*((30303*(math.sqrt(61)))+236674))**3)

d = decimal.Decimal(0)
e = decimal.Decimal(math.sqrt(C))

oldpi = decimal.Decimal(0)
pi = decimal.Decimal(3)

n = int(0)

while pi != oldpi:
    
    oldpi = pi
    
    d += (((-1)**n)*math.factorial(6*n)*(A+n*B))/((math.factorial(n)**3)*math.factorial(3*n)*(C**n)*e)

    n += 1

    pi = 1/(12*d)
    print (pi, n)

print(pi)
