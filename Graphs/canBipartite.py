from collections import deque

def canBipartite(adj_list, n):
    """
        vertices are numbered from 0 , 1 ...to n - 1
        Return a tuple (True, coloring) if we can color the n vertices with 2 colors, 
        given than vertices on both sides of an edge must have different colors.
        We use BFS for that
    """
    visited = [0] * n

    queue = deque()

    #loop through all the vertices
    for start in range(n):

        #####everyhting after this could be put in a separate function if we wanted to#####

        #visited is also used to track the 2 colors, 1 and -1
        if not visited[start]:
            queue.append(start)
            visited[start] = 1 #here we could also assign -1 to the starting vertex of this connected component, doesnt matter 


        while queue:
            u = queue.popleft() 

            # Return false if there is a self-loop 
            if u in adj_list[u]: 
                return False, []

            for v in (adj_list[u]): 
                if not visited[v]: 

                    # Assign alternate number to this adjacent v of u 
                    visited[v] = -visited[u] 
                    queue.append(v) 

                elif visited[v] == visited[u]: 
                    return False, []

    return True, visited

#example use

n = 3
adj_list = [[1,2],[0,2],[0]]
print(canBipartite(adj_list, n))

n = 4
adj_list = [[1],[0],[3],[2]]
print(canBipartite(adj_list, n))

#example of problem to solve with that:
#https://www.spoj.com/problems/BUGLIFE/

#https://codeforces.com/contest/445/problem/A
#solution: https://codeforces.com/contest/445/submission/103170939