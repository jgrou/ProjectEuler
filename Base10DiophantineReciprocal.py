#answers = [20, 102, 356, 958, 2192, 4456, 8260, 14088, 23058]
# This code is very slow!

def Solutions(n=1):
    ans = 0
    a_max = 2 * 10**n
    for a in range (1, a_max+1):
        p_min = 10**n // a # a*p > 10
        p_max = 2 * 10**n // a # b >= a, not the same as 2*p_min
        for p in range(p_min + 1, p_max + 1):
            b = (10**n * a) // (p * a - 10**n)
            if a * b * p == 10**n * (a + b):
                ans += 1
    return ans

for n in range(1,10):
    print(Solutions(n))