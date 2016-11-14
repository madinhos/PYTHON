def fibonacci(n):
	f0 = 0
	f1 = 1
	f=0
	
	for i in range(n+1):
		if(i > 1):
			f = f0 + f1
			f0 =f1
			f1 = f
		else:
			f = i
	return f
	
def factorial(n):
	result = 1
	if(n>0):
		for i in range(1, n+1):
			result *= i;
		return result	
	else:
		return 1