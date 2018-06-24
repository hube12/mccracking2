import functools, time, itertools, multiprocessing, multiprocessing.pool, sys
from psutil import virtual_memory

class NoDaemonProcess(multiprocessing.Process):
    def _get_daemon(self):
        return False

    def _set_daemon(self, value):
        pass

    daemon = property(_get_daemon, _set_daemon)


class MyPool(multiprocessing.pool.Pool):
    Process = NoDaemonProcess


def next(seed):
    seed = (seed * 0x5deece66d + 0xb) & ((1 << 48) - 1)
    retval = seed >> (48 - 31)
    if retval & (1 << 31):
        retval -= (1 << 32)
    return retval, seed

def nextInt(n, seed, count, flag):
    l = []
    if flag:
        seed = (seed ^ 0x5deece66d) & ((1 << 48) - 1)
    for i in range(count):
        retval, seed = next(seed)
        if not (n & (n - 1)):
            l.append((n * retval) >> 31)
        else:
            bits = retval
            val = bits % n

            while (bits - val + n - 1) < 0:
                bits, seed = next(seed)
                val = bits % n
            l.append(val)
    return l, seed

def shuffle(l, seed):
    for i in range(len(l), 1, -1):
        j, seed = nextInt(i, seed, 1, i == len(l))
        l[i - 1], l[j[0]] = l[j[0]], l[i - 1]
    return l

def get_all_possible_end_pillar_configuration_fast(seed, currentPillar):
    interval, i, flag = shuffle(list(range(10)), seed), 0, True
    while i < 10 and flag:
        if (76 + interval[i] * 3) != currentPillar[i]:
            flag = False
        i += 1
    return seed if flag else -1

def goBack(seed, pillar):
    currentSeed = (seed << 16 & 0xFFFF00000000) | (pillar << 16) | (seed & 0xFFFF)
    currentSeed = ((currentSeed - 0xb) * 0xdfe05bcb1365) & 0xffffffffffff
    currentSeed = ((currentSeed - 0xb) * 0xdfe05bcb1365) & 0xffffffffffff
    currentSeed ^= 0x5DEECE66D
    return currentSeed

def canSpawnStruct(params):
    seed, pillar, indice = params
    global liste
    chunkX, chunkZ, incompleteRand, modulus, typeStruct = liste[indice]
    currentSeed = goBack(seed, pillar)+incompleteRand
    if typeStruct == "s":
        l = nextInt(24, currentSeed, 2, True)[0]
        k, m = l[0], l[1]
    elif typeStruct == "e":
        l = nextInt(9, currentSeed, 4, True)[0]
        k, m = (l[0] + l[1]) // 2, (l[2] + l[3]) // 2
    elif typeStruct == "o":
        l = nextInt(27, currentSeed, 4, True)[0]
        k, m = (l[0] + l[1]) // 2, (l[2] + l[3]) // 2
    else:
        l = nextInt(60, currentSeed, 4, True)[0]
        k, m = (l[0] + l[1]) // 2, (l[2] + l[3]) // 2
    if chunkX % modulus == k and m == chunkZ % modulus:
        if indice > 4:
            print(
                    "In case you want to shut down, copy this number somewhere: it is likely to be a good one" + currentSeed)
        if indice == len(liste) - 1:
            return currentSeed
        return canSpawnStruct((seed, pillar, indice + 1))
    else:
        return -1

def data(structureType):
    t = structureType.lower()
    if t == "m":
        uniquifier,modulus = "10387319",80
    elif t == "e" :
        uniquifier,modulus  = "10387313",20
    elif t == "o":
        uniquifier,modulus  = "10387313",32
    elif t=='v':
        uniquifier, modulus = "10387312", 32
    else:
        uniquifier,modulus  = "14357617",32
    return uniquifier,modulus

def test(chunkX, chunkZ, uniquifier, seed, modulus, typeStruct):


    currentSeed = (chunkX) // modulus * 341873128712 + (chunkZ) // modulus * 132897987541 + seed + uniquifier

    if typeStruct == "s" or typeStruct=="v":
        l = nextInt(24, currentSeed, 2, True)[0]
        k, m = l[0], l[1]
    elif typeStruct == "e":
        l = nextInt(9, currentSeed, 4, True)[0]
        k, m = (l[0] + l[1]) // 2, (l[2] + l[3]) // 2
    elif typeStruct == "o":
        l = nextInt(27, currentSeed, 4, True)[0]
        k, m = (l[0] + l[1]) // 2, (l[2] + l[3]) // 2
    else:
        l = nextInt(60, currentSeed, 4, True)[0]
        k, m = (l[0] + l[1]) // 2, (l[2] + l[3]) // 2
    if chunkX % modulus == k and m == chunkZ % modulus:
        #print(str(seed)+ " is ok with that structure")
        return True
    #print("Not correct")
    return False

