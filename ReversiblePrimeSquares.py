limit = 100000000

IsPrime = (limit + 1) * [True]

for p in range(2, int(limit**0.5)+1):
    if IsPrime[p]:
        for k in range(p**2, limit+1, p):
            IsPrime[k] = False
            
PrimeSquares = [i**2 for i in range(2,limit+1) if IsPrime[i]]
PrimeSquares_set= set(PrimeSquares)
ReversiblePrimeSquare = set()

for PrimeSquare in PrimeSquares:
    reverse = int(str(PrimeSquare)[::-1])
    if reverse == PrimeSquare:
        continue
    if reverse in PrimeSquares_set:
        ReversiblePrimeSquare.add(reverse)
        ReversiblePrimeSquare.add(PrimeSquare)
        
ans = sum(ReversiblePrimeSquare) # This are by chance 50 numbers