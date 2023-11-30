day = 366  # start on Monday + 365
sundays = 0
DaysPerMonth = [31,28,31,30,31,30,31,31,30,31,30,31]
LeapYear     = [31,29,31,30,31,30,31,31,30,31,30,31]

for year in range(1901, 2001):
    if year%4==0:
        for month in LeapYear:
            day += month
            if day%7==0:
                sundays += 1
    else:
        for month in DaysPerMonth:
            day += month
            if day % 7 == 0:
                sundays +=1