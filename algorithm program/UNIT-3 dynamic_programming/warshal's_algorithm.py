def warshall(m):
    n=len(m)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                m[i][j]=m[i][j] or (m[i][k] and m[k][j])
    return m
matrix = [
    [1,0,0,1],
    [0,1,1,0],
    [0,1,1,0],
    [1,0,0,1]
]
result = warshall(matrix)

for row in result:
    print(row)
