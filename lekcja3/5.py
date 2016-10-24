try:
	result = ''
	L = int(raw_input("Podaj dlugosc miarki:"))
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
	
	print result
except ValueError:
	print "To nie jest liczba!"
	
raw_input()


