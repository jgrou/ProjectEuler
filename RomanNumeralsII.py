def RomanToArabic(n):
    res = 0
    i = 0
    
    while i < len(n):
        if n[i] == 'M':
            res += 1000
        elif n[i] == 'D':
            res += 500
        elif n[i] == 'C':
            if i+1 < len(n):
                if n[i+1] == 'D':
                    res += 400
                    i += 1
                elif n[i+1] == 'M':
                    res += 900
                    i += 1
                else:
                    res += 100
            else:
                res += 100
        elif n[i] == 'L':
            res += 50
        elif n[i] == 'X':
            if i+1 < len(n):
                if n[i+1] == 'C':
                    res += 90
                    i += 1
                elif n[i+1] == 'L':
                    res += 40
                    i += 1
                else:
                    res += 10
            else:
                res += 10
        elif n[i] == 'V':
            res += 5
        else:
            if i+1 < len(n):
                if n[i+1] == 'V':
                    res += 4
                    i += 1
                elif n[i+1] == 'X':
                    res += 9
                    i += 1
                else:
                    res += 1
            else:
                res += 1
        i += 1
    return res

def RomanNumeral(number, p, length):
    possibilities = {'I', 'V', 'X', 'L', 'C', 'D', 'M'}

    # Cannot draw I
    if length > 1 and number[-2:] in {'IX','IV'}:
        possibilities.remove('I')
    elif length > 2 and number[-3:] =='III':
        possibilities.remove('I')
    
    # Cannot draw V or X
    if 'V' in number:
        possibilities.remove('V')
        possibilities.remove('X')
    elif length > 1 and number[-2:] in {'IX', 'II'}:
        possibilities.remove('V')
        possibilities.remove('X')
        
    # Cannot draw X
    elif length > 1 and number[-2:] in {'XL', 'XC'}:
        possibilities.remove('X')
    elif length > 2 and number[-3:] =='XXX':
        possibilities.remove('X')
        
    # Cannot draw L or C
    if any(c in number for c in 'IVL'):
        possibilities.remove('L')
        possibilities.remove('C')
    elif length > 1 and number[-2:] in {'XC', 'XX'}:
        possibilities.remove('L')
        possibilities.remove('C')
    
    # Cannot draw C
    elif length > 1 and number[-2:] in {'CD', 'CM'}:
        possibilities.remove('C')
    elif length > 2 and number[-3:] =='CCC':
        possibilities.remove('C')
    
    # Cannot draw D or M
    if any(c in number for c in 'IVLXD'):
        possibilities.remove('D')
        possibilities.remove('M')
    elif length > 1 and number[-2:] in {'CM', 'CC'}:
        possibilities.remove('D')
        possibilities.remove('M')
   
    # Probability that I return to my current state is 0.98 - #possibilities * 0.14
    # Then by geometric series we have to multiply with p_loop
    p_loop = 1/(0.02 + len(possibilities) * 0.14) 
    
    for letter in possibilities:
        RomanNumeral(number+letter, p_loop*0.14*p, length+1)
    
    n = RomanToArabic(number)
    if len(possibilities) == 0:
        P[n] = p
        return
    else:
        P[n] = 0.02 * p * p_loop

P = {0: 0.02} # Dictionary of all values 0,1,...,999 with their probability
RomanNumeral('I', 0.14, 1)
RomanNumeral('V', 0.14, 1)
RomanNumeral('X', 0.14, 1)
RomanNumeral('L', 0.14, 1)
RomanNumeral('C', 0.14, 1)
RomanNumeral('D', 0.14, 1)

ans = 0
for key,value in P.items():
    for M in range(15):
        ans += value * (key + M * 1000) * 0.14**M

print(round(ans,8))