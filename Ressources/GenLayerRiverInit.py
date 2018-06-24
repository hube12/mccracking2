from genLayer import Main
import numpy as np

class GenLayerRiverInit(Main):
    def __init__(self, seed, layer,goup):
        super().__init__(seed)
        self.parent = [(layer,goup)]

    def getInts(self, aX, aY, aW, aH):
        aint = self.parent[0][0].getInts(aX, aY, aW, aH)
        aint1 = np.empty(aW*aH,dtype=int)
        for i in range(aH):
            for j in range(aW):
                self.initChunkSeed((j + aX, i + aY))
                aint1[j+i*aW]=self.nextIntGen(299999)+2 if  aint[j+i*aW] else 0

        return aint1