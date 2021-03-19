
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

def dfs(i):
    global result

    to_visit = deque()
    to_visit.append(i)

    while to_visit:
        node = to_visit.popleft()
        for child in graph[node]:
            if dist[child] == inf:
                dist[child] = 1 + dist[node]
                parent[child] = node
                to_visit.append(child)

            elif parent[node] != child and parent[child] != node:
                result = min(result, dist[node] + dist[child] + 1)

    return result


first = True
count = inf
cases = 0
all_inputs = []
for line in sys.stdin:
    all_inputs.append(line)
    if first:
        n,m = list(map(int, line.split()))
        count = m
        cases += 1
        first = False
    elif count != 0:
        count -= 1
        

    else: # count ==0 and first ==False
        
        n,m = list(map(int, line.split()))
        first = False
        count = m
        cases += 1
idx = 0
for t in range(cases):
    line  = all_inputs[idx]
    idx += 1

    n,m =list(map(int, line.split()))

    graph = [[] for i in range(n)]
    edges = []
    for i in range(m):
        line  = all_inputs[idx]
        idx += 1
        u,v = list(map(int, line.split()))
        u, v = u-1, v-1
        edges.append((u,v))
        graph[u].append(v)
        graph[v].append(u)

    result = inf
    for i in range(n):
        dist = [inf]*n
        parent = [-1] * n
        dist[i] = 0
        result = min(result, dfs(i))
    if result == inf:
        result = -1
    print(result)
    