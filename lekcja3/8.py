A = [1, 2, 3, 4, 5]
B = [4, 5, 1, 6, 9]
C = A+B
resultA = []
resultB = []

for i in C:
	if i not in resultA:
		resultA.append(i)
	else:
		resultB.append(i)
	

print "lista A: ", A
print "lista B: ", B
print "lista elementow wystepujacych w obu sekwencjach: ", resultB
print "lista wszystkich elementow z obu sekwencjach: ", resultA
raw_input()