matrix1 = [
    [11, 9, 2],
    [8, -133, 27],
    [40, 6, -5],
]
matrix2 = [
    [11, 91, -42],
    [28, 53, 27],
    [401, 6, -5],
]

result = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix2))]

print("Resultant Matrix:")
for row in result:
    print(row)