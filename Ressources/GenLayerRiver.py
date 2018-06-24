from genLayer import Main
import numpy as np

class GenLayerRiver(Main):
    def __init__(self, seed, layer,goup):
        super().__init__(seed)
        self.parent = [(layer,goup)]

    def getInts(self, aX, aY, aW, aH):
        i, j, k, l = aX - 1, aY - 1, aW + 2, aH + 2
        aint = self.parent[0][0].getInts(i, j, k, l)
        aint1 = np.empty(aW*aH,dtype=int)
        for i1 in range(aH):
            for j1 in range(aW):
                k1 = self.riverFilter(aint[j1 + (i1 + 1) * k])
                l1 = self.riverFilter(aint[j1 + 2 + (i1 + 1) * k])
                i2 = self.riverFilter(aint[j1 + 1 + (i1) * k])
                j2 = self.riverFilter(aint[j1 + 1 + (i1 + 2) * k])
                k2 = self.riverFilter(aint[j1 + 1 + (i1 + 1) * k])
                if k2 == k1 and k2 == i2 and k2 == l1 and k2 == j2:
                    aint1[j1 + i1 * aW] = -1
                else:
                    aint1[j1 + i1 * aW] = 7

        return aint1

    def riverFilter(self, biomeId):
        return 2 + (biomeId & 1) if biomeId >= 2 else biomeId
