
import numpy

def extract(fname, alphas):
    f = open(fname, 'r')
    col1 = []
    col2 = []
    for lines in f:
        line = lines.split()
        col1.append(float(line[0]))
        col2.append(float(line[1]))
    f.close()

    if len(alphas)==0: alphas = numpy.array(col1)
    col2 = numpy.array(col2)

    return col2, alphas

