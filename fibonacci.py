#Fibonacci example

def fibonacci():
	a, b = 0, 1
	while True:
		yield a
		a, b = b, a + b

f = fibonacci()
c = 0
for x in f:
	print x
	c += 1
	if(c > 200):
		break