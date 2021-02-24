"""
GENERAL IDEA:
The key is to find a Property P such that P(x) implies P(y) for all y > x.



IMPLEMENTATION
define 3 things:
-a function can(x), boolean, and increasing
-find L and R such as can(L)==0 and can(R) == 1

Then we have 2 implementations depending if we want the first occurence true
or the last occurence not true
"""

"""
ALSO(but can live without it):
we can use bisect left and bisect right from python library bisect
bisect_left(aa, x): smallest index to insert x to keep aa sorted
bisect_right(aa, x): biggest index to insert x to keep aa sorted
"""



#implementations similar to the ones in python bisect library(not usefull, just good to look at implementation): 

def my_bisect_left(aa, x):
	"""
	return smallest index to insert x and keep aa sorted
	returns n if x is bigger than all elements
	"""
	n = len(aa)

	def can(i):
		return (x<=aa[i])


	#cannot
	L = -1

	#can
	R = n

	while (R -L) > 1:
		M = L  + (R-L)//2 #better than (R-L)//2, to prevent overflow
		if can(M):
			R = M
		else:
			L = M

	return R

def my_bisect_right(aa, x):
	"""
	return biggest index to insert x and keep aa sorted
	returns -1 if x is smaller than all elements of the list
	"""
	n = len(aa)

	def can(i):
		return (aa[i] > x)

	#cannot
	L = -1

	#can
	R = n

	while (R -L) > 1:
		M = L  + (R-L)//2 #better than (R-L)//2, to prevent overflow
		if can(M):
			R = M
		else:
			L = M

	return R


def occurences(aa, x):
	"""
	easy to calculate number of occurences of x in aa
	"""
	return my_bisect_right(aa, x) - my_bisect_left(x)

#example uses:
# https://codeforces.com/group/PMzrLJM5Tw/contest/317668

import bisect
aa= [0,0,1,2,3,3,4,5]
x= 3
print(bisect.bisect_left(aa,x), my_bisect_left(aa, x))
print(bisect.bisect_right(aa,x), my_bisect_right(aa, x))


aa= [0,0,1,2,3,3,4,5]
x= 6
print(bisect.bisect_left(aa,x), my_bisect_left(aa, x))
print(bisect.bisect_right(aa,x), my_bisect_right(aa, x))

