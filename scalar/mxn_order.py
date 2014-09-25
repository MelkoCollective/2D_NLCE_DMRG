
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
