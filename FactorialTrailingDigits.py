from math import log

# multiply numbers from 1 to N
N = 10**12

# To compute the last 5 digits of product of all number from 1 to N, discarding trailing zeroes,
# we discard all the 2 and 5 factors, and add at the end some of the missing 2's
# (all 2's left and all 5's being put together to make discarded 10's)
# Then, as we will never divider by 10, we can only focus on the last digits,
#    which is to always take the modulo 10^5.
# only take 5 last significant numbers -> LIM is the modulo to perform.
# It is also the limit to precompute things, as we will be able to match
#   every number >= LIM to one number < LIM.
LIM = 10**5

# phi(n) is the product of all number Z<=n, with Z not a multiple of 2 or 5
# To compute that quickly, we pre-compute values from 1 to LIM.
phis = (LIM+1)*[0]
phis[0] = 1

i = 0
p = 1
while i < LIM:
  i += 1
  if (i%2 != 0) and (i%5 != 0):
    p *= i
    p %= LIM
  phis[i] = p

# Quickly now, even for big k, we can compute
#    product[1..k*LIM+m](Z) % LIM = (product[1..LIM](Z) ^ k) % LIM * product[1..m](Z).
# Why ? As (Z is not a multiple of 2 or 5) <=> (Z % LIM is not a multiple of 2 or 5),
# if "product[from..to](Z)" is the product of numbers which are no multiple of 2 or 5,
# we have product[1..m](Z)%LIM = product[1..m](Z%LIM)%LIM =
#    = product[LIM+1..LIM+m](Z%LIM)%LIM = product LIM+1..LIM+m](Z)%LIM
# Which means product[1..LIM](Z) % LIM = product[k*LIM+1 .. k*LIM+LIM](Z) % LIM, for each k-th slice.
def phi(n):
  k = n // LIM
  m = n % LIM
  a = phis[LIM]**k % LIM
  return (a * phis[m]) % LIM

# maximum powers of 2 and 5 which are in N
MAX2 = int(log(N,2))
MAX5 = int(log(N,5))

result = 1

# Each number is Z*2^p2*5^p5, with Z not a multiple of 2 or 5. We group numbers by p.
# So, for each number p which is 2^p2*5^p5, multiply result with
#   all number Z having Z*p<=N (Z only, as we discard 2's and 5's, which are in the 'p')
for p2 in range(0, MAX2 + 1):
    for p5 in range(0, MAX5 + 1):
        p = (2**p2) * (5**p5)
        if p > N:
           break
        result *= phi(N//p)
        result %= LIM

# Now, back to the forgotten 2's and 5's
# compute how much 2's factors are they from 1 to N
p2 = 0
k = N
while k > 0:
  k //= 2
  p2 += k

# compute how much 5's factors are they from 1 to N 
p5 = 0
k = N
while k > 0:
  k //= 5
  p5 += k

# how much 2's are left to multiply result, as we pair all 5's with 2's to make non-desired 10's.
p2 -= p5  # (p5 always > p2)

# now, get the result !
ans = result * pow(2, p2, LIM) % LIM