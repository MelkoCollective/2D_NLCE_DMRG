
class Arithmetic:


    def length(self,N):
        return float(N/2)

    def lengthstr(self,N):
        return "%.1f"%self.length(N)

    def clusters(self,N):
        x = N-2
        y = 2
        res = [(x,y),]
        while x > (y+1):
            x -= 1
            y += 1
            res.append((x,y))
        return res

class Geometric:


    def length(self,N):
        import math
        return math.sqrt(N)

    def lengthstr(self,N):
        return "%.4f"%self.length(N)

    def clusters(self,N):
        tol=10**-9
        maxy=int(N/2)
        res=[]
        for y in range(2,maxy+1):
            x=N/y
            xf=float(N)/y
            diff=xf-x
            if diff < tol:
                if x >= y:
                    res.append((x,y))

        return res

class Circular:


    def length(self,N):
        import math
        return math.sqrt(N)

    def lengthstr(self,N):
        return "%.4f"%self.length(N)

    def clusters(self,N):
        from math import sqrt
        tol=10**-9
        maxy=int(sqrt(N))
        res=[]
        for y in range(2,maxy+1):
            x2=N-y*y
            x=sqrt(x2)
            xint=int(x)
            diff=x-xint
            if diff < tol:
                if x >= y:
                    res.append((xint,y))

        return res
