#!/usr/bin/env python
import numpy
import mxn_getdata
import mxn_weight
from frange import *
from mxn_order import *

#############################
# User settings

order_min = 2
order_max = 5
order_step = 1
order = Arithmetic()

#############################

total = None
w = {} # weights
d={} # data
required = [] # The list of required data files
missing = [] # The list of missing data files

clusters = []

for I in frange(order_min,order_max+0.01,order_step):
    for m,n in order.clusters(I):

        d,alphas,newrequired,newmissing = mxn_getdata.getdata(m,n,d) # read and check for missing data
        required.extend(newrequired)
        missing.extend(newmissing)

        if len(missing) == 0:
            w = mxn_weight.weight(m,n,d,w) # performs cluster weight calculations

            #Embedding factor (1 for squares, 2 for rectangles):
            Lc = 1
            if m != n: Lc = 2

            # cannot use total += w['%02d%02d'%(m,n)] or else W0202 somehow gets changed every iteration
            if total is None:
                total = Lc*w['%02d%02d'%(m,n)]
            else:
                total = total + Lc*w['%02d%02d'%(m,n)]

    # Save result to file
    filename = "Results_" + order.lengthstr(I)
    print "Writing file ",filename
    f = open(filename, 'w')
    for i in range(len(alphas)):
        f.write("%.20f %.20f\n" % (alphas[i],total[i]))
    f.close()

# Show all required data files
#print "The following data files are required:"
#for r in required:
#    print "  ",r 

# If any missing data
if len(missing) > 0:
    print "The following data files were not found:"
    for m in missing:
        print "  ",m 
