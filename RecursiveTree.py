# Children of parent are n-2**k, for k = 0,1,...
# Then the largest child (n-1) has children (n-1) - 2**k for k =1,2,..
# And the second largest child (n-2) has children (n-2) - 2**k for k=2,3,,
# etc.
# Then for the children of the children:
# If difference between parent and node is 2**m, then it has children node - 2**(m+1), node - 2**(m+2), etc.

def f(n, k):
    ans = n
    current_number = n

    for depth, i in enumerate(bin(n - k)[-1:1:-1]): # Iterate over binary digits backwards
        if i == '1':
            current_number -= 2**depth
            ans += current_number

    return ans

print(f(10**17, 9**17))