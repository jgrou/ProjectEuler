largest = 0
digits = [str(i) for i in range(1,10)]

for integer in range(10**4): # If larger than sum of the concatenated product with (1,2) would always have 10 numbers
    ConcatenatedProduct = str(integer)
    n = 2
    
    while len(ConcatenatedProduct) < 9:
        ConcatenatedProduct += str(n*integer)
        if len(ConcatenatedProduct) == 9:
            pandigital = True
            for i in digits:
                if i not in ConcatenatedProduct:
                    pandigital = False
                    break
                
            if pandigital and int(ConcatenatedProduct) > largest:
                largest = int(ConcatenatedProduct)
                
        n += 1