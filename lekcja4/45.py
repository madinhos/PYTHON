#iteracja
def odwracanie(L, left, right): 
	temp = int((right - left)/2)
	if(left < right):
		temp2 = L[left]
		for i in range(temp):
			L[left+i] = L[right-i]
			L[right-i] = L[left+i]
		L[right] = temp2	
		return L
	else:
		return None
		
		
#rekurencja
def odwracanie2(L, left, right): 
	if(left < right):
		temp = L[left]
		L[left] = L[right]
		l[right] = temp
	else:
		return None
	if(left+1 != right):
		odwracanie2(L,left+1, right-1)

		
		
print("Iteracyjnie")		
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(A)
print(odwracanie(A, 3, 6)) 
print("\nRekurencyjnie")		
B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(B)
print(odwracanie(B, 2, 7)) 
raw_input()