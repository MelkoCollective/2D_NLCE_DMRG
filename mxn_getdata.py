############### To read the data files ##################
# Cmn_xy, Lmn_1x, Lmn_1y, Lmn_1 (squares)

import numpy
import mxn_checkdata
import mxn_extractdata

def getdata(m,n,d):

    alphas = []
    required = []  # The list of required data files
    missing = [] # The list of missing data files

    # C's
    for y in range (1,n):
        for x in range (y, m):
            fname = "C%02d%02d_%02d%02d"%(m,n,x,y)
            required.append(fname)
            if mxn_checkdata.checkdata(fname):
                d[fname], alphas = mxn_extractdata.extract(fname, alphas)
            else:
                missing.append(fname)
            
    if m != n: # Extra terms on rectangles
        for x in range (1, m):
            for y in range (x+1,n):
                fname = "C%02d%02d_%02d%02d"%(m,n,x,y)
                required.append(fname)
                if mxn_checkdata.checkdata(fname):
                    d[fname], alphas = mxn_extractdata.extract(fname, alphas)
                else:
                    missing.append(fname)
                
    # L's
    if m == n:
        for j in range (1,int(n/2)+1): # squares
            keyname = "L%02d%02d_%02d"%(m,n,j)
            required.append(keyname)

            fname = keyname
            if mxn_checkdata.checkdata(fname):
                d[keyname], alphas = mxn_extractdata.extract(fname, alphas)
            else:
                fname = "L%02d%02d_%02dX"%(m,n,j)
                if mxn_checkdata.checkdata(fname):
                    d[keyname], alphas = mxn_extractdata.extract(fname, alphas)
                else:
                    fname = "L%02d%02d_%02dY"%(m,n,j)
                    if mxn_checkdata.checkdata(fname):
                        d[keyname], alphas = mxn_extractdata.extract(fname, alphas)
                    else:
                        missing.append(fname)
    else:
        for jx in range (1,int(n/2)+1): # rectangle - horizontal line cuts
            fname = "L%02d%02d_%02dX"%(m,n,jx)
            required.append(fname)
            if mxn_checkdata.checkdata(fname):
                d[fname], alphas = mxn_extractdata.extract(fname, alphas)
            else:
                missing.append(fname)
        
        for jy in range (1,int(m/2)+1): # rectangle - vertical line cuts
            fname = "L%02d%02d_%02dY"%(m,n,jy)
            required.append(fname)
            if mxn_checkdata.checkdata(fname):
                d[fname], alphas = mxn_extractdata.extract(fname, alphas)
            else:
                missing.append(fname)
        
    return d, alphas, required, missing
