from genLayer import Main
import numpy as np

class GenLayerBiomeEdge(Main):
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
                if (not self.replaceBiomeEdgeIfNecessary(aint, aint1, j, i, aW, k, 3, 20)) and (
                        not self.replaceBiomeEdge(aint, aint1, j, i, aW, k, 38, 37)) and (
                        not self.replaceBiomeEdge(aint, aint1, j, i, aW, k, 39, 37)) and (
                        not self.replaceBiomeEdge(aint, aint1, j, i, aW, k, 32, 5)):
                    # extreme hills switch to extreme hills edge then mesa rock to mesa, mesa clear rock to mesa and redwood taiga to taiga
                    if k == 2:  # desert
                        l1 = aint[j + 1 + i * (aW + 2)]
                        i2 = aint[j + 2 + (i + 1) * (aW + 2)]
                        j2 = aint[j + (i + 1) * (aW + 2)]
                        k2 = aint[j + 1 + (i + 2) * (aW + 2)]
                        if l1 != 12 and i2 != 12 and j2 != 12 and k2 != 12:  # ice plains
                            aint1[j + i * aW] = k
                        else:
                            aint1[j + i * aW] = 34  # extreme hills with trees
                    elif k == 6:  # swampland
                        l1 = aint[j + 1 + i * (aW + 2)]
                        i2 = aint[j + 2 + (i + 1) * (aW + 2)]
                        j2 = aint[j + (i + 1) * (aW + 2)]
                        k2 = aint[j + 1 + (i + 2) * (aW + 2)]
                        x = [2, 30, 12]  # desert,cold taiga and ice plains
                        if not (l1 in x) and not (i2 in x) and not (j2 in x) and not (k2 in x):
                            if l1 != 21 and j2 != 21 and i2 != 21 and k2 != 21:  # jungle
                                aint1[j + i * aW] = k
                            else:
                                aint1[j + i * aW] = 23  # jungle edge
                        else:
                            aint1[j + i * aW] = 1  # plains
                    else:
                        aint1[j + i * aW] = k

        return aint1

    def replaceBiomeEdgeIfNecessary(self, aint, aint1, j1, i1, aW, k1, biome1, biome2):
        if not self.biomesEqualOrMesaPlateau(k1, biome1):
            return False
        else:
            i = aint[j1 + 1 + i1 * (aW + 2)]
            j = aint[j1 + 2 + (i1 + 1) * (aW + 2)]
            k = aint[j1 + (i1 + 1) * (aW + 2)]
            l = aint[j1 + 1 + (i1 + 2) * (aW + 2)]
            if self.canBiomesBeNeighbors(i, biome1) and self.canBiomesBeNeighbors(j, biome1) \
                    and self.canBiomesBeNeighbors(k, biome1) and self.canBiomesBeNeighbors(l, biome1):
                aint1[j1 + i1 * aW] = k1
            else:
                aint1[j1 + i1 * aW] = biome2
            return True

    def replaceBiomeEdge(self, aint, aint1, j1, i1, aW, k1, biome1, biome2):
        if k1 != biome1:
            return False
        else:
            i = aint[j1 + 1 + i1 * (aW + 2)]
            j = aint[j1 + 2 + (i1 + 1) * (aW + 2)]
            k = aint[j1 + (i1 + 1) * (aW + 2)]
            l = aint[j1 + 1 + (i1 + 2) * (aW + 2)]
            if self.biomesEqualOrMesaPlateau(i, biome1) and self.biomesEqualOrMesaPlateau(j, biome1) \
                    and self.biomesEqualOrMesaPlateau(k, biome1) and self.biomesEqualOrMesaPlateau(l, biome1):
                aint1[j1 + i1 * aW] = k1
            else:
                aint1[j1 + i1 * aW] = biome2
        return True

    def canBiomesBeNeighbors(self, biome1, biome2):
        if self.biomesEqualOrMesaPlateau(biome1, biome2):
            return True
        else:
            if self.isValidId(biome1) and self.isValidId(biome2):
                t1, t2 = self.getTempCategory(biome1), self.getTempCategory(biome2)
                return t1 == t2 or t1 == 1 or t2 == 1
            else:
                return False
