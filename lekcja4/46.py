def sum_seq(sequence):
	result = 0;
	l = len(sequence)
	for i in range(l):
		if isinstance(sequence[i], (list, tuple)):
			result += sum_seq(sequence[i])
		else:
			result += sequence[i]
	return result		


seq = [1,(2,3),[],[4,(5,6,7)],8,[9],10]
print(seq)	
print(sum_seq(seq))

raw_input()


