def CountAtPlace(digit, limit, this_digit, this_place, base=10):
    lpv = base**this_place      # Larger of two relevant place values
    spv = base**(this_place-1)  # Smaller of two relevant place values
    until_target_digit = (limit // lpv) * spv
    
    if this_digit < digit:
        return until_target_digit
    elif this_digit > digit:
        return until_target_digit + spv
    else:
        return until_target_digit + (limit % spv) + 1

def CountByDigits(digit, limit, base=10):
    limit_digits = strbase(limit, base)
    length = len(limit_digits)
    counts = [CountAtPlace(digit, limit, this_digit, length-i, base=base) for i, this_digit in enumerate(limit_digits)]
    return sum(counts)

def strbase(n, b):
    # Convert a python numeric value n to a base b list of numeric values
    if n < b:
        return [n] 
    else:
        return strbase(n // b, b) + [n % b]

def UnboundedBinarySearch(digit=1, base=10, safeleft=2, width=1):
    eq = None
    limit = digit * base**base
    
    while safeleft <= limit and eq is None:
        upper = safeleft + width
        fnsl = CountByDigits(digit, safeleft, base=base)
        
        if eq is None and width == 1 and CountByDigits(digit, upper, base=base) == upper:
            eq = upper
            safeleft, width = upper, 1
            continue
        if fnsl > safeleft + 1:
            # If fn(safeleft) is larger than safeleft, then even if none of the values
            # between safeleft and fn(safeleft) - 1 have the digit of interest,
            # fn(safeleft) will still remain larger, so we can skip ahead a bit.
            safeleft, width = fnsl - 1, 1
        elif width == 1 or CountByDigits(digit, upper, base=base) < safeleft:
            safeleft, width = upper, width * 2
        else:
            safeleft, width = safeleft, width // 2
    return eq

s = 0

for digit in range(1,10):
    x = 0
    while x is not None:
        s += x
        x = UnboundedBinarySearch(digit=digit, safeleft=x)