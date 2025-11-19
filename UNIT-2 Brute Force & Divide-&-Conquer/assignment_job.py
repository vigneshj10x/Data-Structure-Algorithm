import itertools
def assignment_bruteforce(c):
    n=len(c)
    job=list(range(n))
    best_cost=float('inf')
    best_assignment=None
    for prem in itertools.permutations(job):
        total=0
        for i in range(n):
            total +=c[i][prem[i]]
        if total<best_cost:
            best_cost=total
            best_assignment=prem
    return best_assignment, best_cost



cost_matrix = [
    [9, 2, 7],
    [6, 4, 3],
    [5, 8, 1]
]

assignment, minimum_cost = assignment_bruteforce(cost_matrix)

print("Cost Matrix:")
for row in cost_matrix:
    print(row)

print("\nBest Assignment (worker → job):", assignment)
print("Minimum Total Cost:", minimum_cost)