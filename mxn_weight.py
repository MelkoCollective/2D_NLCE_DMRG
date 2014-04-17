############### Cluster Weight Calculations #############
## ex. w[0404] = p0404 - 4*w[0403] - 4*w[0303] - 6*w[0402] - 12*w[0302] - 9*w[0202] 

import numpy
import mxn_cornerentropy # builds corner entropy formulas ( ie. P0404 = # )

def weight(m,n,d,w):

    w_mxn_name = '%02d%02d'%(m,n)

    # First term in weight of mxn is property of mxn
    w[w_mxn_name] = mxn_cornerentropy.cornerentropy(m,n,d)

    wformula = "W%02d%02d=P%02d%02d"%(m,n,m,n)

    for y in range (2,n+1):
        for x in range (y,m+1):
            if y < n or x < m:
                
                if x > n: coeff = (m-x+1)*(n-y+1)  # drop last term otherwise get negative coeff
                else: coeff = (m-x+1)*(n-y+1)+(m-y+1)*(n-x+1)
                
                if x==y: coeff = coeff/2   # different coefficents for squares

                wformula += "%+d*W%02d%02d"%(-coeff,x,y)

                w[w_mxn_name] -= coeff * w['%02d%02d'%(x,y)]

    print wformula

    return w
