import decimal
import math
import time


decimal.getcontext().prec = 7000
A = decimal.Decimal((212175710912*(math.sqrt(61)))+1657145277365)
B = decimal.Decimal((13773980896272*(math.sqrt(61)))+107578229802750)
C = decimal.Decimal((5280*((30303*(math.sqrt(61)))+236674))**3)

d = decimal.Decimal(0)
e = decimal.Decimal(math.sqrt(C))

oldpi = decimal.Decimal(0)
pi = decimal.Decimal(3)

n = int(0)

with open ('PI_logs/' + time.strftime("%Y%m%d-%H%M") + '.txt','w+') as text_file:
    print('Method: Ramanujan-Sato', file=text_file)
    print('decimal Spaces: ', dec, file=text_file)
    print('start time: ', time.strftime("%Y%m%d-%H%M%S" ), file=text_file)
    while pi != oldpi:
        
        oldpi = pi
        
        d += (((-1)**n)*math.factorial(6*n)*(A+n*B))/((math.factorial(n)**3)*math.factorial(3*n)*(C**n)*e)

        n += 1

        pi = 1/(12*d)

    print('end time: ', time.strftime("%Y%m%d-%H%M%S"), file=text_file)
    print('interactions: ', (n-1), file=text_file)
    print('pi: ', (pi), file=text_file)
        

print(DONE)
