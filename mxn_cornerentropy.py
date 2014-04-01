############### Corner Entropy Formulas ##################

import numpy

def cornerentropy(m,n,d):

    pmn = 0

    # C's
    for y in range (1,n):
        for x in range (y, m):
            fname = "C%02d%02d_%02d%02d"%(m,n,x,y)
            if m == n and x != y: pmn += 4*d[fname] # square cross terms (ie. C0303_0201)
            else: pmn += 2*d[fname]

    if m != n: # Extra terms on rectangles
        for x in range (1, m):
            for y in range (x+1,n):
                fname = "C%02d%02d_%02d%02d"%(m,n,x,y)
                pmn += 2*d[fname]
                
    # L's
    if m == n:
        for j in range (1,int(n/2)+1): # squares
            fname = "L%02d%02d_%02d"%(m,n,j)
            if j == int(m/2) and m%2 == 0: pmn -= 2*(m-1)*d[fname] # new L terms (ie. p0404 = ... -12*L1 - 6*L2)
            else: pmn -= 4*(m-1)*d[fname]
            
    else:
        for jx in range (1,int(n/2)+1):  # rectangle - horizontal line cuts
            fname = "L%02d%02d_%02dX"%(m,n,jx)
            if jx == int(n/2) and n%2 == 0: pmn -= (m-1)*d[fname]
            else: pmn -= 2*(m-1)*d[fname]
        
        for jy in range (1,int(m/2)+1): # rectangle - horizontal line cuts
            fname = "L%02d%02d_%02dY"%(m,n,jy)
            if jy == int(m/2) and m%2 == 0: pmn -= (n-1)*d[fname]
            else: pmn -= 2*(n-1)*d[fname]

    pmn *= 0.5
    return pmn
