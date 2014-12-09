
class Arithmetic:

    def length(self,N):
        return (2+N)/2.

    def lengthstr(self,N):
        return "%.1f"%self.length(N)

    def clusters(self,N):
        x = N
        y = 2
        res = [(x,y),]
        while x > (y+1):
            x -= 1
            y += 1
            res.append((x,y))
        return res

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
