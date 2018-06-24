from genLayer import Main
import numpy as np

class GenLayerSmooth(Main):
    def __init__(self, seed, layer,goup):
        super().__init__(seed)
        self.parent = [(layer,goup)]


    def getInts(self, aX, aY, aW, aH):
        i, j, k, l = aX - 1, aY - 1, aW + 2, aH + 2
        aint = self.parent[0][0].getInts(i, j, k, l)
        aint1 = np.empty(aW*aH,dtype=int)
        for i1 in range(aH):
            for j1 in range(aW):
                k1 = aint[j1  + (i1+1) * k]
                l1 = aint[j1 + 2 + (i1 +1) * k]
                i2 = aint[j1 +1+ (i1 ) * k]
                j2 = aint[j1 + 1 + (i1 + 2) * k]
                k2 = aint[j1 + 1 + (i1 + 1) * k]
                if k1==l1 and i2==j2:
                    self.initChunkSeed((j1+aX,i1+aY))
                    if self.nextIntGen(2):
                        k2=i2
                    else:
                        k2=k1
                else:
                    if k1==l1:
                        k2=k1
                    if i2==j2:
                        k2=i2
                aint1[j1+i1*aW]=k2
        return aint1