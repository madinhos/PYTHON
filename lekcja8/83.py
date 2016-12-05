import random, math

def pi_calc(n):
	count = 0
	for i in range(0, n):
		x2 = random.random()**2
		y2 = random.random()**2
		if math.sqrt(x2 + y2) < 1.0:
			count += 1
	return(float(count) / n) * 4

	
	
print("liczba prob 10:  ", pi_calc(10))
print("liczba prob 100:  ", pi_calc(100))
print("liczba prob 1000:  ", pi_calc(1000))
print("liczba prob 10000:  ", pi_calc(10000))
print("liczba prob 100000:  ", pi_calc(100000))

raw_input()