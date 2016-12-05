def solve1(a, b, c):
	if a == b == 0:
		if c == 0:
			print("Rownanie nieokreslone!")
			return
		else:
			print("Rownanie sprzeczne")
			return
	if b == 0:
		x = float(-c)/float(a)
		print ("Rozwiazaniem jest prosta: x = %s, y e R") % (x)
		return
	if a == 0:
		y = float(-c)/float(b)
		print ("Rozwiazaniem jest prosta: y = %s, x e R") % (y)
		return
		
	y1 = float(-c)/float(b)
	y2 = float(-a)/float(b)
	print ("Rozwiazaniem jest prosta: y = %sx + %s") % (y2, y1)
	return
	
print("Podaj wartosci A B C")
a = input()
b = input()
c = input()
solve1(a, b, c)

raw_input()