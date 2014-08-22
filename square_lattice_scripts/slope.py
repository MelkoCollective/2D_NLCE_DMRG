#!/usr/bin/env python
#Calculates the slope fits of the data as a function of alpha; uses the arithmetic ordering scheme
import numpy as np
from numpy import matrix,linalg,mean
from math import log,sqrt
import sys
import argparse


##------------------------

lmin = 2.5
lmax = 3.5

##------------------------


#
# Function definitions
#

# least-squares algorithm for linear fitting
# given x and y data, returns tuple of slope m, intercept b, and root-mean-square error
def linfit(x_list,y_list):
    Y = matrix([[y_] for y_ in y_list])
    X = matrix([[x_,1] for x_ in x_list])

    (Q,R) = linalg.qr(X)

    (m,b) = [float(item) for item in linalg.solve(R,Q.transpose()*Y)]

    rms_err = sqrt(mean([float(item)**2 for item in Y-X*matrix([[m],[b]])]))

    return (m,b,rms_err)

def frange(start, end, step):
    x = start
    while x < end:
        yield x
        x += step

#
# Argument parsing
#


parser=argparse.ArgumentParser()
parser.add_argument('alpha_out',nargs='*',type=float,help='Alphas that we want as output files')

args=parser.parse_args()

alpha_out=args.alpha_out
print alpha_out

#
# Main program
#


# lfloat and lstring are lists of all the arithmetic orders
# from lmin to lmax as a float or a string, respectively
lfloat=[]
lstring=[]
logl = []
for l in frange(lmin,lmax+0.001,0.5):
    lfloat.append(l)
    lstring.append(str(l))
    logl.append(log(l))

print "Fitting orders: ",lstring

# build list of Renyi indices alpha from the first Results_ file
fname = "Results_"+lstring[0]
f = open(fname, 'r')
alphas = []
for lines in f:
    line = lines.split()
    alphas.append(float(line[0]))
f.close()

# build a dictionary res: l -> c 
# the keys l are the nlce orders
# the values c are lists of the corner term data as a function of Renyi index alpha
res = {}
for i,l in enumerate(lfloat):
    fname = "Results_"+lstring[i]
    print "Reading in file: ",fname
    f = open(fname, 'r')
    corners = []
    for lines in f:
        line = lines.split()
        corners.append(float(line[1]))
    f.close()
    res[l] = corners

slopes = []
errors=[]

for i,a in enumerate(alphas):
    corners = []
    for l in lfloat:
        corners.append(res[l][i])
    m,b,err = linfit(logl,corners)
    slopes.append(m)
    errors.append(err)
    if a in alpha_out:
        print a
        a = str(a)
        print "Writing file: data_"+a
        f = open("data_"+a,'w')
        for j,l in enumerate(lfloat):
            f.write("%.20f %.20f\n"%(logl[j],corners[j]))
        f.close()
        print "Writing file: line_"+a
        print "alpha=%s, m=%f, b=%f"%(a,m,b)
        f = open("line_"+a,'w')
        for j,l in enumerate(lfloat):
            c=m*logl[j]+b
            f.write("%.20f %.20f\n"%(logl[j],c))
        f.close()

fname="slope_%.1f"%(lmin)
print "Writing file: ",fname
f = open(fname,'w')
for a,m,err in zip(alphas,slopes,errors):
    f.write("%.20f %.20f %.20f\n"%(a,-m,err))
f.close()
