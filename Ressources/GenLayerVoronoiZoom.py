from genLayer import Main
import numpy as np


class GenLayerVoronoiZoom(Main):
    def __init__(self, seed, layer,goup):
        super().__init__(seed)
        self.parent = [(layer,goup)]

    def getInts(self, aX, aY, aW, aH):
        aX -= 2
        aY -= 2
        i = aX >> 2
        j = aY >> 2
        k = (aW >> 2) + 2
        l = (aH >> 2) + 2
        aint = self.parent[0][0].getInts(i, j, k, l)
        i1 = k - 1 << 2
        j1 = k - 1 << 2
        aint1 = np.empty(i1 * j1,dtype=int)
        for k1 in range(l - 1):
            i2 = aint[0 + k1 * k]
            for l1 in range(k - 1):
                j2 = aint[l1 + (k1 + 1) * k]
                d0 = 3.6
                self.initChunkSeed((k1 + i << 2, k1 + j << 2))

                d1 = (self.nextIntGen(1024) / 1024 - 0.5) * 3.6
                d2 = (self.nextIntGen(1024) / 1024 - 0.5) * 3.6
                self.initChunkSeed((l1 + i + 1 << 2, k1 + j << 2))
                d3 = (self.nextIntGen(1024) / 1024 - 0.5) * 3.6 + 4
                d4 = (self.nextIntGen(1024) / 1024 - 0.5) * 3.6
                self.initChunkSeed((l1 + i << 2, k1 + j + 1 << 2))
                d5 = (self.nextIntGen(1024) / 1024 - 0.5) * 3.6
                d6 = (self.nextIntGen(1024) / 1024 - 0.5) * 3.6 + 4
                self.initChunkSeed((l1 + i + 1 << 2, k1 + j + 1 << 2))
                d7 = (self.nextIntGen(1024) / 1024 - 0.5) * 3.6 + 4
                d8 = (self.nextIntGen(1024) / 1024 - 0.5) * 3.6 + 4
                k2 = aint[l1 + 1 + k1 * k] & 255
                l2 = aint[l1 + 1 + (k1 + 1) * k] & 255
                for i3 in range(4):
                    j3 = ((k1 << 2) + i3) * i1 + (l1 << 2)
                    for k3 in range(4):
                        d9 = (i3 - d2) ** 2 + (k3 - d1) ** 2
                        d10 = (i3 - d4) ** 2 + (k3 - d3) ** 2
                        d11 = (i3 - d6) ** 2 + (k3 - d5) ** 2
                        d12 = (i3 - d8) ** 2 + (k3 - d7) ** 2
                        if d9 < d10 and d9 < d11 and d9 < d12:
                            aint1[j3] = i2
                        elif d10 < d9 and d10 < d11 and d10 < d12:
                            aint1[j3] = k2
                        elif d11 < d10 and d11 < d9 and d11 < d12:
                            aint1[j3] = j2
                        else:
                            aint1[j3] = l2
                        j3 += 1
                i2 = k2
                j2 = l2
        aint2 = np.empty(aW*aH,dtype=int)
        for l3 in range(aH):
            aint2[l3 * aW:(l3 + 1) * aW] = np.copy(aint1[(l3 + (aY & 3)) * i1 + (aX & 3):(l3 + (aY & 3)) * i1 + (aX & 3) + aW])

        return aint2
