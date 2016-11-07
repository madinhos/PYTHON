#miarka
def miarka(L):
	try:
		result = ''

		#mnoze przez 5 poniewaz gdy liczba bedzie podzielna przez 5 wstawiam '|'
		#a jak nie to '.'
		L *=5 
		for i in range(L+1):
			if (i%5 == 0):
				result +="|"
			else:
				result +="."
		result +="\n"
		
		c = 0
		for i in range(L+2):
			if(i%5 == 0):
				if c<9:
					result += str(c)
					c+=1
					result += "    "
			if((i+1)%5 == 0):
				if c>=9 and c<99:
					result += str(c)
					c+=1
					result += "   "
			if((i+2)%5 == 0):
				if c>=99 and c<999:
					result += str(c)
					c+=1
					result += "  "
		
		return result
	except ValueError:
		return "To nie jest liczba!"


#prostokat
def prostokat(X,Y):
	try:
		result = ''	
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
		
		return result
	except ValueError:
		return "To nie jest liczba!"

#wywolanie	
l = int(raw_input("Podaj dlugosc miarki:"))
print(miarka(l))	

X = int(raw_input("Podaj szerokosc prostokata:"))
Y = int(raw_input("Podaj wysokosc prostokata:"))
print(prostokat(X,Y))
raw_input()


