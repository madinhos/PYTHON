class Stack:

	def __init__(self, size=10):
		self.items = size * [None]      # utworzenie tablicy
		self.n = 0                      # liczba elementow na stosie
		self.size = size
		self.occupied = size * [0]
		
	def is_empty(self):
		return self.n == 0

	def is_full(self):
		return self.size == self.n

	def push(self, data):
		if self.occupied[data] == 0:
			self.items[self.n] = data
			self.n = self.n + 1
			self.occupied[data] = 1
			
	def pop(self):
		self.n = self.n - 1
		data = self.items[self.n]
		self.occupied[data] = 0
		self.items[self.n] = None    # usuwam referencje
		return data
		
	def printStack(self):
		while not self.is_empty():
			print(self.pop())

a = Stack()	
a.push(1)
a.push(2)
a.push(2)
a.push(5)
a.push(5)
a.push(6)
a.printStack()
raw_input()		


