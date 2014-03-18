############### Corner Entropy Formulas ##################

import numpy

def cornerentropy(m,d):

    #print "m = ",m
    
    pmm = 0
    x = 1
    y = 1       
        
    if m==1: return 0     # p0101 = 0
    
    # The contribution from the C's
    while x < m:       # loops from C0404_0101, C0404_0102, ... , C0404_0303
        dname = "C%02d%02d_%02d%02d"%(m,m,x,y)

        # set coefficients
        if x==y:
            d[dname] = 2*d[dname]
        else:
            d[dname] = 4*d[dname]

        pmm = pmm + d[dname]

        # to cycle through all data
        if y==m-1 and x==m-1:     #C0404_0303 is the last term required for C0303 data, now move to C0404_0101
            x += 1       # break loop
        elif y==m-1:     # go from C0404_0102 to C0404_0202
            x += 1
            y = x
        else:             # go from C0404_0101 to C0404_0102
            y += 1

    x = 1

    # The contribution from the L's
    while x <= 1./2*m:       # loops from L0404_01 to L0404_02
        dname = "L%02d%02d_%02d"%(m,m,x)

        # set coefficients
        coef = 0
        if x == int(m/2) and m%2==0: coef = (2.*m-2.)
        else:                        coef = (4.*m-4.)

        d[dname] = coef*d[dname]

        #print dname," %.3f"%(coef,)

        pmm = pmm - d[dname]
        x += 1     # cycle through all data

    pmm *= 0.5

    return pmm


## Formulas
##
## 2x2: p22 = 2*C11 -2*L
## 3x3: p33 = 2*( C11 + C22 ) + 4*C12 - 8*L
## 4x4: p44 = 2*( C11 + C22 + C33) + 4*( C12 + C13 + C23 ) - 12*L1 - 6*L2
## 5x5: p55 = 2*( C11 + C22 + C33 + C44)
##              + 4*( C12 + C13 + C14 + C23 + C24 + C34 ) - 16*L1 - 16*L2
## 6x6: p66 = 2*( ... ) + 4*( ... ) - 20*L1 - 20*L2 - 10*L3
## 7x7: p77 = 2*( ... ) + 4*( ... ) - 24*L1 - 24*L2 - 24*L3
## 8x8: p88 = 2*( ... ) + 4*( ... ) - 28*L1 - 28*L2 - 28*L3 - 14*L4
