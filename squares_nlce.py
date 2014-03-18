import numpy

n = 6           # square lattice nxn

Nx = 2
#Ny = 2       # Not needed since it will only be square lattices in data file (Nx=Ny)
x = 1
y = 1

############### To read the data files ##################

alphas = []
d = {}

# For the Cxx_xx
while Nx <= n:       #loops from c0202_0101, c0303_0101, ... , C0404_0303
    fname = "C%02d%02d_%02d%02d"%(Nx,Nx,x,y)
    print fname
    f = open(fname, 'r')
    col1 = []
    col2 = []
    for lines in f:
        line = lines.split()
        col1.append(float(line[0]))
        col2.append(float(line[1]))
    f.close()

    if len(alphas)==0: alphas = numpy.array(col1)

    d[fname] = numpy.array(col2)

    # to cycle through all data
    if y==Nx-1 and x==Nx-1:     #C0303_0202 is the last term required for C0303 data, now move to C0404_0101
        Nx += 1
        x=1
        y=1
    elif y==Nx-1:     #go from C0303_0102 to C0303_0202
        x += 1
        y = x
    else:             #go from C0303_0101 to C0303_0102
        y += 1


Nx = 2

# For the Lxx_x
for Nx in range(2,n+1):       #loops from L0202_01, L0303_01, ... , L0404_0202
    for x in range(1,Nx//2+1):
        fname = "L%02d%02d_%02d"%(Nx,Nx,x)
        print fname
        f = open(fname, 'r')
        col1 = []
        col2 = []
        for lines in f:
            line = lines.split()
            col1.append(float(line[0]))
            col2.append(float(line[1]))
        f.close()

        d[fname] = numpy.array(col2)
            

############### Perform the calculations ##################

Zero = 0*alphas # numpy array of zeros

# Corner entropy formulas
p11 = Zero
p22 = 2*d['C0202_0101'] - 2*d['L0202_01']
p33 = 2*( d['C0303_0101'] + d['C0303_0202'] ) + 4*d['C0303_0102'] - 8*d['L0303_01']
p44 = 2*( d['C0404_0101'] + d['C0404_0202'] + d['C0404_0303'] ) + \
      4*( d['C0404_0102'] + d['C0404_0103'] + d['C0404_0203'] ) - 12*d['L0404_01'] - 6*d['L0404_02']
p55 = 2*( d['C0505_0101'] + d['C0505_0202'] + d['C0505_0303'] + d['C0505_0404'] ) + \
      4*( d['C0505_0102'] + d['C0505_0103'] + d['C0505_0104'] + d['C0505_0203'] + d['C0505_0204'] + d['C0505_0304'] ) - 16*d['L0505_01'] - 16*d['L0505_02']
p66 = 2*( d['C0606_0101'] + d['C0606_0202'] + d['C0606_0303'] + d['C0606_0404'] + d['C0606_0505'] ) + \
      4*( d['C0606_0102'] + d['C0606_0103'] + d['C0606_0104'] + d['C0606_0105'] + d['C0606_0203'] + d['C0606_0204'] + d['C0606_0205'] + d['C0606_0304'] + d['C0606_0305'] + d['C0606_0405'] ) \
      - 20*d['L0606_01'] - 20*d['L0606_02'] - 10*d['L0606_03']

# Weights
w = []
w.append( p11 )
w.append( p22 - 4*p11 )
w.append( p33 - 4*p22 + 7*p11 )
w.append( p44 - 4*p33 + 7*p22 - 8*p11 )
w.append( p55 - 4*p44 + 7*p33 - 8*p22 + 8*p11 )
w.append( p66 - 4*p55 + 7*p44 - 8*p33 + 8*p22 - 8*p11 )

# Results (partial sums of weights)
psum = Zero
for o in range(n):
    psum += w[o]
    # Save result to file
    f = open("Results_%02dx%02d" % (1+o,1+o), 'w')
    for i in range(len(alphas)):
        f.write("%.20f %.20f\n" % (alphas[i],psum[i]*0.5))
    f.close()
