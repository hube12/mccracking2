from genLayer import Main
import numpy as np

class GenLayerShore(Main):
    def __init__(self, seed, layer,goup):
        super().__init__(seed)
        self.parent = [(layer,goup)]

    def getInts(self, aX, aY, aW, aH):
        aint = self.parent[0][0].getInts(aX - 1, aY - 1, aW + 2, aH + 2)
        aint1 = np.empty(aW*aH,dtype=int)
        for i in range(aH):
            for j in range(aW):
                self.initChunkSeed((j + aX, i + aY))
                k = aint[j + 1 + (i + 1) * (aW + 2)]
                if k == 14:
                    j2 = aint[j + 1 + (i) * (aW + 2)]
                    i3 = aint[j + 2 + (i + 1) * (aW + 2)]
                    l3 = aint[j + (i + 1) * (aW + 2)]
                    k4 = aint[j + 1 + (i + 2) * (aW + 2)]
                    if j2 != 0 and i3 != 0 and l3 != 0 and k4 != 0:  # not ocean
                        aint1[j + i * aW] = k
                    else:
                        aint1[j + i * aW] = 15
                elif self.isValidId(k) and self.sameClass(k, 21):  # jungle test
                    i2 = aint[j + 1 + (i) * (aW + 2)]
                    l2 = aint[j + 2 + (i + 1) * (aW + 2)]
                    k3 = aint[j + (i + 1) * (aW + 2)]
                    j4 = aint[j + 1 + (i + 2) * (aW + 2)]
                    if self.isJungleCompatible(i2) and self.isJungleCompatible(l2) and self.isJungleCompatible(
                            k3) and self.isJungleCompatible(j4):
                        if not self.isBiomeOceanic(i2) and not self.isBiomeOceanic(l2) and not self.isBiomeOceanic(
                                k3) and not self.isBiomeOceanic(j4):
                            aint1[j + i * aW] = k
                        else:
                            aint1[j + i * aW] = 16  # beach
                    else:
                        aint1[j + i * aW] = 23  # jungle edge
                elif not (k in [3, 34, 20]):  # not an extreme hills variant
                    if self.isValidId(k) and self.isSnowy(k):
                        self.replaceIfNeighborOcean(aint, aint1, j, i, aW, k, 26)  # cold beach
                    elif not k in [37, 38]:  # not a mesa or mesa rock
                        if not (k in [0, 24, 6, 7]):  # not a ocean or swamp or river
                            l1 = aint[j + 1 + (i) * (aW + 2)]
                            k2 = aint[j + 2 + (i + 1) * (aW + 2)]
                            j3 = aint[j + (i + 1) * (aW + 2)]
                            i4 = aint[j + 1 + (i + 2) * (aW + 2)]
                            if not self.isBiomeOceanic(l1) and not self.isBiomeOceanic(k2) and not self.isBiomeOceanic(
                                    j3) and not self.isBiomeOceanic(i4):
                                aint1[j + i * aW] = k
                            else:
                                aint1[j + i * aW] = 16  # beach
                        else:
                            aint1[j + i * aW] = k
                    else:
                        l = aint[j + 1 + (i) * (aW + 2)]
                        i1 = aint[j + 2 + (i + 1) * (aW + 2)]
                        j1 = aint[j + (i + 1) * (aW + 2)]
                        k1 = aint[j + 1 + (i + 2) * (aW + 2)]
                        if not self.isBiomeOceanic(l) and not self.isBiomeOceanic(i1) and not self.isBiomeOceanic(
                                j1) and not self.isBiomeOceanic(k1):
                            if self.isMesa(l) and self.isMesa(i1) and self.isMesa(j1) and self.isMesa(k1):
                                aint1[j + i * aW] = k
                            else:
                                aint1[j + i * aW] = 2  # desert
                        else:
                            aint1[j + i * aW] = k
                else:
                    self.replaceIfNeighborOcean(aint, aint1, j, i, aW, k, 25)  # stone beach

        return aint1

    def replaceIfNeighborOcean(self, aint, aint1, j, i, aW, k, biomeToReplace):
        if self.isBiomeOceanic(k):
            aint1[j + i * aW] = k
        else:
            l1 = aint[j + 1 + (i) * (aW + 2)]
            k2 = aint[j + 2 + (i + 1) * (aW + 2)]
            j3 = aint[j + (i + 1) * (aW + 2)]
            i4 = aint[j + 1 + (i + 2) * (aW + 2)]
            if not self.isBiomeOceanic(l1) and not self.isBiomeOceanic(k2) and not self.isBiomeOceanic(
                    j3) and not self.isBiomeOceanic(i4):
                aint1[j + i * aW] = k
            else:
                aint1[j + i * aW] = biomeToReplace

    def isJungleCompatible(self, id):
        if self.isValidId(id) and self.sameClass(id, 21):
            return True
        else:
            return id in [23, 22, 21, 4, 5] or self.isBiomeOceanic(id)  # jungle biomes or taiga or forest or oceanic

    def isMesa(self, id):
        return id in [37, 38, 39, 165, 166, 167]
