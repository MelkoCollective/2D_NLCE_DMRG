import numpy
import getdatafile    # read data
import weightfile     # performs cluster weight calculations


n = 4     # square lattice nxn


d, alphas = getdatafile.getdata(n)
w_n = weightfile.weight(n,d)


# Save result to file
f = open('Results_nxn', 'w')
for i in range(len(alphas)):
    f.write("%.20f %.20f\n" % (alphas[i],w_n[i]))
f.close()
