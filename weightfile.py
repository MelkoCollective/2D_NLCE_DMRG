############### Cluster Weight Calculations #############
## ex. w[4] = p0404 - 4*w[3] - 9*w[2] - 16*w[1]

import numpy
import cornerentropyfile   # builds corner entropy formulas

def weight(n,d):

    m = 1
    p = {}
    w = []
    w.append(0)
    w[0] = 0

    while m <= n:
        pname = "p%02d%02d"%(m,m)   #p0101, p0202, p0303, ...
        p[pname] = cornerentropyfile.cornerentropy(m,d)
        w.append(0)
        w[m] = p[pname]
        mprime = m-1
        i = 2
        while mprime > 0:
            w[m] = w[m] - i*i*w[mprime]
            mprime -= 1
            i += 1   
        m += 1

    return w[n]
