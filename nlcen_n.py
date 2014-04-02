import numpy
import getdatafile    # read data
import weightfile     # performs cluster weight calculations

maxn = 6     # square lattice nxn

total = None
for n in range(2,maxn+1):
    d, alphas = getdatafile.getdata(n)
    w_n = weightfile.weight(n,d)

    if total is None: total = w_n
    else: total += w_n

    f = open("Weights_%02dx%02d" % (n,n), 'w')
    for i in range(len(alphas)):
        f.write("%.20f %.20f\n" % (alphas[i],w_n[i]))
    f.close()

    # Save result to file
    f = open("Results_%02dx%02d" % (n,n), 'w')
    for i in range(len(alphas)):
        f.write("%.20f %.20f\n" % (alphas[i],total[i]))
    f.close()
