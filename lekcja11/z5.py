#Heapsort - szybki i niepochlaniajacy wiele pamieci algorytm sortowania. Nie jest stabilny.
#na podstawie algorytmu ze strony codecodex.com

# Pesymistyczna zlozonosc:	O(n log n)
# Optymistyczna zlozonosc:	O(n log n)
# Srednia zlozonosc:		O(n log n)

import z1

def heapSort(a):  
	count = len(a)  
	start = count / 2 - 1  
	end = count - 1  
  
	while start >= 0:  
		sift(a, start, count)  
		start -= 1  
  
	while end > 0:  
		a[end], a[0] = a[0], a[end]  
		sift(a, 0, end)  
		end -= 1  		
		
		
def sift(a, start, count):  
	root = start  

	while root * 2 + 1 < count:  
		child = root * 2 + 1  
		if child < count - 1 and a[child] < a[child + 1]:  
			child += 1  
		if a[root] < a[child]:  
			a[root], a[child] = a[child], a[root]  
			root = child  
		else:  
			return  
		
			
l = z1.listA(100)
print("Przed sortowaniem:")
print(l)
print("Po sortowaniu")
heapSort(l)
print(l)
