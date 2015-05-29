#!/usr/bin/env python
import numpy
import mxn_getdata
import mxn_weight
from frange import *
from mxn_order import *

xmin = None
xmax = None

#############################
# User settings

#order_min = 2
#order_max = 4.0
#order_step = 0.5
#order = Arithmetic()

order_min = 2
order_max = 5.0
order_step = 1.0
order = MaxL()

#xmin = 2.00
#xmax = 1.72

#############################

total = None
totalerr = None
w = {} # weights
werr = {} # weights for errorbars
d={} # data
err={} # errorbars
required = [] # The list of required data files
missing = [] # The list of missing data files

clusters = []

for I in frange(order_min,order_max+0.01,order_step):
    for m,n in order.clusters(I,min_L=order_min):
        print "Order %f Cluster %02dx%02d"%(I,m,n)

        d,xs,err,newrequired,newmissing = mxn_getdata.getdata(m,n,d,err,xmin=xmin,xmax=xmax) # read and check for missing data
        required.extend(newrequired)
        missing.extend(newmissing)

        #print "xs = [%.2f,%.2f,...,%.2f]"%(xs[0],xs[1],xs[-1])

        if len(missing) == 0:
            w, werr = mxn_weight.weight(m,n,d,err,w,werr,min_L=order_min) # performs cluster weight calculations

            #Embedding factor (1 for squares, 2 for rectangles):
            Lc = 1
            if m != n: Lc = 2

            print "Contribution Lc*W%02dx%02d=(%d)*(%.5f)=%.5f"%(m,n,Lc,w['%02dx%02d'%(m,n)],Lc*w['%02dx%02d'%(m,n)])

            # cannot use total += w['%02d%02d'%(m,n)] or else W0202 somehow gets changed every iteration
            if total is None:
                total = Lc*w['%02dx%02d'%(m,n)]
                totalerr = Lc*werr['%02dx%02d'%(m,n)]
            else:
                total = total + Lc*w['%02dx%02d'%(m,n)]
                totalerr = totalerr + Lc*werr['%02dx%02d'%(m,n)]

            # Save result to file
            filename = "Results_" + order.lengthstr(I)
            f = open(filename, 'w')
            for i in range(len(xs)):
                f.write("%.20f %.20f %.20f\n" % (xs[i],total[i],totalerr[i]))
            f.close()

# Show all required data files
#print "The following data files are required:"
#for r in required:
#    print "  ",r 

# If any missing data
if len(missing) > 0:
    if xmin or xmax:
        print "The following data files were not found or did not contain data within the range [xmin,xmax]:"
    else:
        print "The following data files were not found:"
    for m in missing:
        print "  ",m 
