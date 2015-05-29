
#############################################
# MaxL Order
#
# - N is the maximum linear size
#   e.g. order N=5 is 5x1,5x2,5x3,5x4,5x5
# - Setting min_L=2 means .clusters(5,2)
#   (clusters of order N=5,min_L=2) 
#   will return [(5,2),(5,3),(5,4),(5x5)]
#   i.e. (5,1) cluster will not appear
#
class MaxL:
    def length(self,N):
        return N

    def lengthstr(self,N):
        return "%.1f"%self.length(N)

    def clusters(self,N,min_L=1):
        x = int(N)
        y = min_L
        res = [(x,y),]
        while x > y:
            y += 1
            if x >= y: res.append((x,y))
        return res
#
#############################################

#############################################
# Arithmetic Order
#
# - N is the average linear size
#   e.g. order N=5 is 9x1,8x2,7x3,6x4,5x5
# - Setting min_L=2 means .clusters(5,2)
#   (clusters of order N=5,min_L=2) 
#   will return [(8,2),(7,3),(6,4),(5x5)]
#   i.e. (9,1) cluster will not appear
#
class Arithmetic:

    def length(self,N):
        return N

    def lengthstr(self,N):
        return "%.1f"%self.length(N)

    def clusters(self,N,min_L=1):
        x = int(2*N-min_L)
        y = min_L
        res = [(x,y),]
        while x > y:
            x -= 1
            y += 1
            if x >= y: res.append((x,y))
        return res
#
#############################################

#
# Old version of Arithmetic order,
# had confusing meaning of N as 
# the x size of the largest (x,2)
# cluster
#
#class Arithmetic:
#
#    def length(self,N):
#        return (2+N)/2.
#
#    def lengthstr(self,N):
#        return "%.1f"%self.length(N)
#
#    def clusters(self,N):
#        x = N
#        y = 2
#        res = [(x,y),]
#        while x > (y+1):
#            x -= 1
#            y += 1
#            res.append((x,y))
#        return res

class Geometric:

    def length(self,L):
        return L

    def lengthstr(self,L):
        return "%.1f"%self.length(L)

    def clusters(self,L):
        from math import sqrt
        from frange import frange
        res = []
        for y in frange(2,L+1.):
            for x in frange(y,L+1.):
                ll = sqrt(x*y)
                if (ll > (L-0.5) or abs(ll-(L-0.5))<1E-5) and (ll < L or abs(ll-L)<1E-5):
                    res.append((int(x),int(y)))
        return res
