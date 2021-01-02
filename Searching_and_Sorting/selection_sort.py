from math import inf

def selection_sort(aa):
	n = len(aa)
	for i in range(n - 1):
		mini = inf
		argmini = -1
		for j in range(i, n):
			if aa[j] < mini:
				argmini = j
				mini = aa[j]
		temp = mini
		aa[argmini] = aa[i]
		aa[i] = temp

aa = [8,12,3,5,4,55,12,5,99,99,101,98,1,2,7,1,54]
print(aa)
selection_sort(aa)
print(aa)