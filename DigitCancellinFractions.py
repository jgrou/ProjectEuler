lst = []

for den in range(10,100):
    for num in range(10,den): # Smaller than 1
        if den%10 != 0 and num%10 != 0:
            for i in range(2):
                for j in range(2):
                    if str(num)[i] == str(den)[j]:
                        if int(str(num)[i-1]) / int(str(den)[j-1]) == num / den:
                            lst.append(str(num)+'/'+str(den))