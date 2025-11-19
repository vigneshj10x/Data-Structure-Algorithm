def floyd_warshall(g):
    n=len(g)
    dist=[]
    for i in g:
        dist.append(i)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
    return dist

INF = 9999
graph = [
    [0,   4,   INF, 8],
    [INF, 0,   3,   INF],
    [INF, INF, 0,   7],
    [INF, INF, INF, 0]
]

result = floyd_warshall(graph)

for row in result:
    print(row)
