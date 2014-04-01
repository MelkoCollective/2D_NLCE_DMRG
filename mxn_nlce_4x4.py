import numpy
import mxn_getdata

maxm = 4 
maxn = 4

total = None
w = {} # weights
d={} # data
required = [] # The list of required data files
missing = []  # The list of missing data files


# read data and check for any missing
for n in range (2,maxn+1):
    for m in range(n,maxm+1):
        d,alphas,newrequired,newmissing = mxn_getdata.getdata(m,n,d)
        required.extend(newrequired)
        missing.extend(newmissing)
        
# Show all required data files
print("The following data files are required:\n", required)

# If any missing data
if len(missing) > 0:
    print("The following data files were not found\n", missing)
else:
                
    # All calculations and formulas will be written out explicitly
    P0202 = 0.5*(2*d["C0202_0101"] - 2*d["L0202_01"])
    P0302 = 0.5*(2*( d["C0302_0101"] + d["C0302_0201"] ) - 2*d["L0302_01X"] - 2*d["L0302_01Y"])
    P0402 = 0.5*(2*( d["C0402_0101"] + d["C0402_0201"] + d["C0402_0301"] ) - 3*d["L0402_01X"] - 2*d["L0402_01Y"] - d["L0402_02Y"])
    P0303 = 0.5*(2*( d["C0303_0101"] + d["C0303_0202"] ) + 4*d["C0303_0201"] - 8*d["L0303_01"])
    P0403 = 0.5*(2*( d["C0403_0101"] + d["C0403_0201"] + d["C0403_0301"] + d["C0403_0202"] + d["C0403_0302"] + d["C0403_0102"] ) - 6*d["L0403_01X"] - 4*d["L0403_01Y"] - 2*d["L0403_02Y"])
    P0404 = 0.5*(2*( d["C0404_0101"] + d["C0404_0202"] + d["C0404_0303"] ) + 4*( d["C0404_0201"] + d["C0404_0301"] + d["C0404_0302"] ) - 12*d["L0404_01"] - 6*d["L0404_02"])
    
    W0202 = P0202
    W0302 = P0302 - 2*W0202
    W0402 = P0402 - 2*W0302 - 3*W0202
    W0303 = P0303 - 4*W0302 - 4*W0202
    W0403 = P0403 - 2*W0402 - 2*W0303 - 7*W0302 - 6*W0202
    W0404 = P0404 - 4*W0403 - 6*W0402 - 4*W0303 - 12*W0302 - 9*W0202

    total = W0202 + W0302 + W0402 + W0303 + W0403 + W0404

    # Save result to file
    for n in range (2,maxn+1):
        for m in range(n,maxm+1):
            f = open("Results_%02dx%02d_explicit" % (m,n), 'w')
            for i in range(len(alphas)):
                f.write("%.20f %.20f\n" % (alphas[i],total[i]))
            f.close()

