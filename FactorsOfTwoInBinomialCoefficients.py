# https://oeis.org/A119387
# a(n) is the number of binary digits (1's and nonleading 0's) which remain unchanged in their positions when n and (n+1) are written in binary.
# The last digit always changes
# The second-last digit only changes if the last digit was 1
# the third-last-digit chagnes if the last two were both 1
# etc.
# For all 1's: all digits change

# There is 1 number with 1 digit
# There are 4-2=2 numbers with 2 digits:
## For those 1 ends in 1
# There are 4 numbers with 3 digits:
## Of those 2 end in 1
## And 1 ends in 11

limit = 10**16

def S(n):
    max_power = n.bit_length()
    total_digits = 0
    changed_digits = 0

    for power in range(1, max_power):
        total_digits += power * 2**(power-1)
        changed_digits += (n+1) // 2**(power-1) - 1

    # Now for the rest
    total_digits += max_power * (n - 2**(max_power-1) + 1)
    changed_digits += (n+1) // 2**(max_power-1) - 1

    return total_digits - changed_digits

print(S(limit))