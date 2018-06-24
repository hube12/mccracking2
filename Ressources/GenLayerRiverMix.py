from genLayer import Main
import numpy as np

class GenLayerRiverMix(Main):
    def __init__(self, seed, biomePattern, riverPattern,goup):
        super().__init__(seed)
        self.parent=[(biomePattern,goup),(riverPattern,goup)]


    def getInts(self, aX, aY, aW, aH):

        aint = self.parent[0][0].getInts(aX, aY, aW, aH)

        aint1 = self.parent[1][0].getInts(aX, aY, aW, aH)
        aint2 = np.empty(aW*aH,dtype=int)
        for i in range(aH * aW):
            if aint[i] != 0 and aint[i] != 24:  # not ocean
                if aint1[i] == 7:  # river
                    if aint[i] == 12:  # ice plains
                        aint2[i] = 11  # frozen river
                    elif aint[i] != 14 and aint[i] != 15:  # not mushroom
                        aint2[i] = aint1[i] & 255
                    else:
                        aint2[i] = 15  # mushroom shore
                else:
                    aint2[i] = aint[i]
            else:
                aint2[i] = aint[i]

        return aint2


