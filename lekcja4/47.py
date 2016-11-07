def flatten(sequence):
	lista = list()
	l = len(sequence)
	for i in range(l):
		if isinstance(sequence[i], (list, tuple)):
			lista.extend(flatten(sequence[i]))
		else:
			lista.append(sequence[i])
	return lista


seq = [1,(2,3),[],[4,(5,6,7)],8,[9],10]
print(seq)	
print(flatten(seq))

raw_input()


