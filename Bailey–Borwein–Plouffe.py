import decimal
import math
import time

print ('Please input the number of decimal spaces')
dec = int(input())

decimal.getcontext().prec = dec

pi = decimal.Decimal(0)
oldpi = decimal.Decimal(3)

k = int(0)

with open ('PI_logs/' + time.strftime("%Y%m%d-%H%M") + '.txt','w+') as text_file:
    print('Method: Bailey-Borwein-Plouffe', file=text_file)
    print('decimal Spaces: ', dec, file=text_file)
    print('start time: ', time.strftime("%Y%m%d-%H%M%S" ), file=text_file)
    while pi != oldpi:
        
        oldpi = pi

        pi += decimal.Decimal(1/(16**k))*decimal.Decimal(decimal.Decimal(120*k**2+151*k+47)/decimal.Decimal(512*k**4+1024*k**3+712*k**2+194*k+15))

        k += 1

    print('end time: ', time.strftime("%Y%m%d-%H%M%S"), file=text_file)
    print('interactions: ', (k), file=text_file)
    print('pi: ', (pi), file=text_file)

print(DONE)
