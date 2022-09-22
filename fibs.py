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
	if n == 0:
		return 0
	a = 0
	b = 1
	for _ in range(1, n):
		c = a + b
		a = b
		b = c
	return b

n_values = 15

print(list(range(n_values)))
print('normal')
print([fibs(val) for val in range(n_values)])
print('short')
print([fibs_short(val) for val in range(n_values)])