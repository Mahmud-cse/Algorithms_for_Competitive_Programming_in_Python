from math import inf

def bellman_ford(s=0):
	"""
	you dont even need the adjacendcy list, just need the list of edges
	"""
    d = [inf] * n
    d[s] = 0
    parent = [-1]*n
    parent[s]=s
    for i in range(n-1):
        for e in edges:
            x,y, l =e
            if d[x] < inf and d[y] > d[x] + l:
                d[y] = d[x] + l
                parent[y] = x
    return d, parent



#driving code

n, m = rl()

edges = []
for i in range(m):
    x,y, l = rl()
    x,y = x-1, y-1
    # graph[x].append(y)
    # weight[x].append(l)
    edges.append((x,y, l))
 
d, parent = bellman_ford(0)
for i in range(1,n):
    if d[i] == inf:
        print("NO")
    else:
        print(d[i])


 #see https://codeforces.com/group/PMzrLJM5Tw/contest/319824/problem/A