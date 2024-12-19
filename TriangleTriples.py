class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)
        self.size = size

    def update(self, index, delta):
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index

    def query(self, index):
        sum_ = 0
        while index > 0:
            sum_ += self.tree[index]
            index -= index & -index
        return sum_

def count_decreasing_triplets(nums):
    n = len(nums)
    
    # Coordinate compression
    sorted_nums = sorted(set(nums))
    rank = {v: i + 1 for i, v in enumerate(sorted_nums)}  # Map value to rank (1-based index)
    compressed = [rank[num] for num in nums]
    max_rank = len(sorted_nums)

    # Fenwick Tree for greater_left
    greater_left = [0] * n
    fenwick_left = FenwickTree(max_rank)
    for i in range(n):
        # Count elements greater on the left
        greater_left[i] = fenwick_left.query(max_rank) - fenwick_left.query(compressed[i])
        # Update Fenwick Tree with the current element
        fenwick_left.update(compressed[i], 1)

    # Fenwick Tree for smaller_right
    smaller_right = [0] * n
    fenwick_right = FenwickTree(max_rank)
    for i in range(n - 1, -1, -1):
        # Count elements smaller on the right
        smaller_right[i] = fenwick_right.query(compressed[i] - 1)
        # Update Fenwick Tree with the current element
        fenwick_right.update(compressed[i], 1)

    # Calculate total triplets
    count = 0
    for i in range(n):
        count += greater_left[i] * smaller_right[i]
    return count

limit = 60_000_000
PrimeFactorization = [{} for n in range(limit+2)]
IsPrime = (limit + 2) * [True]

for p in range(2, limit+2):
    if IsPrime[p]:
        for k in range(p**2, limit+2, p):
            IsPrime[k] = False
        power = 1
        while p**power <= limit+2:
            for k in range(p**power, limit+2, p**power):
                if p in PrimeFactorization[k]:
                    PrimeFactorization[k][p] += 1
                else:
                    PrimeFactorization[k][p] = 1
            power+=1

ans = 0
dT = (limit+1)*[None]
dT[1] = 1

for k in range(2,limit+1):
    res = 1
    for key in PrimeFactorization[k].keys() | PrimeFactorization[k+1].keys():
        # Safely retrieve the value for the key from dict, or 0 if the key is not present.
        value = PrimeFactorization[k].get(key,0) + PrimeFactorization[k+1].get(key,0) 
        if key == 2:
            value -= 1
        res *= (value+1)
    dT[k] = res

ans = count_decreasing_triplets(dT[1:])
print(ans%10**18)