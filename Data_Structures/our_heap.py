"""
CAREFUL, THIS IMPLEMENTATION ONLY WORKS FOR HEAPS WITH ALL ELEMENTS DIFFERENT
"""
"""\
A min heap. We don't use the heapq module in Python, 
because in that module, you cannot modify
the values in the heaps. 
And that feature is usefull for Dijkstra algo implementation
(to improve time complexity)

christoph dürr et jill-jênn vie - 2015-2019
"""



class OurHeap:
    """ min heap
    * heap: is the actual heap, heap[1] = index of the smallest element
    * rank: inverse of heap with rank[x]=i iff heap[i]=x
    * n: size of the heap
    :complexity: init O(n log n), len O(1),
                other operations O(log n) in expectation
                and O(n) in worst case, due to the usage of a dictionary
    """
    def __init__(self, items):
        self.heap = [None]  # index 0 will be ignored
        self.rank = {}
        for x in items:
            self.push(x)

    def __len__(self):
        return len(self.heap) - 1

    def push(self, x):
        """Insert new element x in the heap.
           Assumption: x is not already in the heap"""
        assert x not in self.rank
        i = len(self.heap)
        self.heap.append(x)    # add a new leaf
        self.rank[x] = i
        self.up(i)             # maintain heap order

    def pop(self):
        """Remove and return smallest element"""
        root = self.heap[1]
        del self.rank[root]
        x = self.heap.pop()    # remove last leaf
        if self:               # if heap is not empty
            self.heap[1] = x    # move the last leaf
            self.rank[x] = 1    # to the root
            self.down(1)        # maintain heap order
        return root
 


    def up(self, i):
        """The value of heap[i] has decreased. Maintain heap invariant."""
        x = self.heap[i]
        while i > 1 and x < self.heap[i // 2]:
            self.heap[i] = self.heap[i // 2]
            self.rank[self.heap[i // 2]] = i
            i //= 2
        self.heap[i] = x       # insertion index found
        self.rank[x] = i

    def down(self, i):
        """the value of heap[i] has increased. Maintain heap invariant."""
        x = self.heap[i]
        n = len(self.heap)
        while True:
            left = 2 * i       # climb down the tree
            right = left + 1
            if (right < n and self.heap[right] < x and
                    self.heap[right] < self.heap[left]):
                self.heap[i] = self.heap[right]
                self.rank[self.heap[right]] = i   # move right child up
                i = right
            elif left < n and self.heap[left] < x:
                self.heap[i] = self.heap[left]
                self.rank[self.heap[left]] = i    # move left child up
                i = left
            else:
                self.heap[i] = x   # insertion index found
                self.rank[x] = i
                return

    def update(self, old, new):
        """Replace an element in the heap
        """
        i = self.rank[old]     # change value at index i
        del self.rank[old]
        self.heap[i] = new
        self.rank[new] = i
        if old < new:          # maintain heap order
            self.down(i)
        else:
            self.up(i)

    #I added a remove method
    def remove(self, val):
        #do nothing if val is not in the heap
        if val not in self.rank:
            return
        #val is the only element in the heap
        if len(self.heap) == 1:
            self.pop()
        elif val == self.heap[-1]:
            x = self.heap.pop()
            del self.rank[x]
        else:
            #remove the last leaf
            x = self.heap.pop()
            del self.rank[x]
            #put back the last leaf inplace of val
            self.update(val, x)




#example
#https://www.hackerrank.com/challenges/qheap1/problem
#solution:

Q = int(input())
hh = OurHeap([])

for q in range(Q):
    line = input()
    #insert a value
    if line[0] == "1":
        val = int(line.split()[1])
        hh.push(val)
    #remove a value
    if line[0] == "2":
        val = int(line.split()[1])
        hh.remove(val)
    #print the minimum of the heap, it is hh.heap[1]
    if line[0] == "3":
        print(hh.heap[1])

