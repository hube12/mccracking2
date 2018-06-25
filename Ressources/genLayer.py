import numpy as np
from collections import Counter
from copy import deepcopy

class Main:
    def __init__(self, seed=None):
        if seed:
            self.baseSeed = seed
            self.baseSeed *= self.baseSeed * 6364136223846793005 + 1442695040888963407
            self.baseSeed += seed
            self.baseSeed *= self.baseSeed * 6364136223846793005 + 1442695040888963407
            self.baseSeed += seed
            self.baseSeed *= self.baseSeed * 6364136223846793005 + 1442695040888963407
            self.baseSeed += seed
            self.baseSeed = self.javaInt64(self.baseSeed)

    def javaInt64(self, val):
        return ((val + (1 << 63)) % (1 << 64)) - (1 << 63)

    def initChunkSeed(self, chunk):
        chunkSeed = self.worldGenSeed
        chunkSeed *= (chunkSeed * 6364136223846793005 + 1442695040888963407)
        chunkSeed += chunk[0]
        chunkSeed *= (chunkSeed * 6364136223846793005 + 1442695040888963407)
        chunkSeed += chunk[1]
        chunkSeed = self.javaInt64(chunkSeed)
        chunkSeed *= (chunkSeed * 6364136223846793005 + 1442695040888963407)
        chunkSeed += chunk[0]
        chunkSeed *= (chunkSeed * 6364136223846793005 + 1442695040888963407)
        chunkSeed += chunk[1]

        self.chunkSeed = self.javaInt64(chunkSeed)

    def countIt(self, array):
        dic = Counter(array)
        print(list(array))
        return [str(el) + " " + str(dic[el] / array.size) for el in dic]

    def initWorldSeed(self, seed):
        self.worldGenSeed = seed
        for el in self.parent:
            if el[1]:
                el[0].initWorldSeed(seed)
        self.worldGenSeed *= self.worldGenSeed * 6364136223846793005 + 1442695040888963407
        self.worldGenSeed += self.baseSeed
        self.worldGenSeed *= self.worldGenSeed * 6364136223846793005 + 1442695040888963407
        self.worldGenSeed = self.javaInt64(self.worldGenSeed)
        self.worldGenSeed += self.baseSeed
        self.worldGenSeed *= self.worldGenSeed * 6364136223846793005 + 1442695040888963407
        self.worldGenSeed += self.baseSeed
        self.worldGenSeed = self.javaInt64(self.worldGenSeed)

    def nextIntGen(self, limit):
        i = (self.chunkSeed >> 24) % limit
        if i < 0:
            i += limit
        self.chunkSeed *= (self.chunkSeed * 6364136223846793005 + 1442695040888963407)
        self.chunkSeed += self.worldGenSeed
        self.chunkSeed = self.javaInt64(self.chunkSeed)
        return i

    def selectRandom(self, l):
        return l[self.nextIntGen(len(l))]

    def genlayer(self, seed, customized):
        # customized hold 0 for normal, 1 for large and 2 for fully cuztomized, 4 for default1.1, then it holds biomeSize and river size then chunk composition

        # first stack from 1:4096 to 1:256
        initialLayer = g1.GenLayerIsland(1)
        firstLayer = g4.GenLayerZoom(2000, initialLayer, 1, 1, 1)
        secondLayer = g3.GenLayerAddIsland(1, firstLayer, 1)
        thirdLayer = g4.GenLayerZoom(2001, secondLayer, 0, 1, 1)
        genlayeraddisland1 = g3.GenLayerAddIsland(2, thirdLayer, 1)
        genlayeraddisland1 = g3.GenLayerAddIsland(50, genlayeraddisland1, 1)
        genlayeraddisland1 = g3.GenLayerAddIsland(70, genlayeraddisland1, 1)
        genlayerremovetoomuchocean = g5.GenLayerRemoveTooMuchOcean(2, genlayeraddisland1, 1)
        genlayeraddsnow = g6.GenLayerAddSnow(2, genlayerremovetoomuchocean, 1)
        genlayeraddisland2 = g3.GenLayerAddIsland(3, genlayeraddsnow, 1)
        genlayeredge = g7.GenLayerEdge(2, genlayeraddisland2, "COOL_WARM", 1)
        genlayeredge = g7.GenLayerEdge(2, genlayeredge, "HEAT_ICE", 1)
        genlayeredge = g7.GenLayerEdge(3, genlayeredge, "SPECIAL", 1)
        genlayerzoom1 = g4.GenLayerZoom(2002, genlayeredge, 0, 1, 1)
        genlayerzoom1 = g4.GenLayerZoom(2003, genlayerzoom1, 0, 1, 1)
        genlayeraddisland3 = g3.GenLayerAddIsland(4, genlayerzoom1, 1)
        genlayeraddmushroomisland = g8.GenLayerAddMushroomIsland(5, genlayeraddisland3, 1)
        genlayerdeepocean = g9.GenLayerDeepOcean(4, genlayeraddmushroomisland, 1)
        genlayerdeepocean.initWorldSeed(seed)
        lvt71 = deepcopy(genlayerdeepocean)
        # End first stack

        # choosing type of generation
        i, j = 4, 4
        if customized[0] == 2:
            i, j = customized[1], customized[2]
        if customized[0] == 1:
            i = 6
        # end of choice

        # starting biome stack
        lvt81 = g11.GenLayerBiome(200, genlayerdeepocean, customized, 0)  # 19
        genlayer6 = g4.GenLayerZoom.magnify(1000, lvt81, 2, 0, 1, 1)  # 20 and 21
        genlayerbiomeedge = g12.GenLayerBiomeEdge(1000, genlayer6, 1)  # 22
        # end Biome stack

        # starting river stack
        genlayerriverinit = g10.GenLayerRiverInit(100, lvt71, 0)  # 23
        lvt91 = g4.GenLayerZoom.magnify(1000, genlayerriverinit, 2, 0, 1, 0)  # 24 and 25
        # merge point
        # merging and starting hills/rare/shore/smooth chain
        genlayerhills = g13.GenLayerHills(1000, genlayerbiomeedge, lvt91, 1)
        genlayerhills = g16.GenLayerRareBiome(1001, genlayerhills, 1)
        for k in range(i):
            genlayerhills = g4.GenLayerZoom(1000 + k, genlayerhills, 0, 1, 1)
            if not k:
                genlayerhills = g3.GenLayerAddIsland(3, genlayerhills, 1)
            if k == 1 or i == 1:
                genlayerhills = g17.GenLayerShore(1000, genlayerhills, 1)
        genlayersmooth1 = g15.GenLayerSmooth(1000, genlayerhills, 1)
        # end of biome chain

        #finishing river
        genpreriver = g4.GenLayerZoom.magnify(1000, genlayerriverinit, 2, 0, 1, 1)
        genlayer5 = g4.GenLayerZoom.magnify(1000, genpreriver, j, 0, 1, 1)  # 37,38,39,40
        genlayerriver = g14.GenLayerRiver(1, genlayer5, 1)
        genlayersmooth = g15.GenLayerSmooth(1000, genlayerriver, 1)  # 42
        # end river

        # merging river with biome
        genlayerrivermix = g18.GenLayerRiverMix(100, genlayersmooth1, genlayersmooth, 1)
        # zooming
        genlayer3 = g19.GenLayerVoronoiZoom(10, genlayerrivermix, 1)
        # initializing
        genlayer3.initWorldSeed(seed)

        return [genlayerrivermix, genlayer3, genlayerrivermix][1]

    def isBiomeOceanic(self, biomeID):
        return biomeID in [24, 10, 0]

    def isValidId(self, id):
        x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
             29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 127, 129, 130, 131, 132, 133, 134, 140, 149, 151, 155, 156,
             157, 158, 160, 161, 162, 163, 164, 165, 166, 167]
        return id in x

    def sameClass(self, biomeA, biomeB):
        flag = False
        biomeClass = {"ocean": [0, 10, 24],
                      "plains": [1, 129],
                      "desert": [2, 17,  130],
                      "hills": [3, 20, 34, 131, 162],
                      "forest": [4, 18, 132, 157,27, 28, 29],
                      "taiga": [5, 19, 30, 31, 32, 33, 133, 158, 160, 161],
                      "swamp": [6, 134],
                      "river": [7, 11],
                      "hell": [8],
                      "end": [9],
                      "mushroom": [14, 15],
                      "mesa": [37, 38, 39],
                      "savanna": [35, 36],
                      "beach": [16, 26],
                      "stonebeach": [25],
                      "jungle": [21, 22, 23, 149, 151],
                      "savannaMutated": [163, 164],
                      "forestMutated": [155, 156],
                      "snow": [12, 13, 140],
                      "void": [127]}
        for el in biomeClass:
            if biomeB in biomeClass[el] and biomeA in biomeClass[el]:
                flag = True
        return flag

    def getTempCategory(self, biome):
        cold, medium, warm = 0, 1, 2
        if biome in [30, 158, 12, 140, 11, 26, 127, 10]:
            return cold  # below 0.2
        elif biome in [35, 163, 2, 130, 37, 165, 38, 166, 36, 39, 164, 167, 8, 17]:
            return warm  # above 1.0
        else:
            return medium

    def biomesEqualOrMesaPlateau(self, biomeA, biomeB):

        if biomeA == biomeB:
            return True
        else:
            if self.isValidId(biomeA) and self.isValidId(biomeB):
                if biomeA != 38 and biomeA != 39:  # mesa rock and clear rock
                    return biomeA == biomeB or self.sameClass(biomeA, biomeB)

                else:
                    return biomeB != 38 or biomeB != 39
            else:
                return False

    def isSnowy(self, id):
        return id in [10, 11, 12, 13, 26, 30, 31, 140, 158]

    def selectModeOrRandom(self, j, l, k, i):

        if (l == k and k == i):

            return l

        elif (j == l and j == k):

            return j

        elif (j == l and j == i):

            return j
        elif (j == k and j == i):

            return j

        elif (j == l and k != i):

            return j

        elif (j == k and l != i):

            return j

        elif (j == i and l != k):

            return j

        elif (l == k and j != i):

            return l

        elif (l == i and j != k):

            return l

        else:

            return k if k == i and j != l else self.selectRandom([j, l, k, i])


