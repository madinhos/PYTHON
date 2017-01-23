import unittest
from avlTree import *

class TestQueue(unittest.TestCase):

	#test rotacji RR
	#1		2
	# 2	->  1 3
	#  3
	def test_RR_Rotation(self):
		print
		avl = AVLTree()
		avl.insert(1)
		avl.insert(2)
		avl.insert(3)
		
		self.assertTrue(
			avl.root.data == 2 and
			avl.root.right.data == 3 and
			avl.root.left.data == 1
		)
	
	#test rotacji LL
	#  1		2
	# 2	->  1 3
	#3	
	def test_LL_Rotation(self):
		avl = AVLTree()
		avl.insert(3)
		avl.insert(2)
		avl.insert(1)
		
		self.assertTrue(
			avl.root.data == 2 and
			avl.root.right.data == 3 and
			avl.root.left.data == 1
		)
		
	#test rotacji RL
	# 1		3
	#  5	->  1 5
	# 3	
	def test_RL_Rotation(self):
		avl = AVLTree()
		avl.insert(1)
		avl.insert(5)
		avl.insert(3)
		
		self.assertTrue(
			avl.root.data == 3 and
			avl.root.right.data == 5 and
			avl.root.left.data == 1
		)

	#test rotacji RL
	# 5		3
	#1	->  1 5
	# 3		
	def test_LR_Rotation(self):
		avl = AVLTree()
		avl.insert(5)
		avl.insert(1)
		avl.insert(3)
		
		self.assertTrue(
			avl.root.data == 3 and
			avl.root.right.data == 5 and
			avl.root.left.data == 1
		)	
		
	#test removeNode
	# 2		3
	#1 3	->  1		
	def test_remove_Node(self):
		avl = AVLTree()
		avl.insert(1)
		avl.insert(2)
		avl.insert(3)
		avl.removeNode(2)	
		self.assertTrue(
			avl.root.data == 3 and
			avl.root.left.data == 1
		)		
		
		avl.removeNode(3)
		
		self.assertTrue(
			avl.root.data == 1
		)

	def test_remove2_Node(self):
		avl = AVLTree()
		avl.insert(1)
		avl.insert(2)
		avl.insert(3)
		avl.insert(4)
		avl.removeNode(1)	
		self.assertTrue(
			avl.root.data == 3 and
			avl.root.left.data == 2 and
			avl.root.right.data == 4 
		)			
		
	def test_findNode(self):
		avl = AVLTree()
		avl.insert(1)
		avl.insert(2)
		avl.insert(3)
		avl.insert(4)
		
		self.assertTrue(avl.findNode(4))
		self.assertTrue(avl.findNode(1))
		self.assertFalse(avl.findNode(6))
		
		
	def test_other(self):
		avl = AVLTree()
		avl.insert(10)
		avl.insert(3)
		avl.insert(6)
		avl.insert(7)
		avl.insert(2)
		avl.insert(14)
		avl.insert(15)
		avl.insert(23)
		
		self.assertTrue(
			avl.root.data == 6 and
			avl.root.left.data == 3 and
			avl.root.right.data == 10 and
			avl.root.left.left.data	== 2 and
			avl.root.right.right.data == 15 and
			avl.root.right.left.data == 7 and
			avl.root.right.right.left.data == 14 and
			avl.root.right.right.right.data == 23 
		)
		
		avl.removeNode(2)
		
		self.assertTrue(
			avl.root.data == 10 and
			avl.root.left.data == 6 and
			avl.root.right.data == 15 and
			avl.root.left.left.data	== 3 and
			avl.root.left.right.data	== 7 and
			avl.root.right.right.data == 23 and
			avl.root.right.left.data == 14 
		)
		
			
	def tearDown(self): pass

if __name__ == '__main__':
	unittest.main()     # uruchamia wszystkie testy