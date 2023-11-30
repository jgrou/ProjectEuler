C = {}
N_max = 21768             # Empirically this is enough
L_max = int(N_max/4)      # Maximal L, first cover is at least 4 L

for l in range(1,L_max+1):
    w_max = min( int( (N_max-2*l) / (2*(l+1)) ), l )
    for w in range(1,w_max+1):
        h_max = min( int( (N_max-2*l*w) / (2*(l+w)) ), w)
        for h in range(1,w+1):
            # minimum number of cubes to cover
            old_layer = l*w # Size of first layer
            cubes = []
            n = 1
            new_layer = old_layer + 2*(l+w) + (n-1)*4
            cover = (2-h)*old_layer + h * new_layer
            while cover <= N_max:
                cubes.append(cover)
                old_layer = new_layer
                n += 1
                
                new_layer = old_layer + 2*(l+w) + (n-1)*4
                cover = (2-h)*old_layer + h * new_layer

            # increase number of cuboids by 1 for every n
            for n in cubes:
                try:
                    C[n] += 1
                    if C[n] == 1000:
                        print(n)
                except KeyError:
                    C[n] = 1
      
lst = []
for key, value in C.items():
    if value == 1000:
        lst.append(key)

ans = min(lst)