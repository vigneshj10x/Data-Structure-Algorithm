import itertools
def tsp_bruteforce(d):
    n=len(d)
    city=list(range(n))
    best_cost=float('inf')
    best_path=None
    for prem in itertools.permutations(city[1:]):
        path=[0]+list(prem)+[0]
        cost=0
        for i in range(len(path)-1):
            cost+=d[path[i]][path[i+1]]
        if cost<best_cost:
            best_cost=cost
            best_path=path
    return best_path,best_cost
D = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

print(tsp_bruteforce(D))