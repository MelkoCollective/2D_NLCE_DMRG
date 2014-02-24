############### To read the data files ##################

def getdata(n):

    import numpy
    cl = ['C', 'L']   # to disntinguish the data types
    d = {}            # data
    alphas = []
    
    for corl in cl:
        Nx = 2
        x = 1
        y = 1
        
        while Nx <= n:       # loops from c0202_0101, c0303_0101, ... , C0404_0303, ...
            if corl=='C':
                fname = "%s%02d%02d_%02d%02d"%(corl,Nx,Nx,x,y)
            else:
                fname = "%s%02d%02d_%02d"%(corl,Nx,Nx,x)
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
            if corl == 'C':
                if y==Nx-1 and x==Nx-1:     # C0303_0202 is the last term required for C0303 data, now move to C0404_0101
                    Nx += 1
                    x=1
                    y=1
                elif y==Nx-1:     # go from C0404_0102 to C0404_0202
                    x += 1
                    y = x
                else:             # go from C0404_0101 to C0404_0102
                    y += 1
            else:
                if Nx < 2*(x+1):
                    Nx += 1
                    x=1
                else:
                    x += 1
    return d, alphas