import GenLayerIsland as g1

import GenLayerAddIsland as g3
import GenLayerZoom as g4
import GenLayerRemoveTooMuchOcean as g5
import GenLayerAddSnow as g6
import GenLayerEdge as g7
import GenLayerAddMushroomIsland as g8
import GenLayerDeepOcean as g9
import GenLayerRiverInit as g10
import GenLayerBiome as g11
import GenLayerBiomeEdge as g12
import GenLayerHills as g13
import GenLayerRiver as g14
import GenLayerSmooth as g15
import GenLayerRareBiome as g16
import GenLayerShore as g17
import GenLayerRiverMix as g18
import GenLayerVoronoiZoom as g19
import time, timeit

def recursiveCall(layer,l,i):
    t=int(layer.getInts(l[i][1],l[i][2],1,1))
    print(t)
    if int(layer.getInts(l[i][1],l[i][2],1,1))==int(l[i][0]):
        print("e",i)
        if i==len(l)-1:
            return True
        return recursiveCall(layer,l,i+1)
    return False


def generate(seedmaj,data):
    coordinates,indice,seed,biome=data
    globalseed=seed|(seedmaj<<48)
    print(globalseed)
    customized=0 if biome==[4,4] else 1 if biome==[6,4] else 2

    c=[customized,biome[0],biome[1],""]
    print(c)
    m=Main()
    genlayerFinal = m.genlayer(globalseed, c)
    if recursiveCall(genlayerFinal,coordinates,indice):
        return globalseed
    return -1
