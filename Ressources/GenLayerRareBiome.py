from genLayer import Main
import numpy as np

class GenLayerRareBiome(Main):
    def __init__(self, seed, layer,goup):
        super().__init__(seed)
        self.parent = [(layer,goup)]

    def getInts(self, aX, aY, aW, aH):
        aint = self.parent[0][0].getInts(aX - 1, aY - 1, aW + 2, aH + 2)
        aint1 = np.empty(aW*aH,dtype=int)
        for i in range(aH):
            for j in range(aW):
                self.initChunkSeed((j + aX, i + aY))
                k=aint[j+1+(i+1)*(aW+2)]
                if not self.nextIntGen(57):
                    if k==1:
                        aint1[j+i*aW]=129 #mutated plains
                    else:
                        aint1[j + i * aW] =k
                else:
                    aint1[j + i * aW] =k

        return aint1
