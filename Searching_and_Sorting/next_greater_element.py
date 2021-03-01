"""
How to find the next greater element in a sequence?
we have a sequence aa = [12,1,45,21,4,7,2,5,4,1,6]
and we want to build another sequence bb, that contains at each index i the smallest index j/
such as i < j and aa[i] < aa[j]
"""

"""
easy to get smallest instead of greatest with -aa
"""


def indexes_of_next_stricly_greater(aa):
	"""
	returns an array of indexes
	indexes = n in that array means that there is not greater element on the right
	"""
	n = len(aa)
	result = [n]* n # n means no index to the right is greater

	#we maintain a stack of INDEXES of decreasing values from the left 
	# .. >= .. >= .. >= ... 

	stack = []
	for i in range(n):
		#elements in the stack samller than aa[i] get popped
		while stack and aa[ stack[-1] ] < aa[i]:
			result[stack.pop()] = i

		# then we add i
		stack.append(i)
	return result


def indexes_of_next_greater_or_equal(aa):
	"""
	returns an array of indexes
	indexes = n in that array means that there is no greater element on the right
	"""
	n = len(aa)
	result = [n]* n # n means no index to the right is greater

	#we maintain a stack of INDEXES of decreasing values from the left 
	# .. > .. > .. > ... 

	stack = []
	for i in range(n):
		#elements in the stack samller than aa[i] get popped
		while stack and aa[ stack[-1] ] <= aa[i]:
			result[stack.pop()] = i

		# then we add i
		stack.append(i)
	return result

def indexes_of_previous_stricly_ greater(aa):
	"""
	returns an array of indexes
	indexes = -1 in that array means that there is not greater element on the left
	"""
	n = len(aa)
	result = [-1]* n # n means no index to the right is greater

	#we maintain a stack of INDEXES of decreasing values from the right
	# <=  <=  <=

	stack = []
	for i in range(n-1,-1,-1):
		#elements in the stack samller than aa[i] get popped
		while stack and aa[ stack[-1] ] < aa[i]:
			result[stack.pop()] = i

		# then we add i
		stack.append(i)
	return result

def indexes_of_previous_greater_or_equal(aa):
	"""
	returns an array of indexes
	indexes = -1 in that array means that there is not greater element on the left
	"""
	n = len(aa)
	result = [-1]* n # 

	#we maintain a stack of INDEXES of decreasing values from the right
	# <  <  <

	stack = []
	for i in range(n-1,-1,-1):
		#elements in the stack samller than aa[i] get popped
		while stack and aa[ stack[-1] ] <= aa[i]:
			result[stack.pop()] = i

		# then we add i
		stack.append(i)
	return result



#example problem:
#https://codeforces.com/group/PMzrLJM5Tw/contest/317834/problem/I