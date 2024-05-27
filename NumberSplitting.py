from itertools import permutations
import math

def partitions(n):
    unique_partitions = set()
    _partitions(n, n, [], unique_partitions)
    # The roots of numbers with 2n digits needs can only be made with a number of n digits
    # The roots of numbers with 2n+1 digits can be made with numbers of n and n+1 digits
    unique_partitions = {x for x in unique_partitions if max(x) >= math.floor(n/2) and max(x) <= math.ceil(n/2)}
    
    all_partitions = []
    for partition in unique_partitions:
        # Generate all unique permutations of the partition
        for perm in set(permutations(partition)):
            all_partitions.append(perm)
            
    return all_partitions

def _partitions(n, max_val, current_partition, unique_partitions):
    if n == 0:
        # Convert the partition to a tuple so it can be added to a set
        unique_partitions.add(tuple(current_partition))
        return

    for i in range(min(n, max_val), 0, -1):
        _partitions(n - i, i, current_partition + [i], unique_partitions)
   
dic = {}

for k in range(1,13):
    dic[k] = partitions(k)

def SNumber(n):
    square = n**2
    NoOfDigits = int(math.log10(square)) + 1
    string = str(square)
    
    for part in dic[NoOfDigits]:
        number = 0
        index = 0
        for i in part:
            number += int(string[index:index+i])
            index += i
        if number == n:
            return True
    return False

ans = 0

for k in range(4,100000): # Numbers need to split in two of more numbers so, square should be at least 10
    if SNumber(k):
        print(k)
        ans += k**2

ans += 10**12