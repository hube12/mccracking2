from genLayer import Main
import numpy as np

class GenLayerBiome(Main):
    def __init__(self, seed, layer,customized,goup):
        super().__init__(seed)
        self.parent = [(layer,goup)]
        if customized[0]==4:
            print("I dont support WorldType.DEFAULT_1_1")
    def getInts(self, aX, aY, aW, aH):
        aint = self.parent[0][0].getInts(aX, aY, aW, aH)
        aint1 = np.empty(aW*aH,dtype=int)
        for i in range(aH):
            for j in range(aW):
                self.initChunkSeed((j+aX,i+aY))
                k=aint[j+i*aW]
                l=(k&3840)>>8
                k=k&-3841
                if self.isBiomeOceanic(k):
                    aint1[j + i * aW]=k #oceans
                elif (k==14):
                    aint1[j + i * aW] = k #mushroom
                elif k==1:
                    if l>0:
                        if not self.nextIntGen(3):
                            aint1[j + i * aW] = 39 #mesa clear rock
                        else:
                            aint1[j + i * aW] = 38 #mesa rock
                    else:
                        aint1[j + i * aW] = [2,2,2,35,35,1][self.nextIntGen(6)] #desert, savannah or plains
                elif k==2:
                    if l>0:
                        aint1[j + i * aW] = 21 #jungle
                    else:
                        aint1[j + i * aW] = [4,29,3,1,27,6][self.nextIntGen(6)] #forest,roofed forest, extreme hills, plains, birch forest, swampland
                elif k==3:
                    if l>0:
                        aint1[j + i * aW]=32 # redwood taiga
                    else:
                        aint1[j + i * aW]=[4,3,5,1][self.nextIntGen(4)] #forest,extreme hills,taiga,plains
                elif k==4:
                    aint1[j + i * aW]=[12,12,12,30][self.nextIntGen(4)] #ice plains (flats),cold taiga
                else:
                    aint1[j + i * aW]=14 #mushroom again

        return aint1

