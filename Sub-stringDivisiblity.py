def CheckProperty(n):
    if int(n[1:4]) % 2 != 0:
        return False
    if int(n[2:5]) % 3 != 0:
        return False
    if int(n[3:6]) % 5 != 0:
        return False
    if int(n[4:7]) % 7 != 0:
        return False
    if int(n[5:8]) % 11 != 0:
        return False
    if int(n[6:9]) % 13 != 0:
        return False
    if int(n[7:10]) % 17 != 0:
        return False
    return True

ans = 0
digits = [str(d9) for d9 in range(10)]

for d1 in digits[1:]:
    for d2 in digits:
        if d2 not in d1:
            for d3 in digits:
                if d3 not in d1+d2:
                    for d4 in digits:
                        if d4 not in d1+d2+d3:
                            for d5 in digits:
                                if d5 not in d1+d2+d3+d4:
                                    for d6 in digits:
                                        if d6 not in d1+d2+d3+d4+d5:
                                            for d7 in digits:
                                                if d7 not in d1+d2+d3+d4+d5+d6:
                                                    for d8 in digits:
                                                        if d8 not in d1+d2+d3+d4+d5+d6+d7:
                                                            for d9 in digits:
                                                                if d9 not in d1+d2+d3+d4+d5+d6+d7+d8:
                                                                    for d10 in digits:
                                                                        if d10 not in d1+d2+d3+d4+d5+d6+d7+d8+d9:
                                                                            number = d1+d2+d3+d4+d5+d6+d7+d8+d9+d10
                                                                            if CheckProperty(number):
                                                                                ans += int(number)