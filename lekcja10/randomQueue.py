import random

class randomQueue:

	def __init__(self):
		self.items = []

	def __str__(self):             # podgladanie kolejki
		return str(self.items)

	def is_empty(self):
		return not self.items

	def is_full(self):             # nigdy nie jest pusta
		return False

	def insert(self, data):
		self.items.append(data)

	def remove(self):
		l = len(self.items)
		
		if l <= 1:
			data = self.items[0]
			del self.items[0]
			
			return data
		
		r = random.randint(0, l-1)
		data = self.items[r]	
		self.items[r], self.items[l-1] = self.items[l-1], self.items[r]
		del self.items[l-1]
		
		return data
		
		
		
		
a = randomQueue()

a.insert(5) 
print (a.remove())
print a
a.insert(9)
a.insert(2)
a.insert(1)
a.insert(10)
print a
print (a.remove())
print a

raw_input() 
