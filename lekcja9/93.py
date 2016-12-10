class Node:
	"""Klasa reprezentujaca wezel listy jednokierunkowej."""

	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

	def __str__(self):
		return str(self.data)   # bardzo ogolnie
		
def find_max(node):
	if node:
		max = node
	else:
		print("Brak elementu max")
		return
	while node != None:
		if node.data > max.data:
			max = node
		node = node.next
	return max	


def find_min(node):
	if node:
		min = node
	else:
		print("Brak elementu min")
		return
	while node != None:
		if node.data < min.data:
			min = node
		node = node.next
	return min

	
def traverse(node):
	if node:
		print(node.data)
		traverse(node.next)
       
  

#lista1
head = None                   
head = Node(6, head)          
head = Node(2, head)     
head = Node(20, head)      
head = Node(4, head)      
head = Node(1, head)          
head = Node(10, head)  
head = Node(8, head)     
head = Node(-5, head)        
head = Node(5, head)    

print "max", find_max(head)
print "min", find_min(head)

raw_input()