import random

def mediana_sort(L, left, right):
	if(left > right):
		return None

	lst = heapSort(L)
	lstLen = len(L)
	index = (lstLen -1) // 2
	
	if (lstLen % 2):
		return lst[index]
	else:
		return (lst[index] + lst[index + 1])/2.0

#funkcje z poprzedniego zestawu
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
	return a
		
		
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

def listA(n):
    l = list(range(n))
    random.shuffle(l)
    return l
	
l = listA(100)

print "mediana", mediana_sort(l, 0, 9)

raw_input()