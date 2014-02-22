import numpy

n = 4           # square lattice nxn
Nx = 2
#Ny = 2       # Not needed since it will only be square lattices in data file (Nx=Ny)
x = 1
y = 1

############### To read the data files ##################

alphas = []

# For the Cxx_xx
while Nx <= n:       #loops from c0202_0101, c0303_0101, ... , C0404_0303
    fname = "C%02d%02d_%02d%02d"%(Nx,Nx,x,y)
    f = open(fname, 'r')
    col1 = []
    col2 = []
    for lines in f:
        line = lines.split()
        col1.append(float(line[0]))
        col2.append(float(line[1]))
    f.close()

    if len(alphas)==0: alphas = numpy.array(col1)

    # to assign correct labels
    
    # This part gave me trouble. If I put this or the while loop into a seperate function I would
    # lose the label that I had just assigned it here
    if Nx == 2 and x == 1 and y == 1: C0202_0101 = numpy.array(col2)
    if Nx == 3 and x == 1 and y == 1: C0303_0101 = numpy.array(col2)
    if Nx == 3 and x == 1 and y == 2: C0303_0102 = numpy.array(col2)
    if Nx == 3 and x == 2 and y == 2: C0303_0202 = numpy.array(col2)
    if Nx == 4 and x == 1 and y == 1: C0404_0101 = numpy.array(col2)
    if Nx == 4 and x == 1 and y == 2: C0404_0102 = numpy.array(col2)
    if Nx == 4 and x == 1 and y == 3: C0404_0103 = numpy.array(col2)
    if Nx == 4 and x == 2 and y == 2: C0404_0202 = numpy.array(col2)
    if Nx == 4 and x == 2 and y == 3: C0404_0203 = numpy.array(col2)
    if Nx == 4 and x == 3 and y == 3: C0404_0303 = numpy.array(col2)

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
x = 1
i=False     # this is used so it only adds one additional line term at a time


# For the Lxx_x
while Nx <= n:       #loops from L0202_01, L0303_01, ... , L0404_0202
    fname = "L%02d%02d_%02d"%(Nx,Nx,x)
    f = open(fname, 'r')
    col1 = []
    col2 = []
    for lines in f:
        line = lines.split()
        col1.append(float(line[0]))
        col2.append(float(line[1]))
    f.close()

    # to assign correct labels
    if Nx == 2 and x == 1: L0202_01 = numpy.array(col2)
    if Nx == 3 and x == 1: L0303_01 = numpy.array(col2)
    if Nx == 4 and x == 1: L0404_01 = numpy.array(col2)
    if Nx == 4 and x == 2: L0404_02 = numpy.array(col2)

        
    # to cycle through all data
    if Nx%2==0 and i==True:    # An additional line term appears when n is even
        x += 1
        i=False
    else:
        Nx += 1
        x=1
        i=True

############### Perform the calculations ##################

# Corner entropy formulas
p11 = 0
p22 = 2*C0202_0101 - 2*L0202_01
p33 = 2*( C0303_0101 + C0303_0202 ) + 4*C0303_0102 - 8*L0303_01
p44 = 2*( C0404_0101 + C0404_0202 + C0404_0303 ) + \
       4*( C0404_0102 + C0404_0103 + C0404_0203 ) - 12*L0404_01 - 6*L0404_02

# Result
w4 = p44 - 4*p33 + 7*p22 - 8*p11

# Save result to file
f = open('Results_4x4', 'w')
for i in range(len(alphas)):
    f.write("%.20f %.20f\n" % (alphas[i],w4[i]))
f.close()
