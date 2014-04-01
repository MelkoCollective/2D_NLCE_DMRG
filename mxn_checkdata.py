def checkdata(fname):
    try:
        f = open(fname, 'r')
        f.close()
        return []
    except:
        return fname # if file doesnt exist, add name to missing list
