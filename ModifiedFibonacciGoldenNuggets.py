# The modified generating function is (x + 3 * x**2) / (x**2 + x - 1)
# This means 5*n**2 + 14*n + 1 should be perfect square

G = [1,4]

for n in range(1, 10000):
    square = 5*n**2 + 14*n + 1
    root = int(square**0.5)
    if root * root == square:
        print(n)
    G.append(G[n] + G[n-1])
    
# Generate Fibonacci sequence
F = [0,1,1]

for _ in range(100):
    F.append(F[-1] + F[-2])
    
A_G = [2,5]
dA_G = A_G[1] - A_G[0] # Difference between first and second AG
index = 7              # The accelerations are alternating Fibonacci numbers
ans = A_G[1] + A_G[0]

for i in range(28):
    dA_G += F[index]
    new_A_G = A_G[-1] + dA_G
    A_G.append(new_A_G)
    ans += new_A_G
    
    if i%2==0:
        index -= 2
    else:
        index += 6