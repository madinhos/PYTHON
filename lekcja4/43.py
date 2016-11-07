def factorial(n):
	result = 1
	if(n>0):
		for i in range(1, n+1):
			result *= i;
		return result	
	else:
		return 1		
		
l = int(raw_input("Podaj lizcbe:"))
print(factorial(l))

raw_input()