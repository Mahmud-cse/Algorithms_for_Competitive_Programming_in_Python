#formulation of the problem:
#given a list aa = ['a', 'b', 'a', 'a', 'c', 'd', 'b', 'a', 'b', 'c']
#you will be given queries of the kind [i, j)
#you want to know if there is duplicates in aa[i:j]


"""
1/ We sweep left to right, to create a list pp
pp[i] = max index l such as l <= i and aa[l] == aa[i]   (-1 if no such index l)

2/ based on this pp, we build qq
qq[i] = max {pp[k] for k <= i}

Then for any query [i,j):
if qq[j-1] < i :  no duplicates
else: aa[ qq[j-1] ] is a duplicate in that range

complexity: initializtion O(n)
then O(1) for each query
"""
from collections import defaultdict

def closest_left_duplicate(aa):
	n = len(aa)
	pp = [-1]*n
	last_seen = defaultdict()
	for i, ai in enumerate(aa):
		if ai in last_seen:
			pp[i] = last_seen[ai]
		last_seen[ai] = i
	return pp

def max_closest_left_duplicate(pp):
	n = len(pp)
	qq = [-1] * n
	qq[0] = pp[0]
	for i in range(1, n):
		qq[i] = max(qq[i - 1], pp[i])
	return qq

def initialize(aa):
	pp = closest_left_duplicate(aa)
	qq = max_closest_left_duplicate(pp)
	return pp, qq

def answer_query( i, j, aa, pp, qq):
	if qq[j - 1] < i:
		return "No duplicates between i and j (i included, j excluded)"
	else:
		return f"element {aa[qq[j-1]]}, at index {qq[j-1]} is a duplicate in [i, j)." 


aa = ['a', 'b', 'a', 'a', 'c', 'd', 'b', 'a', 'b', 'c']
pp, qq = initialize(aa)
print(answer_query( 3, 6, aa, pp, qq))
print(answer_query( 4, 10, aa, pp, qq))






"""
example of application:
https://icpcarchive.ecs.baylor.edu/external/58/5881.pdf
"""