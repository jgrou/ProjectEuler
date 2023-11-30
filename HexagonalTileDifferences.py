def Hexagonal(ring, tile):
    '''
    ring: which ring, starting from inside and defining 1 as ring 0
    tile: which tile within the ring couting counterclockwise with 12 o'clock as tile 0
    returns number on the tile
    '''
    if ring == 0:
        return 1
    maxtile = 6 * ring - 1
    if tile == maxtile + 1:
        tile = 0
    elif tile == -1:
        tile = maxtile
    return 2 + 3 * ring * (ring - 1) + tile

def neighbours(ring, tile):
    outer = tile%ring + (ring+1) * (tile // ring) # Tile index of outer neighbour
    inner = tile%ring + (ring-1) * (tile // ring) # Tile index of inner neighour
    
    if tile%ring == 0: # Corner tiles with three outer tiles as neighbours
        return [Hexagonal(ring+1, outer-1),  Hexagonal(ring+1,outer),  Hexagonal(ring+1,outer+1), Hexagonal(ring-1,inner), Hexagonal(ring, tile-1), Hexagonal(ring, tile+1)]
    else:
        return [Hexagonal(ring+1, outer), Hexagonal(ring+1, outer+1), Hexagonal(ring-1,inner), Hexagonal(ring-1,inner-1), Hexagonal(ring, tile-1), Hexagonal(ring, tile+1)]
    
def IsPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    for p in range(3,int(n**0.5)+1,2):
        if n%p == 0:
            return False
    return True

ring = 1
lst = [1]

# Only chek corners of hexagon since difference with neigbours is same ring is 
# 1 which is not prime and difference between two outer or inner neighbours is 
# 1, so one of them is even 

while len(lst) < 2000:
    for t in range(6):
        m = Hexagonal(ring, t*ring)
        ListOfNeighbours = neighbours(ring, t*ring)
        PD = 0
        for neighbour in ListOfNeighbours:
            if IsPrime(abs(m - neighbour)):
                PD += 1
        if PD == 3:
            lst.append(m)
    
    t = 6 * ring - 1
    m = Hexagonal(ring, t)
    ListOfNeighbours = neighbours(ring, t)
    PD = 0
    for neighbour in ListOfNeighbours:
        if IsPrime(abs(m - neighbour)):
            PD += 1
    if PD == 3:
        lst.append(m)
        
    ring += 1