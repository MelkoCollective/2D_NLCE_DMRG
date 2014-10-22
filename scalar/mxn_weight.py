############### Cluster Weight Calculations #############
## ex. w[0404] = p0404 - 4*w[0403] - 4*w[0303] - 6*w[0402] - 12*w[0302] - 9*w[0202] 

import numpy

def weight(m,n,d,err,w,werr,min_L=1):

    w_mxn_name = '%02dx%02d'%(m,n)

    # First term in weight of mxn is property of mxn
    w[w_mxn_name] = d[w_mxn_name]
    werr[w_mxn_name] = err[w_mxn_name]

    wformula = "W%02dx%02d=P%02dx%02d"%(m,n,m,n)

    for y in range(min_L,n+1):
        for x in range(y,m+1):
            if (y < n or x < m) and (not (x==1 and y==1)): #want to include cases where x==m or y==n separately, but not x==m and y==n.
                if x > n: coeff = (m-x+1)*(n-y+1)  # drop last term otherwise get negative coeff
                else: coeff = (m-x+1)*(n-y+1)+(m-y+1)*(n-x+1)
                
                if x==y: coeff = coeff/2   # different coefficents for squares

                wformula += "%+d*W%02dx%02d"%(-coeff,x,y)

                w[w_mxn_name] -= coeff * w['%02dx%02d'%(x,y)]
                werr[w_mxn_name] -= coeff * werr['%02dx%02d'%(x,y)]

    print wformula

    return w, werr
