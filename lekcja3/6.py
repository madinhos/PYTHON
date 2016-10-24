try:
	result = ''
	X = int(raw_input("Podaj szerokosc prostokata:"))
	Y = int(raw_input("Podaj wysokosc prostokata:"))
	
	helper = 0
	
	if Y == 1:
		helper = 3;
	if Y > 1:
		helper = (Y*2)+1
	
	for i in range(helper):
		if i%2 != 0:
			result +="|"
			for j in range(X):
				result +="   |"
			result +="\n"	
		if i%2 == 0:
			result +="+"
			for j in range(X):
				result +="---+"		
			result +="\n"	
	
	print result
except ValueError:
	print "To nie jest liczba!"
	
raw_input()


