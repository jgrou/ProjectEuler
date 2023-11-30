ans = 1
                
for n100 in range(3):
    for n50 in range(5):
        for n20 in range(11):
            for n10 in range(21):
                for n5 in range(41):
                    for n2 in range(101):
                        sums = 100 * n100 + 50 * n50 + 20 * n20 + 10 * n10 + 5 * n5 + 2 * n2
                        if sums <= 200:
                            ans += 1