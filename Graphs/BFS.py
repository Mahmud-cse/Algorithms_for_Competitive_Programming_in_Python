from collections import deque
from math import inf

def bfs(graph, start = 0):
	"""
		:param graph: directed graph in listlist or listdict format
		:param int start: source vertex
		:returns: nothing, but you can modify it, see other function below
	"""
	n = len(graph)
	visited = [False] * n
	visited[start] = True
	to_visit = deque()
	to_visit.append(start)
	while to_visit:
		node = to_visit.popleft()
		for neighbor in graph[node]:
			if not visited[neighbor]:
				visited[neighbor] = True
				to_visit.append(neighbor)


#main advantage of dfs is to calculate distance to starting node

def bfs_dist(graph, start = 0):
    """Shortest path in unweighted graph by BFS
       :param graph: directed graph in listlist or listdict format
       :param int start: source vertex
       :returns: distance table, precedence table
       :complexity: `O(|V|+|E|)`
       """
    to_visit = deque()
    dist = [inf] * len(graph)
    prec = [None] * len(graph)
    dist[start] = 0
    to_visit.appendleft(start)
    while to_visit:              # an empty queue is considered False
        node = to_visit.pop()
        for neighbor in graph[node]:
            if dist[neighbor] == inf:
                dist[neighbor] = dist[node] + 1
                prec[neighbor] = node
                to_visit.appendleft(neighbor)
    return dist, prec




#example of use:
#https://codeforces.com/problemset/problem/115/A