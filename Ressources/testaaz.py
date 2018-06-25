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
def datas(structureType):
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

u,m=datas("e")
print(test(-16,63,u,))