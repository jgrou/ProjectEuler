triangle = []

with open('triangle.txt') as f:
    for line in f:
        row = [int(num) for num in line.strip().split()]
        triangle.append(row)  # Splitting the line into words
        
# Start from the second-last row and move upwards
for i in range(len(triangle) - 2, -1, -1):
    for j in range(i + 1):
        # Add the maximum of the two adjacent numbers below
        triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])
    
# The maximum sum will be at the top of the triangle
ans = triangle[0][0]