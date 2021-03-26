import decimal
import time

print ('Please input the number of decimal spaces')
dec = int(input())

decimal.getcontext().prec = dec

root = decimal.Decimal(100.024996876)
oldroot = decimal.Decimal(0)

while root != oldroot:
    
    oldroot = root

    root = decimal.Decimal(decimal.Decimal(0.5)*decimal.Decimal(root+decimal.Decimal(10005/root)))


C = decimal.Decimal(426880*root)

L = decimal.Decimal(13591409)
X = decimal.Decimal(1)
M = decimal.Decimal(1)

u=decimal.Decimal(decimal.Decimal(M*L)/X)
oldu = decimal.Decimal(3)

pi = decimal.Decimal(3)

q = int(0)

with open ('PI_logs/' + time.strftime("%Y%m%d-%H%M") + '.txt','w+') as text_file:
    print('Method: Chudnovsky', file=text_file)
    print('decimal Spaces: ', dec, file=text_file)
    print('start time: ', time.strftime("%Y%m%d-%H%M%S" ), file=text_file)
    while u != oldu:
        
        oldu = u

        L = decimal.Decimal(L+545140134)
        X = decimal.Decimal(-262537412640768000*X) 
        M = decimal.Decimal(M*decimal.Decimal(decimal.Decimal((12*q+2)*(12*q+6)*(12*q+10))/decimal.Decimal((q+1)**3)))

        u += decimal.Decimal(decimal.Decimal(M*L)/X)
        
        q += 1



    pi = decimal.Decimal(C/u)

    print('end time: ', time.strftime("%Y%m%d-%H%M%S"), file=text_file)
    print('interactions: ', (q), file=text_file)
    print('pi: ', (pi), file=text_file)

    print('DONE')
