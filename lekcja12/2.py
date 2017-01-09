#wyszukiwanie binarne-rekurencyjnie

def binarne_rek(L, left, right, y):
	if(left > right):
		return None
	else:
		mid = left + ((right-left) / 2)
		if L[mid] > y:
			return binarne_rek(L, left, mid-1, y)
		elif L[mid] < y:
			return binarne_rek(L, mid+1, right, y)
		else:
			return mid
			
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print "szukany:", 1, "pozycja:", binarne_rek(l, 0, 9, 1) 
print "szukany:", 5, "pozycja:", binarne_rek(l, 0, 9, 5) 
print "szukany:", 10, "pozycja:", binarne_rek(l, 0, 9,10) 
print "szukany:", 12, "pozycja:", binarne_rek(l, 0, 9, 12) 

raw_input()