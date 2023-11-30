LargestPalindromeProduct = 1
i = 1000

while i>100:
    j = 1000
    N = i*j
    while j>100 and N > LargestPalindromeProduct:
        N = i*j
        N_str = str(N)
        if N_str[::-1] == N_str: # Check if N is a palindrome
            LargestPalindromeProduct = N # If N is a palindrome, update largest palindrome product
        j-=1
    i-=1