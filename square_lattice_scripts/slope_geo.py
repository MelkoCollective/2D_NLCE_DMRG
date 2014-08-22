#!/usr/bin/env python
#Calculates the fits of the data over the range of alpha to produce curve as a function of alpha showing the corner entropy fits; uses geometric order Results files
import numpy as np
from numpy import matrix,linalg,mean
from math import log,sqrt
import sys
import argparse
import math

parser=argparse.ArgumentParser()
parser.add_argument('alpha_out',nargs='*',type=float,help='Alphas that we want as output files')

args=parser.parse_args()

alpha_out=args.alpha_out
print alpha_out

lmax = 24
lmin = 4
coeff=0

lfloat=[]
lstring=[]
for k in range(lmin,lmax+1):
    if all(k % i for i in xrange(2,k)) is False:
        l='%.4f'% math.sqrt(k)
        lfloat.append(float(l))
        lstring.append(str(l))


def linfit(x_list,y_list): #includes linear fitting as a special case
    Y = matrix([[y_] for y_ in y_list])
    X = matrix([[x_,1] for x_ in x_list])

    (Q,R) = linalg.qr(X)

    (m,b) = [float(item) for item in linalg.solve(R,Q.transpose()*Y)]

    rms_err = sqrt(mean([float(item)**2 for item in Y-X*matrix([[m],[b]])]))

    return (m,b,rms_err)


fname = "Results_"+lstring[0]
f = open(fname, 'r')
alphas = []
for lines in f:
    line = lines.split()
    alphas.append(float(line[0]))
f.close()

res = {}

for i,l in enumerate(lfloat):
    try:
        fname = "Results_"+lstring[i]
        print fname
        f = open(fname, 'r')
        corners = []
        for lines in f:
            line = lines.split()
            corners.append(float(line[1]))
        f.close()
        res[l] = corners
    except:
        print "No file for l="+str(l)

slopes = []
errors=[]

logl = []
for l in lfloat:
    logl.append(log(l))

for i,a in enumerate(alphas):
    corners = []
    for l in lfloat:
        try:
            corners.append(res[l][i])
        except:
            print 'No file for l='+str(l)
    m,b,err = linfit(logl,corners)
    slopes.append(m/2)
    errors.append(err)
    if a in alpha_out:
        print a
        a = str(a)
        f = open("geodata_"+a,'w')
        for j,l in enumerate(lfloat):
            f.write("%.20f %.20f\n"%(logl[j],corners[j]))
        f.close()
        f = open("geoline_"+a,'w')
        for j,l in enumerate(lfloat):
            c=m*logl[j]+b
            f.write("%.20f %.20f\n"%(logl[j],c))
        f.close()

#print errors

fname="geoslope_%.1f"%(lmin)
f = open(fname,'w')
for a,m in zip(alphas,slopes):
    f.write("%.20f %.20f\n"%(a,-m))
f.close()
