n = 1001

NumberOfSpirals = (n + 1) / 2
ans = 1 # Start with the first spiral

for i in range(2,int(NumberOfSpirals)+1):
    StartingValue = (2*(i-2)+1)**2 + 1
    ans += StartingValue + 2*(i-2)+1 # Add lower left diagonal
    ans += StartingValue + 2*(i-2)+1 + 2*(i-1)# Add lower right diagonal
    ans += StartingValue + 2*(i-2)+1 + 4*(i-1)# Add upper right diagonal
    ans += StartingValue + 2*(i-2)+1 + 6*(i-1)# Add upper left diagonal