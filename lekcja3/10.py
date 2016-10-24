keys = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
values = [1, 5, 10, 50, 100, 500, 1000]
D = dict(zip(keys, values))

while True:
	g = raw_input("Podaj znak: ")
	if g == "stop":
		break;
	print D[g]
	
#-----------------------------
slownik = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000};

while True:
	g = raw_input("Podaj znak: ")
	if g == "stop":
		break;
	print slownik[g]

#-----------------------------
slownik = {};
slownik['I'] = 1;
slownik['V'] = 5;
slownik['X'] = 10;
slownik['L'] = 50;
slownik['C'] = 100;
slownik['D'] = 500;
slownik['M'] = 1000;

while True:
	g = raw_input("Podaj znak: ")
	if g == "stop":
		break;
	print slownik[g]

