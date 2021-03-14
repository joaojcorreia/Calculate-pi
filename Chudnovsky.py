import decimal
import math
import time

print ('Please input the number of decimal spaces')
dec = int(input())

decimal.getcontext().prec = dec
C = decimal.Decimal(426880*math.sqrt(10005))

u=decimal.Decimal(0)

oldu = decimal.Decimal(3)
pi = decimal.Decimal(3)

q = int(0)

with open ('PI_logs/' + time.strftime("%Y%m%d-%H%M") + '.txt','w+') as text_file:
    print('Method: Chudnovsky', file=text_file)
    print('decimal Spaces: ', dec, file=text_file)
    print('start time: ', time.strftime("%Y%m%d-%H%M%S" ), file=text_file)
    while u != oldu:
        
        oldu = u

        u += decimal.Decimal(((decimal.Decimal(math.factorial(6*q))/(decimal.Decimal(math.factorial(3*q))*decimal.Decimal((math.factorial(q))**3)))*(545140134*q+13591409))/(decimal.Decimal((-262537412640768000)**q)))

        q += 1



    pi = C/u

    print('end time: ', time.strftime("%Y%m%d-%H%M%S"), file=text_file)
    print('interactions: ', (q), file=text_file)
    print('pi: ', (pi), file=text_file)

    print('DONE')
