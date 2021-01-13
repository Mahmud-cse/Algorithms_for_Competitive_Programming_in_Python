def ternary_search_discrete(f, a, b):
	"""
	input: a function that decreases first and increases after
	(monotonic parts not are not necessarly strictly monotonic,
	but the way my algo deals with the plateaus is not totally
	satisfactory imo, so be careful)
	output: returns an interval of length 3(in the general case) 
	and that interval contains the minimum
	we have to stop when the search interval
	becomes smaller than 3 : we cannot find 4 integers in there anymore
	"""
	while (b - a) >= 3:
		alpha = 1/3
		c = (1-alpha) * a + alpha * b
		c = int(c)
		d  = alpha * a + (1 - alpha) * b
		d = int(d)
		fc = f(c)
		fd = f(d)
		counter = 0
		while fc == fd:
			if counter % 2 == 0:
				d += 1
			else:
				c -= 1
			counter += 1
			if d > b or c < a:
				return (a,b)

		if fc < fd:
			b = d
		else:
			a  = c

	return (a, b)

def ternary_search_not_discrete(f, a, b, tol):
	"""
	we assume that f is stricly decreasing then strictly 
	increasing on [a,b]
	"""
	while (b - a) >= tol:
		alpha = 1/3
		c = (1-alpha) * a + alpha * b
		d  = alpha * a + (1 - alpha) * b
		fc = f(c)
		fd = f(d)

		if fc < fd:
			b = d
		else:
			a  = c

	return a