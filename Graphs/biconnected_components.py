#see https://www.youtube.com/watch?v=iYJqgMKYsdI
from collections import defaultdict as dd
from collections import deque
import bisect
import heapq
from math import inf

import os
import sys
from io import BytesIO, IOBase

BUFSIZE = 8192

class FastIO(IOBase):
    newlines = 0
 
    def __init__(self, file):
        import os
        self.os = os
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
 
    def read(self):
        while True:
            b = self.os.read(self._fd, max(self.os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
 
    def readline(self):
        while self.newlines == 0:
            b = self.os.read(self._fd, max(self.os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
 
    def flush(self):
        if self.writable:
            self.os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)
 
 
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")
 
 
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")



def ri():
    return int(input())
 
def rl():
    return list(map(int, input().split()))
"""
see https://www.youtube.com/watch?v=iYJqgMKYsdI
"""

def dfs(u, p, i):

    """
    returns the fup value (-1 if not visited before = forward edge)
    u is the vertex
    p the parent
    i the index of the edge (p,u)
    """
    global cnt

    if not used[i]:
        used[i] = True
        stack.append(i)


    #backedge
    if tin[u] != -1:
        fup[p] = min(fup[p], tin[u])
        return fup[p]

    #forward edge

    #update tin value
    tin[u] = cnt
    cnt += 1
    fup[u] = tin[u]

    hasFwd = False

    for v,j in graph[u]:
        if j == i:
            continue
        if dfs(v,u,j) < 0:
            fup[u] = min(fup[u], fup[v])

            #bridge condition
            if fup[v] == tin[v]:
                bridges.append(j)

            if (u != p and fup[v] >= tin[u]) or (u==p and hasFwd):
                art[u] = True
                makeComp(j).append(stack.pop())

            hasFwd = True

    return -1

def makeComp(i):
    comp = []
    while stack[-1] != i:
        comp.append(stack.pop())

    comps.append(comp)

    return comp



def solve():
    global graph, tin, fup, bridges, art, cnt, stack, used, comps
    n, m =rl()
    graph =[[] for i in range(n)]
    edges = []
    for i in range(m):
        u,v = rl()
        u,v = u-1,v-1
        graph[u].append((v,i)) # include the id of the edge
        graph[v].append((u,i))
        edges.append((u,v))

    tin = [-1]*n #tin is also used as visited array, so we dont need a visited array
    fup = [-1]*n
    cnt = 1
    bridges = []
    art = [False]*n #is articulation point or not
    stack =[]
    used = [False]*(m+1) #visited array, but for edges, not vertices
    comps =[]

    for i in range(n):
        if tin[i] == -1:
            used[m] = False #dummy edge
            dfs(i, i, m)
            if stack:
                makeComp(m)
            stack = []
    # print("bridges: ",[(edges[i][0] + 1,edges[i][1] + 1) for i in bridges])
    # print("articulation: ", art)
    if m == 0:
        print(0)
    else:
        print(len(comps))
        for comp in comps:
            print(len(comp))
            for e in comp:
                u, v = edges[e]
                print(u+1,v+1)





import threading
sys.setrecursionlimit(3*10**5)
threading.stack_size(8*10**7)
t = threading.Thread(target=solve)
t.start()
t.join()
 
