import random, math

#(a) rozne liczby od 0 do N-1 w kolejnosci losowej, 
def listA(n):
    l = list(range(n))
    random.shuffle(l)
    return l
	
#(b) rozne liczby od 0 do N-1 prawie posortowane 	
def listB(n):	
	l = list(range(n))
	for i in range(n-1):
		#zabezpieczenia przez wyjsciem poza indeks
		if i <= 1:
			ran = random.randint(i, i+2)
		if i > 1 and i < n-2:
			ran = random.randint(i-2, i+2)	
		if i >= n-2:
			ran = random.randint(i-2, i)	
			
		l[i], l[ran] = l[ran], l[i]
		i = i+1
	return l
	
#(c) rozne liczby od 0 do N-1 prawie posortowane w odwrotnej kolejnosci, 	
def listC(n):
	l = listB(n)
	l=l[::-1]
	return l

#(d) N liczb w kolejnosci losowej o rozkladzie gaussowskim, 	
def listD(n):
	l = list()
	for i in range(n-1):
		ran = int(round(random.gauss(n/2, n/6)))
		l.insert(i, ran)
	return l
	
	
#(e) N liczb w kolejnosci losowej, o wartosciach powtarzajacych sie, 
#nalezacych do zbioru k elementowego (k < N, np. k*k = N).	
def listE(n):
	l = list()
	for i in range(n-1):
		ran = int(random.randint(0,math.floor(math.sqrt(n))))
		l.insert(i, ran)
	return l	