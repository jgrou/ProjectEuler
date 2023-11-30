N1_9 = len('one') + len('two') + len('three') + len('four') + len('five') + len('six') + len('seven') + len('eight') + len('nine')
N10_19 = len('ten') + len('eleven') + len('twelve') + len('thirteen') + len('fourteen') + len('fifteen') + len('sixteen') + len('seventeen') + len('eighteen') + len('nineteen')
N1_99 = 10 * (len('twenty') + len('thirty') + len('forty') + len('fifty') + len('sixty') + len('seventy') + len('eighty') + len('ninety')) + 9 * N1_9 + N10_19
N1_999 = 100 * N1_9 + 900 * len('hundred') + 891 * len('and') + 10 * N1_99
N1_1000 = len('one') + len('thousand') + N1_999