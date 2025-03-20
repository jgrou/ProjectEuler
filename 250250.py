import math

# To be divisible by 250, we only need to look at the last three digits
limit = 250250
MOD = 250
List = MOD * [0]

for i in range(1, limit+1):
    LastThreeDigits = pow(i,i,MOD)
    List[LastThreeDigits] += 1
  
# Heavy calculcation: do beforehand. There are few possible value
Comb = {}

for count in set(List):
    lst = (count + 1) * [None]
    for k in range(count//2 + 1):
         pos = math.comb(count, k) % 10**16
         lst[k] = pos
         lst[count-k] = pos
    Comb[count] = lst

# Initialize DP table: dp[s] = number of ways to get sum ≡ s (mod 250)
dp = [0] * MOD
dp[0] = 1  # Base case: one way to form sum 0 (empty set)
    
for num, count in enumerate(List):
    # Create a temporary dp array to update state without interfering with current state
    new_dp = dp[:]
        
    for s in range(MOD):
        if dp[s] > 0:
            # Try adding the number `num` from 1 up to `count` times
            for k in range(1, count + 1):
                new_sum = (s + k * num) % MOD
                # How many different ways to pick k out of count
                new_dp[new_sum] += dp[s] * Comb[count][k]
                new_dp[new_sum] %= 10**16  # Only interested in final 16 digits
                
    # Update dp to the new state after considering current number
    dp = new_dp
    
# Return the number of valid combinations summing to a multiple of 250
result = dp[0] - 1  # Subtract 1 to exclude the empty set
print(result)
