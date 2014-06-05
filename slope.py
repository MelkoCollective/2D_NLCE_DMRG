import numpy as np
from numpy import matrix,linalg,mean
from math import log,sqrt
import sys

lmax = 6
lmin = 4
lstep = 0.5

orders = []
ll = lmin
while abs(ll-lmax) > 1E-6:
   orders.append(ll)
   ll += lstep

print orders

results_template = "Results_%.1f"

def linfit(x_list,y_list): #includes linear fitting as a special case
    Y = matrix([[y_] for y_ in y_list])
    X = matrix([[x_,1] for x_ in x_list])

    (Q,R) = linalg.qr(X)

    (m,b) = [float(item) for item in linalg.solve(R,Q.transpose()*Y)]

    rms_err = sqrt(mean([float(item)**2 for item in Y-X*matrix([[m],[b]])]))

    return (m,b,rms_err)


fname = results_template%(lmin,)
f = open(fname, 'r')
alphas = []
for lines in f:
    line = lines.split()
    alphas.append(float(line[0]))
f.close()

res = {}

for l in orders:
    fname = results_template%(l,)
    print fname
    f = open(fname, 'r')
    corners = []
    for lines in f:
        line = lines.split()
        corners.append(float(line[1]))
    f.close()
    res[l] = corners

slopes = []

logl = []
for l in orders:
    logl.append(log(l))

for i,a in enumerate(alphas):
    corners = []
    for l in orders:
        corners.append(res[l][i])
    m,b,err = linfit(logl,corners)
    slopes.append(m)

f = open("slopes",'w')
for a,m in zip(alphas,slopes):
    f.write("%.20f %.20f\n"%(a,-m))
f.close()
