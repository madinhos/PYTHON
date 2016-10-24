while True:
	try:
		reply = raw_input("Podaj liczbe rzeczywista:")
		if reply == "stop":
			break
		else:
			print reply, pow(float(reply),3)
	except ValueError:
		print "To nie jest liczba rzeczywita!"


