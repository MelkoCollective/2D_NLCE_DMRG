import numpy
import mxn_getdata
import mxn_weight

maxm = 4 # rectangular lattice mxn, m >= n
maxn = 4

total = None
w = {} # weights
d={} # data
required = [] # The list of required data files
missing = [] # The list of missing data files


for n in range (2,maxn+1):
    for m in range(n,maxm+1):

        d,alphas,newrequired,newmissing = mxn_getdata.getdata(m,n,d) # read and check for missing data
        required.extend(newrequired)
        missing.extend(newmissing)

        if len(missing) == 0:
            w = mxn_weight.weight(m,n,d,w) # performs cluster weight calculations

            # cannot use total += w['%02d%02d'%(m,n)] or else W0202 somehow gets changed every iteration
            if total is None:
                total = w['%02d%02d'%(m,n)]
                total2 = 0
            else:
                total2 = w['%02d%02d'%(m,n)]
            total = total + total2

            # Save result to file
            f = open("Results_%02dx%02d" % (m,n), 'w')
            for i in range(len(alphas)):
                f.write("%.20f %.20f\n" % (alphas[i],total[i]))
            f.close()

# Show all required data files
print("The following data files are required:\n", required)

# If any missing data
if len(missing) > 0:
    print("The following data files were not found:\n", missing)


