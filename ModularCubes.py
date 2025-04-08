from sympy.ntheory.residue_ntheory import crt

def factorint(n):
    # Prime factorization: {p1: e1, p2: e2, ...}
    factors = {}
    if n%2 == 0:
        exp = 0
        while n%2 == 0:
            n //= 2
            exp += 1
        factors[2] = exp

    p = 3
    while p**2 <= n:
        if n%p == 0:
            exp = 0
            while n%p == 0:
                n //= p
                exp += 1
            factors[p] = exp
        p += 2

    if n > 1:
        factors[n] = 1
    return factors

def cube_roots_mod_prime(p):
    roots = []
    for x in range(1, p):
        if pow(x, 3, p) == 1:
            roots.append(x)
    return roots

def cube_roots_mod_n(n):
    factors = factorint(n)    
    mod_roots = []

    # Find cube roots modulo each prime factor
    for p, e in factors.items():
        mod = p**e
        roots = cube_roots_mod_prime(mod)
        mod_roots.append((roots, mod))

    # Use CRT to combine combinations of roots
    from itertools import product
    res = 0

    all_root_combinations = product(*[roots for roots, _ in mod_roots])
    moduli = [mod for _, mod in mod_roots]

    for combo in all_root_combinations:
        x, _ = crt(moduli, combo)
        res += (int(x % n))  # Ensure within mod n

    return res-1

ans = cube_roots_mod_n(13082761331670030)
print(ans)
