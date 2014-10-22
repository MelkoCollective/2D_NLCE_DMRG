
import numpy

def extract(fname, xs,xmin=None,xmax=None):
    f = open(fname, 'r')
    col1 = []
    col2 = []
    col3 = []
    for lines in f:
        line = lines.split()
        doappend = True
        x = float(line[0])
        if xmin and x < xmin: doappend = False
        if xmax and x > xmax: doappend = False
        if doappend:
            col1.append(float(line[0]))
            col2.append(float(line[1]))
            if len(line) >= 3:
                col3.append(float(line[2]))
            else:
                col3.append(0)
    f.close()

    if len(xs)==0: xs = numpy.array(col1)
    col2 = numpy.array(col2)
    col3 = numpy.array(col3)

    return col2, xs, col3

