"""
We use DFS here to count the connected components
There is another method using union find, see the example in Data_Structures/union_find.py
"""


from collections import *
"""
It is a little bit heavy, need 2 functions
and the function dfs have a lot of arguments
usually it is nicer to implement with just one function
like here:
https://codeforces.com/contest/755/submission/103528552
"""

def dfs(start, visited, current):
	visited[start] = current
	to_visit = [start]
	while to_visit:
		node = to_visit.pop()
		for child in graph[node]:
			if not visited[child]:
				visited[child] = current
				to_visit.append(child)

def count_components():
	"""
	visited is a list, it can have many values:
	0 -> node unvisited
	k -> node belong to the connected component number k
	""" 
	n = len(graph)
	visited = [0]*n
	nb_components = 0
	for v in range(n):
		if not visited[v]:
			nb_components += 1
			dfs(v, visited, nb_components)

#example use:
#https://codeforces.com/problemset/problem/755/C
#solution: https://codeforces.com/contest/755/submission/103529674
#solution: with one fucntion, not 2:
#https://codeforces.com/contest/755/submission/103528552
