from genLayer import Main
import numpy as np

class GenLayerAddSnow(Main):
    def __init__(self, seed, layer,goup):
        super().__init__(seed)
        self.parent = [(layer,goup)]

    def getInts(self, aX, aY, aW, aH):
        i, j, k, l = aX - 1, aY - 1, aW + 2, aH + 2
        aint = self.parent[0][0].getInts(i, j, k, l)
        aint1 = np.empty(aW*aH,dtype=int)
        for i1 in range(aH):
            for j1 in range(aW):
                k1 = aint[j1 + 1 + (i1 + 1) * k]
                self.initChunkSeed((j1 + aX, i1 + aY))
                if not k1:
                    aint1[j1 + i1 * aW] = 0
                else:
                    l1 = self.nextIntGen(6)
                    if not l1:
                        l1 = 4
                    elif l1 < 2:
                        l1 = 3
                    else:
                        l1 = 1
                    aint1[j1 + i1 * aW] = l1

        return aint1
