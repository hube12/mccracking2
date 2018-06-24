from genLayer import Main
import numpy as np

class GenLayerEdge(Main):
    def __init__(self, seed, layer, mode, goup):
        super().__init__(seed)
        self.parent = [(layer,goup)]
        self.mode = mode

    def getInts(self, aX, aY, aW, aH):
        if self.mode == "COOL_WARM":
            return self.getIntsCoolWarm(aX, aY, aW, aH)
        elif self.mode == "HEAT_ICE":
            return self.getIntsHeatIce(aX, aY, aW, aH)
        else:
            return self.getIntsSpecial(aX, aY, aW, aH)

    def getIntsCoolWarm(self, aX, aY, aW, aH):
        i, j, k, l = aX - 1, aY - 1, aW + 2, aH + 2
        aint = self.parent[0][0].getInts(i, j, k, l)
        aint1 = np.empty(aW*aH,dtype=int)
        for i1 in range(aH):
            for j1 in range(aW):
                self.initChunkSeed((j1 + aX, i1 + aY))
                k1 = aint[j1 + 1 + (i1 + 1) * k]
                if k1 == 1:
                    l1 = aint[j1 + 1 + (i1) * k]
                    i2 = aint[j1 + 2 + (i1 + 1) * k]
                    j2 = aint[j1 + (i1 + 1) * k]
                    k2 = aint[j1 + 1 + (i1 + 2) * k]
                    flag = l1 == 3 or i2 == 3 or j2 == 3 or k2 == 3
                    flag1 = l1 == 4 or i2 == 4 or j2 == 4 or k2 == 4
                    if flag or flag1:
                        k1 = 2
                aint1[j1 + i1 * aW] = k1

        return aint1

    def getIntsHeatIce(self, aX, aY, aW, aH):
        i, j, k, l = aX - 1, aY - 1, aW + 2, aH + 2
        aint = self.parent[0][0].getInts(i, j, k, l)
        aint1 = np.empty(aW*aH,dtype=int)
        for i1 in range(aH):
            for j1 in range(aW):
                self.initChunkSeed((j1 + aX, i1 + aY))
                k1 = aint[j1 + 1 + (i1 + 1) * k]
                if k1 == 4:
                    l1 = aint[j1 + 1 + (i1) * k]
                    i2 = aint[j1 + 2 + (i1 + 1) * k]
                    j2 = aint[j1 + (i1 + 1) * k]
                    k2 = aint[j1 + 1 + (i1 + 2) * k]
                    flag = l1 == 2 or i2 == 2 or j2 == 2 or k2 == 2
                    flag1 = l1 == 1 or i2 == 1 or j2 == 1 or k2 == 1
                    if flag or flag1:
                        k1 = 3
                aint1[j1 + i1 * aW] = k1

        return aint1

    def getIntsSpecial(self, aX, aY, aW, aH):
        aint = self.parent[0][0].getInts(aX, aY, aW, aH)
        aint1 = np.empty(aW*aH,dtype=int)
        for i in range(aH):
            for j in range(aW):
                self.initChunkSeed((j + aX, i + aY))
                k = aint[j + (i) * aW]
                if k and not self.nextIntGen(13):
                    k |= 1 + self.nextIntGen(15) << 8 & 3840

                aint1[j + i * aW] = k

        return aint1
