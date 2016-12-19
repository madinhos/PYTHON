#zadanie 10.4
import unittest
from queue_4 import *

class TestQueue(unittest.TestCase):
	def test_is_empty(self):
		a = Queue()
		self.assertTrue(a.is_empty() == True)
		
	def test_is_full(self):
		a = Queue()
		a.put(1)
		a.put(2)
		a.put(3)
		a.put(4)
		a.put(5)		
		self.assertTrue(a.is_full() == True)
	
	def test_queue_put(self):	
		try:
			a = Queue()
			a.put(1)
			a.put(2)
			a.put(3)
			a.put(4)
			a.put(5)
			a.put(6)
			a.put(8)
		except Exception:
			print("przechwycenie wyjatku, kolejka pelna")
			
	def test_queue_remove(self):	
		try:
			a = Queue()
			a.put(1)
			a.put(2)
			a.put(3)
			a.remove()
			a.remove()
			a.remove()
			a.remove()
		except Exception:
			print("przechwycenie wyjatku, kolejka jest juz pusta")			
			
			
	def tearDown(self): pass

if __name__ == '__main__':
	unittest.main()     # uruchamia wszystkie testy