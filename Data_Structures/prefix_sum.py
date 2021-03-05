def prefix_sum(aa):
	"""
	builds an array of size n + 1
	pp[0] = 0
	pp[i] = aa[0] + aa[1] + ... + aa[i-1]
	then RSQ easy : aa[i] + aa[i+1] + ...+ aa[j] = pp[j+1] - pp[i]
	""" 
	n = len(aa)
	pp = [0]*(n + 1)
	for i in range(n):
		pp[i + 1] = aa[i] + pp[i]
	return pp

#example
aa = [3,2,1,4]
pp = prefix_sum(aa)

print(f"sum between index 1 and 2 is {pp[3]- pp[1]}.")