import math

limit = 10**17
F = [1,2]
ans = 0
  
while F[-1] < limit:
    F.append(F[-2] + F[-1])

F.pop() # Do not need last element

i = 0

while len(F) > 1:
    # This gives the answer for limit = F[-1] + F[-2] - 1
    N = len(F) - 1
    max_terms = (N+1)//2
    for n_terms in range(1, max_terms+1):
        ans += (n_terms + i) * math.comb(N-n_terms+1,n_terms)

    ans += i   # Add F[-1] + F[-2]
    limit -= F[-1]  # Compute the remainder

    
    while (F[-1] > limit) and (len(F)>1):
        F.pop()
    i += 1

print(ans)  
