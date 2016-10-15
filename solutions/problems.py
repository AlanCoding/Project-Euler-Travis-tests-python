def problem1():
	'''
	If we list all the natural numbers below 10 that are multiples of 3 or 5,
		we get 3, 5, 6 and 9. The sum of these multiples is 23.
	Find the sum of all the multiples of 3 or 5 below 1000.
	'''
	return sum([i if (i % 5 == 0 or i % 3 == 0) else 0 for i in range(1000)])

def problem2():
	'''
	Sum of even Fibonacci sequence up to 4 million
	'''
	thesum = 0
	last = 1
	current = 1
	while thesum <= 4000000:
		if current % 2 == 0:
			thesum += current
		store = current
		current = current + last
		last = store
	return thesum
