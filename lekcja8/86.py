# P(0, 0) = 0.5
# P(i, 0) = 0.0 dla i > 0
# P(0, j) = 1.0 dla j > 0
# P(i, j) = 0.5 * (P(i-1, j) + P(i, j-1)) dla i > 0, j > 0


#Wniosek: Funckja dynamiczna jest duzo szybsza od funkcji rekurencyjnej, 
#poniewaz wykorzystuje wczesniej obliczone wartosci.
#Dla wartosci i=10, j=15 dla funkcji rekurencyjnej wynik otrzymujemy po oko³o sekundzie,
#a dla dynamicznej praktycznie od razu

#rekurencyjnie
def Prek(i, j):
	if i == 0 and j == 0:
		return 0.5
	if i > 0 and j == 0:
		return 0.0
	if 	i == 0 and j > 0:
		return 1.0
	if i < 0 or j < 0:
		raise ValueError("Wastosci ujemne!")
		return
	return 0.5*(Prek(i-1, j) + Prek(i, j-1))
	
#dynamicznie
S = {(0,0): 0.5, (0,1): 1.0, (1,0): 0.0} #slownik 
def Pdyn(i,j):
	global S
	if i == 0 and j == 0:
		return 0.5
	if i > 0 and j == 0:
		return 0.0
	if 	i == 0 and j > 0:
		return 1.0
	if i < 0 or j < 0:
		raise ValueError("Wastosci ujemne!")
		return
	
	h = S.get((i, j))
	if(h != None):
		return h
	else:
		h = 0.5*(Pdyn(i-1, j) + Pdyn(i, j-1))
		S[(i,j)] = h
		return h
	
print(Prek(1, 2))
print(Pdyn(1, 2))
print(Prek(10, 15))
print(Pdyn(10, 15))
raw_input()