#!/usr/bin/env python
#Calculates the slope fits of the data as a function of alpha; uses the arithmetic ordering scheme
import numpy as np
from numpy import matrix,linalg,mean
from math import log,sqrt,exp
import sys
import argparse


##------------------------

lmin = 3.0
lmax = 7.0
lstep = 1.0

#fit_type = 'linear'
#fit_type = 'subleading'
fit_type = 'subleading2'
fit_type = 'subleading3'

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

def subleading_fit(x_list,y_list):
    Y = matrix([[y_] for y_ in y_list])
    X = matrix([[x_,1,exp(-x_)] for x_ in x_list])

    (Q,R) = linalg.qr(X)

    (a,b,c) = [float(item) for item in linalg.solve(R,Q.transpose()*Y)]

    rms_err = sqrt(mean([float(item)**2 for item in Y-X*matrix([[a],[b],[c]])]))

    return (a,b,c,rms_err)

def subleading2_fit(x_list,y_list):
    Y = matrix([[y_] for y_ in y_list])
    X = matrix([[x_,1,exp(-x_),exp(-2*x_)] for x_ in x_list])

    (Q,R) = linalg.qr(X)

    (a,b,c,d) = [float(item) for item in linalg.solve(R,Q.transpose()*Y)]

    rms_err = sqrt(mean([float(item)**2 for item in Y-X*matrix([[a],[b],[c],[d]])]))

    return (a,b,c,d,rms_err)

def subleading3_fit(x_list,y_list):
    Y = matrix([[y_] for y_ in y_list])
    X = matrix([[x_,1,exp(-x_),exp(-2*x_),exp(-3*x_)] for x_ in x_list])

    (Q,R) = linalg.qr(X)

    (a,b,c,d,f) = [float(item) for item in linalg.solve(R,Q.transpose()*Y)]

    rms_err = sqrt(mean([float(item)**2 for item in Y-X*matrix([[a],[b],[c],[d],[f]])]))

    return (a,b,c,d,f,rms_err)

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
for l in frange(lmin,lmax+0.001,lstep):
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

if fit_type=='linear': 
    print "Doing linear fit"
elif fit_type=='subleading': 
    print "Doing subleading 1/L fit"
elif fit_type=='subleading2': 
    print "Doing subleading2 1/L, 1/L^2 fit"
elif fit_type=='subleading3': 
    print "Doing subleading3 1/L, 1/L^2, 1/L^3 fit"

for i,a in enumerate(alphas):
    corners = []
    for l in lfloat:
        corners.append(res[l][i])
    m = None; b = None; c = None; err = None

    if fit_type=='linear': 
        m,b,err = linfit(logl,corners)
    elif fit_type=='subleading': 
        m,b,c,err = subleading_fit(logl,corners)
    elif fit_type=='subleading2': 
        m,b,c,d,err = subleading2_fit(logl,corners)
    elif fit_type=='subleading3': 
        m,b,c,d,f,err = subleading3_fit(logl,corners)
    else: raise Exception("Fit type {} not recognized".format(fit_type))

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
        print "alpha={}, m={}, b={}, c={}".format(a,m,b,c)
        f = open("line_"+a,'w')
        for j,l in enumerate(lfloat):
            c=m*logl[j]+b
            f.write("%.20f %.20f\n"%(logl[j],c))
        f.close()

fname="slope_%.1f_%.1f"%(lmin,lmax)
print "Writing file: ",fname
f = open(fname,'w')
for a,m,err in zip(alphas,slopes,errors):
    f.write("%.20f %.20f %.20f\n"%(a,-m,err))
f.close()
