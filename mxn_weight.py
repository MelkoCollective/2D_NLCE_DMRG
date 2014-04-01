############### Cluster Weight Calculations #############
## ex. w[0404] = p0404 - 4*w[0403] - 4*w[0303] - 6*w[0402] - 12*w[0302] - 9*w[0202] 

import numpy
import mxn_cornerentropy # builds corner entropy formulas ( ie. P0404 = # )

def weight(m,n,d,w):

    p = {}
    pname = "p%02d%02d"%(m,n) #p0101, p0202, p0303, ...
    p[pname] = mxn_cornerentropy.cornerentropy(m,n,d)
    w['%02d%02d'%(m,n)] = p[pname]
            
    for y in range (2,n+1):
        for x in range (y,m+1):
            if y < n or x < m:
                
                if x > n: coeff = (m-x+1)*(n-y+1)  # drop last term otherwise get negative coeff
                else: coeff = (m-x+1)*(n-y+1)+(m-y+1)*(n-x+1)
                
                if x==y: coeff = coeff/2   # different coefficents for squares

                w['%02d%02d'%(m,n)] -= coeff * w['%02d%02d'%(x,y)]
    return w
