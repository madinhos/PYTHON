#zadanie 10.8
import random

class RandomQueue:

	def __init__(self, size=5):
		self.n = size + 1         # faktyczny rozmiar tablicy
		self.items = self.n * [None] 
		self.head = 0           # pierwszy do pobrania 
		self.tail = 0           # pierwsze wolne
		self.numOfElements = 0;
		
	def is_empty(self):
		return self.head == self.tail

	def is_full(self):
		return (self.head + self.n-1) % self.n == self.tail

	def put(self, data):
		if self.is_full():
			raise ValueError("kolejka jest pelna")
			return	
		self.items[self.tail] = data
		self.tail = (self.tail + 1) % self.n
		self.numOfElements += 1
	def get(self):
		print ("Przed wymieszaniem  " + str(self.items))
		#mieszanie tablicy od zadanego indeksu do zadanego
		self.items[self.head:self.tail] = random.sample(self.items[self.head:self.tail], self.numOfElements)		
		
		print ("Po wymieszaniu  " + str(self.items))
		data = self.items[self.head]
		self.items[self.head] = None      # usuwam referencje
		self.head = (self.head + 1) % self.n
		self.numOfElements -= 1
		return data
		
		
a = RandomQueue()
a.put(1)
a.put(3)
a.put(10)
a.put(4)
a.put(6)
a.put(7)
print("Zwrocony element " + str(a.get()) + "\n") 
print("Zwrocony element " + str(a.get()) + "\n") 
print("Zwrocony element " + str(a.get()) + "\n") 
print("Zwrocony element " + str(a.get()) + "\n") 
print("Zwrocony element " + str(a.get()) + "\n") 
