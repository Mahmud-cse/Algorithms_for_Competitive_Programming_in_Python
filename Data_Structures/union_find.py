"""
Important to use path compression, that is the key to this data structure efficeincy
path compression is explained here:
https://www.youtube.com/watch?v=VHRhJWacxis&list=PLDV1Zeh2NRsB6SWUrDFW2RmDotAfPbeHu&index=22
In the implementation, it all happens in the find method
"""
class UnionFind:
    """
        up_bound[x] = root of the component x belongs to
        up_bound[v] == v only for root of a component
        at the begining, every node is the root of its own component
        rank[root] = the size of the component of root (minus 1)

    """
    def __init__(self, n):
        self.up_bound = list(range(n))
        self.rank = [0] * n

    def find(self, x_index):
        """
        returns the root of the component x_index belongs to
        """
        if self.up_bound[x_index] == x_index:
            return x_index
        #path compression happens with this recursive call
        self.up_bound[x_index] = self.find(self.up_bound[x_index])
        return self.up_bound[x_index]

    def union(self, x_index, y_index):
        repr_x = self.find(x_index)
        repr_y = self.find(y_index)
        if repr_x == repr_y:    # already in the same component
            return False
        if self.rank[repr_x] == self.rank[repr_y]:
            self.rank[repr_x] += 1
            self.up_bound[repr_y] = repr_x
        elif self.rank[repr_x] > self.rank[repr_y]:
            self.up_bound[repr_y] = repr_x
        else:
            self.up_bound[repr_x] = repr_y
        return True

#example use, find the number of connected components
#https://codeforces.com/problemset/problem/755/C
#solution: https://codeforces.com/contest/755/submission/103610901

#example drving code
n = 5
#we have a list aa
#and we know that for each i, aa[i] and i are connected (ie a path exists)
aa = [1,0,4,2,2]

uu = UnionFind(n)

#we start we each node in his own component
nb_components = n

for i in range(n):
    u = i
    v = aa[i]
    #regroup is True iff u and v are not in the same component yet
    regroup = uu.union(u, v)
    
    if regroup:
        nb_components -= 1
print(nb_components)

