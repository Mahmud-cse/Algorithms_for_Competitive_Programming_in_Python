"""
Assume all elements of a sequence are between 0 and C*n
we can then sort in O(n)
"""

def counting_sort(aa, m):
	counts = [0] * (m + 1)
	for a in aa:
		counts[a] +=1 
	ss = []
	for i in range(m + 1):
		if counts[i] > 0:
			ss += [i]*counts[i]
	return ss

#driving code
aa = [1,4,9,5,2,1,4,5,7,8,5,6,3,1,2,4,5,6,8,5,4,5,2,1,5,7,8,5,5]
m  = max(aa)
ss = counting_sort(aa, m)
print(ss)
print(ss == sorted(aa))

