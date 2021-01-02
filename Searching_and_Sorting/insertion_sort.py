
import sys
import bisect
from collections import deque
input =sys.stdin.readline


def insertion_sort(aa):
    n = len(aa)
    for j in range(1,n):
        key = aa[j]
        i = j - 1
        while i >= 0  and aa[i] > key:
            aa[i + 1] = aa[i]
            i -= 1
        aa[i + 1] = key

def insertion_sort_with_libraries(aa):
    qq = deque(aa[1:])
    result = [aa[0]]
    while qq:
        popped = qq.popleft()
        bisect.insort(result, popped)
    return result



aa = [1, 5, 8, 4, 9, 15, 16, 5, 55, 1, 2]
print("Direct algo:")
print(aa)
insertion_sort(aa)
print(aa)

aa = [1, 5, 8, 4, 9, 15, 16, 5, 55, 1, 2]
print("Using libraries(faster because of binary search):")
print(aa)
print(insertion_sort_with_libraries(aa))







