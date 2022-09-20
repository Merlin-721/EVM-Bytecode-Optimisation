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


def fibs_short(n):
	a = 0
	b = 1
	for _ in range(1, n):
		c = a + b
		a = b
		b = c
	return b

for val in [0, 1, 5, 9, 600]:
	print(f'fibs: {fibs(val)}')
	print(f'fibs_short: {fibs_short(val)}')