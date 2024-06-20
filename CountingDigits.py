def count_at_place(digit_to_count, limit, this_digit, this_place, base=10):
    lpv = base**this_place      # Larger of two relevant place values
    spv = base**(this_place-1)  # Smaller of two relevant place values
    until_target_digit = (limit // lpv) * spv
    if this_digit < digit_to_count:
        return until_target_digit
    elif this_digit > digit_to_count:
        return until_target_digit + spv
    else:
        return until_target_digit + (limit % spv) + 1

def count_by_digits(digit_to_count, limit, base=10):
    limit_digits = strbase(limit, base)
    length = len(limit_digits)
    counts_by_digit = [count_at_place(digit_to_count, limit, this_digit, length-i, base=base) for i, this_digit in enumerate(limit_digits)]
    return sum(counts_by_digit)

def strbase(n, b):
    # Convert a python numeric value n to a base b list of numeric values. E.g. convert 23 to [1, 11] for base b=12.
    return [n] if n < b else strbase(n // b, b) + [n % b]

def unbounded_binary_search(digit=1, base=10, safeleft=2, width=1):
    fn = lambda x: count_by_digits(digit, x, base=base)
    eq = None
    limit = digit * base**base
    while safeleft <= limit and eq is None:
        upper = safeleft + width
        fnsl = fn(safeleft)
        if eq is None and width == 1 and fn(upper) == upper:
            eq = upper
            safeleft, width = upper, 1
            continue
        if fnsl > safeleft + 1:
            # If fn(safeleft) is larger than safeleft, then even if none of the values
            # between safeleft and fn(safeleft) - 1 have the digit of interest,
            # fn(safeleft) will still remain larger, so we can skip ahead a bit.
            safeleft, width = fnsl - 1, 1
        elif width == 1 or fn(upper) < safeleft:
            safeleft, width = upper, width * 2
        else:
            safeleft, width = safeleft, width // 2
    return eq

s = 0

for digit in range(1,10):
    x = 0
    while x is not None:
        s += x
        x = unbounded_binary_search(digit=digit, safeleft=x)