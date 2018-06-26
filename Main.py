import os,ast,sys,multiprocessing
import numpy as np
from collections import Counter
from copy import deepcopy
import functools, time, itertools, multiprocessing, multiprocessing.pool, sys, os
from psutil import virtual_memory
import cracker2 as c
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

import genLayer as gL

def main():
    try:
        text=open("data.txt","r")
    except:
        l=os.listdir()
        for el in l:
            if el[0:4]=="data" and el[len(el)-4:len(el)]==".txt":
                text=open(el,"r")
    dataPack=ast.literal_eval(text.readline())
    ram=int(text.readline())
    core=int(text.readline())
    ok=ast.literal_eval(text.readline())
    c.main(dataPack,ram,core,ok)



if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()