from math import sqrt

def fibs(n):
	if n == 0:
		return 0
	a = 1
	b = 1
	for _ in range(2, n):
		c = a + b
		a = b
		b = c
	return b

val = 30
print(fibs(val))