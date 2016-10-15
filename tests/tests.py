# internal
from solutions import problems

# python
from math import sqrt

# utility methods
def F(n):
    return int(
		((1+sqrt(5))**n-(1-sqrt(5))**n)/
		(2**n*sqrt(5))
	)

def test_problem1():
	ans = problems.problem1()
	assert type(ans) == int
	for i in range(1000):
		if i % 3 == 0 or i % 5 == 0:
			ans -= i
	assert ans == 0

def test_problem2():
	ans = problems.problem2()
	# preliminary value constraint
	assert ans % 2 == 0
	i = 0
	while True:
		Fval = F(i)
		i += 1
		if Fval % 2 != 0:
			continue
		if Fval > 4000000:
			break
		ans -= Fval
	assert ans == 0

