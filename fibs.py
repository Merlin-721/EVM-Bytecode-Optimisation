from math import sqrt

def fibs(n):
	return (((1+sqrt(5))/2)**n - ((1-sqrt(5))/2)**n)/sqrt(5)

phi_pos = 1.618033988749895
phi_neg = -0.6180339887498949
root_5 = 2.23606797749979

def fibs_const(n):
	return (phi_pos**n - phi_neg**n)/root_5

val = 30
print(fibs(val))
print(fibs_const(val))