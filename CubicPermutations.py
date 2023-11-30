def are_permutations(num1, num2):
    # Convert numbers to strings
    str1 = str(num1)
    str2 = str(num2)

    # Check if the lengths are equal
    if len(str1) != len(str2):
        return False

    # Create dictionaries to count digit occurrences
    count1 = {}
    count2 = {}

    # Count occurrences of digits in the first number
    for digit in str1:
        count1[digit] = count1.get(digit, 0) + 1

    # Count occurrences of digits in the second number
    for digit in str2:
        count2[digit] = count2.get(digit, 0) + 1

    # Compare the digit counts
    return count1 == count2

cubes = []
n = 1
count = 0

while count < 5:
    cube = n**3    
    cube_str = str(cube)
    count = 1
    permuted_cube = []
    
    for x in cubes:
        if are_permutations(cube, x):
            permuted_cube.append(x)
            count += 1
            if count == 5:
                print(permuted_cube)
                break
    
    cubes.append(cube)
    n += 1