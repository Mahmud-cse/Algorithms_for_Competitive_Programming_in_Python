#need to do iterative DFS, because recursive DFS cannot work in python for big graphs(number of recursive calls is limited)


def dfs_iterative(graph, start, seen):
	seen[start] = True
	to_visit = [start]
	while to_visit:
		node = to_visit.pop()
		for neighbor in graph[node]:
			if not seen[neighbor]:
				seen[neighbor] = True
				to_visit.append(neighbor)