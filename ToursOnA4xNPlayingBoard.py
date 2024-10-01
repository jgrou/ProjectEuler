# https://oeis.org/A181688
limit = 10**12

a_1 = 8
a_2 = 4
a_3 = 1
a_4 = 1

for _ in range(4, limit):
    a_1, a_2, a_3, a_4 = (2*a_1 + 2 * a_2 - 2 *a_3 + a_4) % 10**8, a_1, a_2, a_3
    
print(a_1)
