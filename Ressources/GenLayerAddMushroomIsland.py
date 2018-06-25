from genLayer import Main
import numpy as np

class GenLayerAddMushroomIsland(Main):
    def __init__(self, seed, layer,goup):
        super().__init__(seed)
        self.parent = [(layer,goup)]
    def getInts(self, aX, aY, aW, aH):
        i, j, k, l = aX - 1, aY - 1, aW + 2, aH + 2
        aint = self.parent[0][0].getInts(i, j, k, l)
        aint1 = np.empty(aW*aH,dtype=int)
        for i1 in range(aH):
            for j1 in range(aW):
                k1 = aint[j1 + i1 * (aW + 2)]
                l1 = aint[j1 + 2 + (i1) * (aW + 2)]
                i2 = aint[j1 + (i1 + 2) * (aW + 2)]
                j2 = aint[j1 + 2 + (i1 + 2) * (aW + 2)]
                k2 = aint[j1 + 1 + (i1 + 1) * (aW + 2)]
                self.initChunkSeed((j1+aX,i1+aY))
                if not k2 and not k1 and not l1 and not j2 and not i2 and not self.nextIntGen(100):
                    aint1[j1+i1*aW]=14 #mushroom_island
                else:
                    aint1[j1 + i1 * aW]=k2

        return aint1
