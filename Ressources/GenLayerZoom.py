from genLayer import Main
import numpy as np


class GenLayerZoom(Main):
    def __init__(self, seed, layer,fuzzy, goup,WorldGenSeedDisable):
        super().__init__(seed)
        self.parent = [(layer, goup)]
        self.fuzzy=fuzzy
        self.switchs=WorldGenSeedDisable

    def getInts(self, aX, aY, aW, aH):
        if not self.switchs:
            self.worldGenSeed=0
        i, j, k, l = aX >> 1, aY >> 1, (aW >> 1) + 2, (aH >> 1) + 2

        aint = self.parent[0][0].getInts(i, j, k, l)

        i1 = (k - 1) << 1
        j1 = (l - 1) << 1

        aint1 = [0] * (i1 * j1)

        for k1 in range(l - 1):
            l1 = (k1 << 1) * i1
            j2 = aint[k1 * k]
            for i2 in range(k - 1):
                k2 = aint[i2 + (k1 + 1) * k]
                self.initChunkSeed(((i2 + i) << 1, (k1 + j) << 1))
                l2 = aint[i2 + 1 + k1 * k]
                i3 = aint[i2 + 1 + (k1 + 1) * k]
                aint1[l1] = j2
                aint1[l1 + i1] = self.selectRandom([j2, k2])
                l1 += 1
                aint1[l1] = self.selectRandom([j2, l2])
                if self.fuzzy:
                    aint1[l1 + i1] = self.selectRandom([j2, l2, k2, i3])
                else:
                    aint1[l1 + i1] = self.selectModeOrRandom(j2, l2, k2, i3)
                l1+=1
                j2, k2 = l2, i3

        aint2 = np.empty(aW * aH, dtype=int)
        for j3 in range(aH):
            aint2[j3 * aW:(j3 + 1) * aW] = np.copy(
                aint1[(j3 + (aY & 1)) * i1 + (aX & 1): (j3 + (aY & 1)) * i1 + (aX & 1) + aW])


        return aint2

    def magnify(seed, layer, coeff,fuzzy, goup,switch):
        for i in range(coeff):
            layer = GenLayerZoom(seed + i, layer,fuzzy, goup,switch)
        return layer
