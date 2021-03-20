from math import inf


def floyd_warshall():
    """
    assume we get a n*n matrix of weights (inf if not reachable)
    O(n^3)
    """
    d = [[inf]*n for i in range(n)]
    for i in range(n):
        d[i][i] = 0

    for i in range(n):
        for j in range(n):
            d[i][j] = min(d[i][j], weights[i][j])
 
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d


#driving code
n =ri()
weights = [[0]*n for i in range(n)]
for i in range(n):
    weights[i] = rl()
    for j in range(n):
        if weights[i][j] == "$": #assuming $ means not reachable, we cahnge it to
            weights[i][j] = inf
 
 
d =floyd_warshall()