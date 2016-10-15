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

def primes(n):
	""" Returns  a list of primes < n """
	# http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188
	sieve = [True] * n
	for i in range(3,int(n**0.5)+1,2):
		if sieve[i]:
			sieve[i*i::2*i]=[False]*int((n-i*i-1)/(2*i)+1)
	return [2] + [i for i in range(3,n,2) if sieve[i]]

# Tests of the solutions themselves
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

def test_problem3():
	ans = problems.problem3()
	num = 600851475143
	lesser_primes = primes(ans)
	reduced_num = num
	for prime in lesser_primes + [ans]:
		while reduced_num % prime == 0:
			reduced_num = int(reduced_num / prime)
	assert reduced_num == 1

