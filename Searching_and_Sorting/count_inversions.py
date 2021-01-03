#!/usr/bin/env python
import os, sys

def mergeSortInversions(arr):
    """
        input: list
        output: tuple (sorted list, number of inversions)
        Merge sort already count inversions.
        So we use exactly merge sort, and we keep track of inversions during merge sort
        running time: O(n log n)
    """
    if len(arr) == 1:
        return arr, 0
    else:
        a = arr[:len(arr)//2]
        b = arr[len(arr)//2:]        

        a, ai = mergeSortInversions(a)
        b, bi = mergeSortInversions(b)
        c = []        

        i = 0
        j = 0
        inversions = 0 + ai + bi    

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
            inversions += (len(a)-i)    

    c += a[i:]
    c += b[j:]

    return c, inversions

#example use:

aa = [1,2,4,3,6,5]
print("initial list:", aa)
sorted_list, inversions = mergeSortInversions(aa)
print("sorted list:", sorted_list)
print("num inversions:",inversions)