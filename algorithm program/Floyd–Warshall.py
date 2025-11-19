def floyd_warshall(d):
    n=len(d)
    dp=[]
    for i in d:
        row=i[:]
        dp.append(row)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dp[i][k]+dp[k][j]<dp[i][j]:
                    dp[i][j]=dp[i][k]+dp[k][j]
    return dp




INF = 10**9
graph = [
    [0,   5,  INF, 10],
    [INF, 0,   3,  INF],
    [INF, INF, 0,   1],
    [INF, INF, INF, 0]
]

result = floyd_warshall(graph)
for i in result:
    print(i)