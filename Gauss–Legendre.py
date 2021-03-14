import decimal
import math
import time

print ('Please input the number of decimal spaces')
dec = int(input())

decimal.getcontext().prec = dec

a=decimal.Decimal(1)
olda = decimal.Decimal(1)
b=decimal.Decimal(1/math.sqrt(2))
t=decimal.Decimal(1/4)
p=(1)

pi = decimal.Decimal(3)

q = int(0)

with open ('PI_logs/' + time.strftime("%Y%m%d-%H%M") + '.txt','w+') as text_file:
    print('Gauss-Legendre', file=text_file)
    print('decimal Spaces: ', dec, file=text_file)
    print('start time: ', time.strftime("%Y%m%d-%H%M%S" ), file=text_file)
    while a != b:
        
        olda = a

        a = decimal.Decimal((a+b)/2)
        b = decimal.Decimal(math.sqrt(olda*b))

        t = decimal.Decimal(t-(p*((olda-a)**2)))

        p = p*2

        q += 1



    pi = decimal.Decimal(((a+b)**2)/(4*t))

    print('end time: ', time.strftime("%Y%m%d-%H%M%S"), file=text_file)
    print('interactions: ', (q), file=text_file)
    print('pi: ', (pi), file=text_file)

    print('DONE')
