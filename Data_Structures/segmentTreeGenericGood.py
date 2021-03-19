
#https://codeforces.com/contest/1473/submission/104303028

#best explanation ever
# https://codeforces.com/blog/entry/44478

class SegmentTree:
    def __init__(self, init_val, segfunc, ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        res = self.ide_ele

        l += self.num
        r += self.num
        left = []
        right = []
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                right.append(self.tree[r - 1])
            l >>= 1
            r >>= 1

        for i in range(len(right)-1,-1,-1):
            res = self.segfunc(res,right[i])
        return res

def merge(a,b):
    new_max = max(a[0],b[0]+a[2])
    new_min = min(a[1],b[1]+a[2])
    new_last = a[2] + b[2]
    return (new_max,new_min,new_last)

ide_ele = (0,0,0)

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n,m = map(int,input().split())
    s = input().rstrip()
    init = [0]*n
    for i in range(n):
        if s[i]=="+":
            init[i] = (1,0,1)
        else:
            init[i] = (0,-1,-1)

    braket = SegmentTree(init,merge,ide_ele)
    ans = []
    for i in range(m):
        l,r = map(int,input().split())
        tmp_1 = braket.query(0,l-1)
        tmp_2 = braket.query(r,n)
        Max,Min,last = merge(tmp_1,tmp_2)
        ans.append(Max-Min+1)
    print(*ans,sep="\n")