# If there is 2 or 5 involved: we only need to check the last number
# Would there be other possibilities?

def IsPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n & 1 == 0:
        return False
    for k in range(3, int(n**0.5)+1, 2):
        if n%k == 0:
            return False
    return True

# We can have 4 * p**3, 25 * p**3, 8 * p**2, 125 * p**3

n = 1 # 200 is the first
p = 7
Prime_proofSqube = [200]
maximum = 10**100

while n < 200 or p < (maximum/8)**0.5:
    if IsPrime(p):
        for k in [4*p**3, 25*p**3, 8*p**2, 125*p**2]:
            if k > maximum:
                continue
            if '200' not in str(k):
                continue
            prime_proof = True
            for final_digit in ['1','3','7','9']: # Prime ends in this
                new_k = int(str(k)[:-1] + final_digit)
                if IsPrime(new_k):
                    prime_proof = False
                    break
            if prime_proof:
                Prime_proofSqube.append(k)
                n += 1
                if n == 200:
                    maximum = max(Prime_proofSqube)
                elif n>200:
                    Prime_proofSqube.sort()
                    maximum = Prime_proofSqube[199]
    p += 1
    
Prime_proofSqube.sort()
ans = Prime_proofSqube[199]