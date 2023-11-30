def CountRectangles(length, height):
    temp = 0
    for i in range(1, height + 1):
        for j in range(1, length + 1):
            temp += (height + 1 - i) * (length + 1 - j)
    return temp

length = 3
min_diff = 2_000_000

while True:
    for heigth in range(length):
        NoOfRectangles = CountRectangles(length, heigth)
        diff = abs(2_000_000 - NoOfRectangles)
        if diff < min_diff:
            min_diff = diff
            ans = heigth * length
        if NoOfRectangles > 2_000_000:
            break
    if heigth == 1:
        break
    length += 1