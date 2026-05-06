limit = 16
ans = 0

for a_plus_b in range(4, 10**(limit//2)):
    square = a_plus_b**2
    s = str(square)

    for split in range(1, len(s)):
        if s[split] == '0':
            continue
        a = int(s[:split])
        b = int(s[split:])
        if a + b == a_plus_b:
            ans += square

print(ans)