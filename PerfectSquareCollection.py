import math

L_max = 10_000 # Emprical high enough bound
m_max = int(0.5 * ((1 + 2 * L_max)**0.5 - 1)) # a = m^2 - n^2, b = 2 mn, c = m^2 + n^2, m>n
triplets = {}

# Find all pythorean triplets untill L_max
for m in range(1, m_max + 1):
    n_max = min(int(L_max / (2 * m) - m), m - 1)
    if m%2 == 1: # m,n not both odd
        for n in range(2, n_max + 1, 2):
            if math.gcd(m, n) == 1:
                a = m**2 - n**2
                b = 2 * m * n
                c = m**2 + n**2 
                for i in range(1, int(L_max/(a+b+c))): # Also add multiples of a,b,c
                    try:
                        triplets[a*i].append([a*i,b*i,c*i])
                    except KeyError:
                        triplets[a*i] = [[a*i,b*i,c*i]]
                
                    try:
                        triplets[b*i].append([a*i,b*i,c*i])
                    except KeyError:
                        triplets[b*i] = [[a*i,b*i,c*i]]

    else:
        for n in range(1, n_max + 1):
            if math.gcd(m, n) == 1:
                a = m**2 - n**2
                b = 2 * m * n
                c = m**2 + n**2
                for i in range(1, int(L_max/(a+b+c))):
                    try:
                        triplets[a*i].append([a*i,b*i,c*i])
                    except KeyError:
                        triplets[a*i] = [[a*i,b*i,c*i]]
                
                    try:
                        triplets[b*i].append([a*i,b*i,c*i])
                    except KeyError:
                        triplets[b*i] = [[a*i,b*i,c*i]]

# Only look at triplets which have multiple solutions
new_triplets = {}

for key, value in triplets.items():
    if len(value) > 1:
        new_triplets[key] = value
 
def main():
    for a, value in new_triplets.items():  # a**2=x-y, b**2=y-z and c**2=x-z have to form a Pythagorean triplet   
        for triple in value: 
            # Select other item in triplet which is not a
            for item in triple[:2]:
                if item != a:
                    b = item
                    break
            try:        
                b_lst = new_triplets[b] # y-z has to be in two Pythagorean triplets
            except KeyError:
                continue
        
            for lb in b_lst:
                if lb != triple: #y-z, x+z and x+y also have to form a Pythagorean triplet
            
                    # Select item in lb which is not b: x+z
                    for item in lb[:2]:
                        if item != b:
                            e1 = item
                            break
                    
                    f = lb[2] #x+y
                
                    for la in value:
                        if la != triple: #x-y, y+z and x+z also have to form a Pythagorean triplet
                    
                            # Select item in la which is not a: y+z
                            for item in la[:2]:
                                if item != a:
                                    d = item
                                    break
                                
                            e2 = la[2] # x+z
                            
                            if e1 == e2: # In both triplets x+z has to occur
                                ans = (e1**2 + d**2 + f**2) / 2 # (x+y+z) = (x+z + y+z + z+y)/2
                                if int(ans) == ans:
                                    return ans
                            if f == d:
                                ans = (e1**2 + e2**2 + d**2) / 2 # (x+y+z) = (x+z + y+z + z+y)/2
                                if int(ans) == ans:
                                    return ans

answer = main()