"""
find the root of a function on a segment [a,b]
"""
def bisection_search(f, a, b, tol):
	low = a
	high = b

	assert f(a)*f(b) < 0

	if f(a) > 0:
		sign_left = 1
	else:
		sign_left = -1

	if (b-a) <= tol:
		return (a + b)/2

	while (high - low) > tol:
		mid = (low + high) / 2
		#we save this val to just do one function call
		#instead of two
		val = f(mid)
		if val == 0:
			break
		elif val*sign_left > 0:
			low = mid
		else:
			high = mid

	return mid
