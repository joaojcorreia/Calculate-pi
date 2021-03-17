import decimal
import time

print ('Please input the number of decimal spaces')
dec = int(input())

decimal.getcontext().prec = dec

pi = decimal.Decimal(4)
oldpi = decimal.Decimal(0)
i = 1
k = 3

with open ('PI_logs/' + time.strftime("%Y%m%d-%H%M") + '.txt','w+') as text_file:
    print('Method: Gregory-Leibniz', file=text_file)
    print('decimal Spaces: ', dec, file=text_file)
    print('start time: ', time.strftime("%Y%m%d-%H%M%S" ), file=text_file)
    while pi != oldpi:
        
        oldpi = pi
        
        pi += -decimal.Decimal(4/k) + decimal.Decimal(4/(k+2))

        i += 1 
        k += 4
    
    print('end time: ', time.strftime("%Y%m%d-%H%M%S"), file=text_file)
    print('interactions: ', (i), file=text_file)
    print('pi: ', (pi), file=text_file)

print(DONE)


