from solutions import problems

def test_problem1():
	ans = problems.problem1()
	assert type(ans) == int
	for i in range(1000):
		if i % 3 == 0 or i % 5 == 0:
			ans -= i
	assert ans == 0
