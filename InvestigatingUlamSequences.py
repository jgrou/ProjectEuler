def ulam(terms, old_arr=[1,2]):
    '''compute first terms of ulam sequence starting with old_arr'''
    arr = terms * [None] # Array to store Ulam Numbers 
    s = set() # Set to search specific Ulam number efficiently 

    # Copy all the terms we already computed to the new array
    for i,u in enumerate(old_arr):
        arr[i] = u
        s.add(u)
    
    term = len(old_arr)
    i = arr[term-1] + 1
    
	# loop to generate Ulam number 
    while term < terms: 
        count = 0

		# traverse the array and check if i can be represented as sum of two distinct element of the array 
        for j in range(term):
			# Check if i-arr[j] exist in the array using set. If yes, then i can be represented as arr[j]+(i-arr[j]) 
            if (i - arr[j]) in s and arr[j] != (i - arr[j]): 
                count += 1
            if count > 2: # if Count is greater than 2 break the loop 
                break
           
        # if count is 2 that means i can be represented as sum of two distinct terms of the sequence 
        if count == 2:
			# i is ulam number 
            arr[term] = i 
            s.add(i) 
            term += 1
        i += 1
    return arr
		
# When v is an odd number greater than 3, the differences between consecutive (2,v)-Ulam numbers is eventually periodic
def Ulam(start_array=[1,2], limit=100): # Try in the first limit terms if there is a pattern
    U = ulam(limit, start_array) 

    for periodicity in range(1, limit):
        diff = [U[i+periodicity] - U[i] for i in range(limit - periodicity)]
        start = limit - periodicity # See where the periodicity starts
        # For n > start, a(n+periodicity) = a(n) + diff[-1]
        while diff[start-1] == diff[-1]:
            start -= 1
            if start == -1:
                return Ulam(U, 2*limit) # If limit is not enough try again with double terms
        if start < limit - 10 - periodicity: # If the last 10 differences are the same, we assume periodcity
            print(periodicity)
            print(diff[-1])
            
            remainder = k % periodicity
            if remainder <= start:
                init = U[remainder+periodicity]
            else:
                init = U[remainder]
            return init + k // periodicity * diff[-1]
        
k = 10**11
ans = 0

for n in range(2,11): # n=9 takes too long! limit at least 2**10 * 100
    ans += Ulam([2, 2*n+1])