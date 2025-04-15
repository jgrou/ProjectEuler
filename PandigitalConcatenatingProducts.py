import itertools

def Pandigital(x):
    for i in range(10):
        if str(i) not in x:
            return False
    return True

def partition(current, n, max_i):
    if n == 0:
        partitions.append(current)
    for i in range(1, min(max_i,n)+1):
        partition(current+(i,), n-i, i)

partitions = []
partition(tuple(), 8, 7)

# First try fist integer having 1 digit: 9 * [1, 87345026] = 9786105234
ans = 9786105234
# Then try two digits: finds the solution

for k in range(98,9,-1):
    d1 = k//10
    d2 = k % 10
    if d1 == d2:
        continue
    rest = set(range(10))
    rest.remove(d1)
    rest.remove(d2)
    for perm in itertools.permutations(rest):
        if perm[0] == 0: # No leading 0's
            continue
        for part in partitions:
            stop = False
            guess = []
            start = 0
            for i in part:
                if perm[start] == 0: # No leading 0's
                    stop = True
                    break
                guess.append(k * int(''.join(str(x) for x in perm[start:start+i])))
                start += i
                
            if stop: # No leading 0's
                continue
                
            guess.sort(reverse=True) # Largest digits first
            guess_str = ''.join(str(i) for i in guess)
            total = int(guess_str)
            
            if total > ans and total < 10**10:
                if Pandigital(guess_str):
                    ans = total
                    print(k, perm,part,total)