def getdata(*args):
    global liste
    liste = [x for x in args]

def convert(data):
    l = []
    for e in data:
        uniquifier, modulus = e[0].split(",")
        if uniquifier == "10387319":
            t = "m"
        elif uniquifier == "10387313" and modulus == 20:
            t = "e"
        elif uniquifier == "10387313":
            t = "o"
        else:
            t = "s"
        l.append((e[1], e[2], e[1] // modulus * 341873128712 + e[2] // modulus * 132897987541 + int(uniquifier), int(modulus), t))

    return l
def ram():
    return virtual_memory().total/1024/1024//4

def main(datapack, ram, core, ok):
    dataPillar = datapack[0]
    data = datapack[1]
    coordinates=datapack[2]
    biome=datapack[3]
    if sys.platform.startswith('win'):
        multiprocessing.freeze_support()
    towerTime = time.time()
    with MyPool(processes=None) as pool:  # get processes from os.cpu_count()
        couple = functools.partial(get_all_possible_end_pillar_configuration_fast,
                                   currentPillar=dataPillar)
        results = pool.map(couple, range(65536))
        towerNumber = [p for p in results if p != -1]
    print("Looking for the tower number took: " + time.time() - towerTime)
    print("The EndPillarSeed found is: " + towerNumber)
    data = convert(data)
    print("You can look one last time at your data before i make confetti of it: " + data)
    if not ok:
        ram=ram()

    if ram > 6000:
        mem = 26
    elif ram > 2000:
        mem = 25
    elif ram > 500:
        mem = 23
    else:
        mem = 22
    print(ram,mem)
    fullResults = []
    chunksize = 1 << mem
    for roll in range(2 ** (32 - mem)):
        t = time.time()
        with MyPool(processes=core if ok else None, initializer=getdata, initargs=data) as pool:
            paramlist = itertools.product(range(chunksize * roll, chunksize * (roll + 1)), towerNumber, [0])
            results = pool.imap_unordered(canSpawnEndCity, paramlist, 1000)
            fullResults.extend([p for p in results if p != -1])
        flagContinue=True
        if not roll:
            tempo = time.time() - t
            print("First roll took: " + tempo + " expected time for the whole thing " + (2 ** (32 - mem)) * tempo / 60 + " min")

        if len(fullResults):
            print(fullResults)
            print("i have found one or more possible structure seeds, would you be kind to provide me another structure before i continue so i can reduce computation time? Y/N")
            response=input().lower()
            if response in ["no","n","0","nope","i will not",'ney',"nah","uh-uh","non","nix","nay","no way","negative","go fish"]:
                print("Beginning layer calculation, gonna take a while...")
            else:
                print("Enter chunkX,chunkZ")
                chunkX, chunkZ = map(int, input().split(","))
                print( "Enter Structure Type: o for ocean monument, e for end cities, m for mansion, v for village, s for all the rest (witch hut, igloo, desert temple, jungle temple)")
                structureType = input()
                while not(structureType in ["m","e","s","o","v"]):
                    print(
                        "Are you kidding me? Enter Structure Type: o for ocean monument, e for end cities, m for mansion, v for village, s for all the rest (witch hut, igloo, desert temple, jungle temple) only")
                    structureType = input()
                uniquifier,modulus=data(structureType)
                for seeds in fullResults:
                    if not test(chunkX,chunkZ,uniquifier,seeds,modulus,typeStruct):
                        print("i eliminated a Seed, well done ",seeds)
                        fullResults.remove(seeds)
                if not len(fullResults):
                    print("Too bad, i cant pin down for now, i will catch you later")
                    flagContinue=False
            if flagContinue:
                with MyPool(processes=core if ok else None, initializer=getdata, initargs=data) as pool:
                    couple = functools.partial(generate, data=[coordinates, 0, seed, biome])
                    results = pool.imap_unordered(couple, range((1 << 16) - 1), 1000)
                    # in generate seed|iter<<48 seed=data[2]

    print(fullResults)

if __name__ == '__main__':
    main()

""" Memory usage
power of 2 | usage in MB
    16          5
    17          10
    18          20
    18          40
    20          80
    21          162
    22          324
    23          648
    24          1296
    25          2593
    26          5200
    27          10400  
    28          21000
"""
