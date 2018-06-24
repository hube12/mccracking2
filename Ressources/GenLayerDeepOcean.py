from genLayer import Main
import numpy as np

class GenLayerDeepOcean(Main):
    def __init__(self, seed, layer,goup):
        super().__init__(seed)
        self.parent = [(layer,goup)]

    def getInts(self, aX, aY, aW, aH):

        i, j, k, l = aX - 1, aY - 1, aW + 2, aH + 2
        aint = self.parent[0][0].getInts(i, j, k, l)
        aint1 = np.empty(aW*aH,dtype=int)
        for i1 in range(aH):
            for j1 in range(aW):
                k1 = aint[j1 + 1 + (i1) * k]
                l1 = aint[j1 + 2 + (i1 + 1) * k]
                i2 = aint[j1 + (i1 + 1) * k]
                j2 = aint[j1 + 1 + (i1 + 2) * k]
                k2 = aint[j1 + 1 + (i1 + 1) * k]
                l2 = 0
                if not k1:
                    l2 += 1
                if not l1:
                    l2 += 1
                if not i2:
                    l2 += 1
                if not j2:
                    l2 += 1

                if not k2 and l2 > 3:
                    aint1[j1 + i1 * aW] = 24  # deep_ocean
                else:
                    aint1[j1 + i1 * aW] = k2

        return aint1
