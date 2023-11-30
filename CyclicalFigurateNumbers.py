import itertools

triangle = []
square = []
pentagonal =[]
hexagonal = []
heptagonal = []
octagonal = []
n = 1
tri = 0

while tri < 10000:
    
    tri = int(n*(n+1)/2)
    if 1000 < tri < 10000:
        triangle.append(tri)
    
    sq = n**2
    if 1000 < sq < 10000:    
        square.append(sq)
    
    pen = int(n*(3*n-1)/2)
    if 1000 < pen < 10000:
        pentagonal.append(pen)
    
    hexa = int(n*(2*n-1))
    if 1000 < hexa < 10000:
        hexagonal.append(hexa)
    
    hep = int(n*(5*n-3)/2)
    if 1000 < hep < 10000:
        heptagonal.append(hep)
    
    octa = int(n*(3*n-2))
    if 1000 < octa < 10000:
        octagonal.append(octa)
    n += 1
    
orderings = list(itertools.permutations([square, pentagonal, hexagonal, heptagonal, octagonal], 5))

def main():
    for i in range(len(orderings)):
        v,w,x,y,z = orderings[i]
        
        for tri in triangle:
            for sq in v:
                if str(tri)[2:] == str(sq)[:2]:
                    for pen in w:
                        if str(sq)[2:] == str(pen)[:2]:
                            for hexa in x:
                                if str(pen)[2:] == str(hexa)[:2]:
                                    for hep in y:
                                        if str(hexa)[2:] == str(hep)[:2]:
                                            for octa in z:
                                                if str(hep)[2:] == str(octa)[:2] and str(octa)[2:] == str(tri)[:2]:
                                                    print(tri,sq,pen,hexa,hep,octa)
                                                    return tri + sq + pen + hexa + hep + octa
                                                
ans = main()