import unittest
from triangles import *

class TestRectangles(unittest.TestCase):
	def test_eq_triangles(self):
		self.assertTrue(Triangle(2, 2, 4, 2, 3, 5) == Triangle(2, 2, 4, 2, 3, 5))
		self.assertFalse(Triangle(2, 2, 4, 2, 3, 5) == Triangle(2, 2, 4, 2, 3, 6))
		
	def test_ne_triangles(self):
		self.assertFalse(Triangle(2, 2, 4, 2, 3, 5) != Triangle(2, 2, 4, 2, 3, 5))
		self.assertTrue(Triangle(2, 2, 4, 2, 3, 5) != Triangle(2, 2, 4, 2, 3, 6))
		
	def test_center_triangles(self):
		self.assertEqual(Triangle(0, 0, 4, 0, 2, 6).center(), Point(2,2))
		self.assertEqual(Triangle(-5, 5, 10, -5, 10, 20).center(), Point(5,6))
		
	def test_area_triangles(self):
		self.assertEqual(Triangle(0, 0, 4, 0, 2, 6).area(), 12)
		self.assertEqual(Triangle(-2, -2, 2, -2, 0, -6).area(), 8)
		
	def test_move_triangles(self):
		self.assertEqual(Triangle(0, 0, 4, 0, 2, 6).move(2,3), Triangle(2, 3, 6, 3, 4, 9))
		self.assertEqual(Triangle(2, 3, 6, 3, 4, 9).move(-2,-3), Triangle(0, 0, 4, 0, 2, 6))
		self.assertEqual(Triangle(0, 0, 4, 0, 2, 6).move(0.5,0.5), Triangle(0.5, 0.5, 4.5, 0.5, 2.5, 6.5))
		
	def test_make4_triangles(self):	
		self.assertEqual(Triangle(0, 0, 4, 0, 2, 4).make4(), [Triangle(0,0,2,0,1,2), Triangle(2,0,4,0,3,2), Triangle(1,2,2,0,3,2), Triangle(1,2,3,2,2,4)])
		
if __name__ == '__main__':
	unittest.main()     # uruchamia wszystkie testy