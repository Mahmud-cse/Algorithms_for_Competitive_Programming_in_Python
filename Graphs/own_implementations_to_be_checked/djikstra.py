import heapq
from math import inf


"""
both implementations assume we have defined the graph like that:

    graph = [[] for i in range(n)]
    for i in range(m):
        a,b,w = rl()
        a,b = a-1, b-1
        graph[a].append((b,w))
        graph[b].append((a,w))
        

"""


def djikstra(s=0):
    """
    O(n^2): good to use that implementation is number of edges is big (m= n^2 for example)

    Assume you have defined a graph like that:

        graph = [[] for i in range(n)]
        for i in range(m):
            a,b,w = rl()
            a,b = a-1, b-1
            graph[a].append((b,w))
            graph[b].append((a,w))
        
    example use:
    https://codeforces.com/group/PMzrLJM5Tw/contest/319824/problem/B
    """
    d = [inf]*n
    d[s] = 0
    p = [-1]*n
    p[s] =s
    visited = [False]*n
    while True:
        u = -1
        for i in range(n):
            if not visited[i] and (u ==-1 or d[u] > d[i]):
                u = i
        if u == -1 or d[u] == inf:
            break
        visited[u] = True
        for T in graph[u]:
            v, l = T
            if d[v] > d[u] + l:
                d[v] = d[u] + l
                p[v] = u
                d[v] = d[u] + l
    return d, p


def djikstra_heap(s=0):
	"""
    O((n+m)log(n))  (if m = n^2, better not to use heap, use other implementation)

	Assume you have defined a graph like that:
    
    	graph = [[] for i in range(n)]
    	for i in range(m):
        	a,b,w = rl()
        	a,b = a-1, b-1
        	graph[a].append((b,w))
        	graph[b].append((a,w))
    	
    example use:
    https://codeforces.com/group/PMzrLJM5Tw/contest/319824/problem/L


	"""
    parent = [None] * n
    visited = [False] * n
    dist = [inf] * n
    dist[s] = 0
    heap = [(0, s)]
    while heap:
        d, u = heapq.heappop(heap)       
        if not visited[u]:
            visited[u] = True
            for v,w in graph[u]:
                if d + w < dist[v]:
                    dist[v] = d + w
                    parent[v] = u
                    heapq.heappush(heap, (dist[v], v))
    return dist, parent