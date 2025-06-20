# https://oeis.org/A011779
limit = 12345

def T(n):
    return n*(n+1) // 2

def H(n):
    # Suppose I start at some point on the bottom of the triangle:
    # I walk x times left and y times left diagonally upward with y<=x
    # Then the hexagon returns from y times right and x times right diagonally upward.
    # Necessary size of the triangle:
    # (1,0): 3
    # (1,1): 6
    # (2,0): 6
    # (2,1): 9
    # (2,2): 12
    # (3,1): 12
    # (3,2): 15
    # Seems like 3*(x+y)
    # If x!=y and x!=0: we can mirror the image to obtain another one.
    res = 0
    x_max = n//3

    for x in range(1, x_max+1):
        for y in range(x+1):
            smallest_triangle = 3*(x+y)
            if smallest_triangle > n:
                break
            if y == 0 or y == x:
                res += T(n + 1 - smallest_triangle)
            else:
                res += 2 * T(n + 1 - smallest_triangle)
        
    return res

def sH(n):
    # For n divisible by 3 this works
    res = 0
    for k in range(1, n//3 + 1):
        m = T(k)
        for i in range(n-1-3*k, n+2-3*k):
            res += m * T(i)
    return res

ans = sH(limit)
print(ans)
