#!/usr/bin/env python
#explanations: https://medium.com/@ssbothwell/counting-inversions-with-merge-sort-4d9910dc95f0

def mergeSort(arr):
    if len(arr) == 1:
        return arr
    else:
        a = arr[:len(arr)//2]
        b = arr[len(arr)//2:]        

        a = mergeSort(a)
        b = mergeSort(b)
        c = []        

        i = 0
        j = 0        

        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                c.append(a[i])
                i = i + 1
            else:
                c.append(b[j])
                j = j + 1        

        c += a[i:]
        c += b[j:]    

    return c


#example use
aa = [5,8,1,4,7,56,4,5,1,4,252,5,1]
print(mergeSort(aa))