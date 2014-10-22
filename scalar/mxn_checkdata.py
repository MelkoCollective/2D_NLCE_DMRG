def checkdata(fname):
    try:
        f = open(fname, 'r')
        f.close()
        return True
    except:
        return False
