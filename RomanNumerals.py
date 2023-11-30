roman = []

with open('roman.txt') as f:
    for line in f:
        roman.append(line)
        
initial = sum(len(numeral) for numeral in roman)

def rewrite(numeral):
    temp = numeral.replace('LXXXX', 'XC')
    temp = temp.replace('XXXX', 'XL')
    
    temp = temp.replace('DCCCC', 'CM')
    temp = temp.replace('CCCC', 'CD')
    
    temp = temp.replace('VIIII', 'IX')
    temp = temp.replace('IIII', 'IV')
    return temp
    
minimal = [rewrite(numeral) for numeral in roman]
new = sum(len(numeral) for numeral in minimal)
saved = initial - new