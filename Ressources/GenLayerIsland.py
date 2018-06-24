from genLayer import Main
import numpy as np

class GenLayerIsland(Main):
    def __init__(self, seed):
        super().__init__(seed)
        self.parent=[]

    def getInts(self, aX, aY, aW, aH):

        aint = np.empty(aW*aH,dtype=int)
        for i in range(aH):
            for j in range(aW):
                self.initChunkSeed((aX + j, aY + i))
                aint[j+i*aW]=1 if self.nextIntGen(10) == 0 else 0

        if 0 >= aX > -aW and 0 >= aY > -aH:
            aint[-aX - aY * aW] = 1


        return aint
