from math import factorial

# Перестановки с повт
def permutationsRep(n):
	return n**n

def permutations(n):
	return factorial(n)

def combinations(n, k):
	return int(factorial(n)/(factorial(n-k)*factorial(k)))

# Cочетания с повт
def combinationsRep(n, k):
	return int(factorial(n + k - 1) / (factorial(n - 1) * factorial(k)))

# Размещения
def accommodations(n, k):
	return int(factorial(n) / factorial(n - k))

# Как эта дичь называлась, блен. todo
def allWords(n, k):
	return n**k

# Кол-во цикл послед длины n алфавита мощности m
def T(n, m):
	return T(n, m)

# Кол-во цикл послед периода n алфавита мощности m
def M(n, m):
	s = 0
	for d in range(1, n + 1):
		if n % d == 0:
			s += ME(d) * m ** (n / d)
	return int(s / n)

# Мебиус
def U(n):
	def isPrime(n):
		if n < 2:
			return False
		for i in range(2, n + 1):
			if i * i <= n and n % i == 0:
				return False
		return True

	if n == 1:
		return 1

	p = 0
	for i in range(1, n + 1):
		if (n % i == 0 and
				isPrime(i)):
			if n % (i * i) == 0:
				return 0
			else:
				p = p + 1

	if p % 2 != 0:
		return -1
	else:
		return 1
