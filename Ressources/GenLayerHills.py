from genLayer import Main
import numpy as np

class GenLayerHills(Main):
    def __init__(self, seed, layer, river,goup):
        super().__init__(seed)
        self.parent = [(layer,goup),(river,goup)]


    def getInts(self, aX, aY, aW, aH):

        aint = self.parent[0][0].getInts(aX - 1, aY - 1, aW + 2, aH + 2)

        aint1 = self.parent[1][0].getInts(aX - 1, aY - 1, aW + 2, aH + 2)
        aint2 = np.empty(aW*aH,dtype=int)
        for i in range(aH):
            for j in range(aW):
                self.initChunkSeed((j + aX, i + aY))
                k = aint[j + 1 + (i + 1) * (aW + 2)]
                l = aint1[j + 1 + (i + 1) * (aW + 2)]
                flag = not ((l - 2) % 29)

                if k > 255:
                    print("error old!")
                flag1 = self.isValidId(k) and k in [129, 130, 131, 132, 133, 134, 140, 149, 151, 155, 156, 157, 158,
                                                    160, 161, 162, 163, 164, 165, 166, 167]  # its an id and a mutation
                if k and l >= 2 and (l - 2) % 29 == 1 and not flag1:
                    mappingMutation = {1: 129, 2: 130, 3: 131, 4: 132, 5: 133, 6: 134, 12: 140, 21: 149, 23: 151,
                                       27: 155, 28: 156, 29: 157, 30: 158, 32: 160, 33: 161, 34: 162, 35: 163, 36: 164,
                                       37: 165, 38: 166, 39: 167}
                    mutation = k + 128  # +128 if a possible mutated
                    if mutation in [129, 130, 131, 132, 133, 134, 140, 149, 151, 155, 156, 157, 158,
                                    160, 161, 162, 163, 164, 165, 166, 167]:
                        aint2[j + i * aW] = mutation
                    else:
                        aint2[j + i * aW] = k
                elif self.nextIntGen(3) and not flag:
                    aint2[j + i * aW] = k
                else:

                    biome1 = k
                    hillTransformation = {2: 17, 4: 18, 27: 28, 29: 1, 5: 19, 32: 33, 30: 31,
                                          12: 13, 21: 22, 0: 24, 3: 34, 35: 36}
                    for el in hillTransformation:
                        if k == el:

                            biome1 = hillTransformation[el]

                    if biome1 == k:
                        if k==1:
                            if self.nextIntGen(3):
                                biome1=4
                            else:
                                biome1=18
                        if self.biomesEqualOrMesaPlateau(k, 38):  # mesarock
                            biome1 = 37 #mesa
                        elif k == 24 and self.nextIntGen(3) == 0: #deep ocean

                            i1 = self.nextIntGen(2)

                            if i1:
                                biome1 = 4
                            else:
                                biome1 = 1

                    j2 = biome1

                    if flag and biome1 != k:
                        mappingMutation = {1: 129, 2: 130, 3: 131, 4: 132, 5: 133, 6: 134, 12: 140, 21: 149, 23: 151,
                                           27: 155, 28: 156, 29: 157, 30: 158, 32: 160, 33: 161, 34: 162, 35: 163,
                                           36: 164, 37: 165, 38: 166, 39: 167}
                        if biome1 + 128 in [129, 130, 131, 132, 133, 134, 140, 149, 151, 155, 156, 157, 158,
                                            160, 161, 162, 163, 164, 165, 166, 167]:
                            j2 = biome1 + 128
                        else:
                            j2 = k
                    if j2 == k:
                        aint2[j + i * aW] = k
                    else:
                        k2 = aint[j + 1 + (i + 0) * (aW + 2)]
                        j1 = aint[j + 2 + (i + 1) * (aW + 2)]
                        k1 = aint[j + 0 + (i + 1) * (aW + 2)]
                        l1 = aint[j + 1 + (i + 2) * (aW + 2)]
                        i2 = 0
                        if self.biomesEqualOrMesaPlateau(k2, k):
                            i2 += 1
                        if self.biomesEqualOrMesaPlateau(j1, k):
                            i2 += 1
                        if self.biomesEqualOrMesaPlateau(k1, k):
                            i2 += 1
                        if self.biomesEqualOrMesaPlateau(l1, k):
                            i2 += 1
                        if i2>=3:
                            aint2[j+i*aW]=j2
                        else:
                            aint2[j + i * aW] = k



        return aint2
