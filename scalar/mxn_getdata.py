############### To read the data files ##################

import numpy
import mxn_checkdata
import mxn_extractdata

def getdata(m,n,d,err,xmin=None,xmax=None):
    xs = []
    required = []  # The list of required data files
    missing = [] # The list of missing data files

    fname = "%02dx%02d"%(m,n)
    required.append(fname)
    if not mxn_checkdata.checkdata(fname): missing.append(fname)
    if len(missing)==0:
        data, xs, derr = mxn_extractdata.extract(fname, xs,xmin=xmin,xmax=xmax)

        if len(data) > 0: 
            d[fname] = data
            if len(derr) == 0: derr = [0 for x in data]
            err[fname] = derr
        else:             
            missing.append(fname)

            
    return d,xs,err,required,missing
