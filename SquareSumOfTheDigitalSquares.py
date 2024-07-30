import itertools

squares = [i**2 for i in range(10)]
limit = 20
NoOfDigits = 9
ans = 0

# Yield all permutations of size NoOfDigits when there are doubles
def YieldAllPermutations(s, NoOfDigits): 
    
    def YieldAllPermutationsFast(s, l):
        if len(s) < TotalDigits + 1 - NoOfDigits:
            yield l, s
        else:
            uset = set()
     
            for i in range(len(s)):
                if s[i] in uset:
                    continue
                else:
                    uset.add(s[i])
         
                temp = ""
                if (i < len(s) - 1):
                    temp = s[:i] + s[i + 1:]
                else:
                    temp = s[:i]
         
                yield from YieldAllPermutationsFast(temp, l + s[i])
                
    TotalDigits = len(s)
    yield from YieldAllPermutationsFast(s, '')

#Python code for the above approach
class Solution:
	def __init__(self):
		self.temp = []

	def solve(self, a, v, idx, s, n):
		# first base case if sum=n we can store vector in a
		# vector
		if s == n:
			v.append(self.temp.copy())
			return

		# if idx < 0 return
		if idx < 0:
			return

		# not take condition
		self.solve(a, v, idx-1, s, n)
		if s < n:
			self.temp.append(a[idx])
			# this is main condition where we can take one
			# element many times
			self.solve(a, v, idx, s+a[idx], n)
			self.temp.pop()

	def UniquePartitions(self, n):
		a = [i for i in range(1, n+1)]
		v = []
		# call solve to get answer
		self.solve(a, v, n-1, 0, n)
		v.reverse()
		return v

sol = Solution()
dic = {}
UniquePartitions = sol.UniquePartitions(11)
for partition in UniquePartitions:
    string = ''
    for i, n in enumerate(partition):
        string += n*str(i)
    if len(string) <= 11:
        dic[tuple(partition)] = sum(1 for _ in YieldAllPermutations(string, len(string)))

def NumberOfCombinations(string):
    '''For a given set of digits, the number of different permutations we can make only depends on the number of 
    occurences, independent of the value of the digit. So we first make a dicitionary for each permutation and then
    we can precompute all values'''
    partition = []
    
    for digit in range(10):
        occurs = string.count(str(digit))
        if occurs > 0:
            partition.append(occurs)
    partition.sort(reverse=True)
    return dic[tuple(partition)]

for combination in itertools.combinations_with_replacement(squares, limit):
    s = sum(combination)
    if int(s**0.5)**2 == s:
        digits = ''.join(map(str,[int(x**0.5) for x in combination]))
        for permutation, rest in YieldAllPermutations(digits,9): # Only need last nine digits
            ans += NumberOfCombinations(rest) * int(permutation)
            ans %= 10**9