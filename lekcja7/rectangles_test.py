import unittest
from rectangles import *

class TestRectangles(unittest.TestCase):

	def test_eq_rectangles(self):
		self.assertTrue(Rectangle(2, 2, 4, 4) == Rectangle(2, 2, 4, 4))
		self.assertFalse(Rectangle(2, 2, 4, 4) == Rectangle(2, 2, 6, 6))
	
	def test_ne_rectangles(self):
		self.assertFalse(Rectangle(2, 2, 4, 4) != Rectangle(2, 2, 4, 4))
		self.assertTrue(Rectangle(2, 2, 4, 4) != Rectangle(2, 2, 6, 6))
		
	def test_center_rectangles(self):	
		self.assertEqual(Rectangle(0, 0, 4, 4).center(), Point(2, 2))
		self.assertEqual(Rectangle(2, 2, 4, 4).center(), Point(3, 3))
		self.assertEqual(Rectangle(-2, -2, 2, 2).center(), Point(0, 0))
		self.assertEqual(Rectangle(2, 2, 2, 2).center(), Point(2, 2))
		
	def test_area_rectangles(self):	
		self.assertEqual(Rectangle(0, 0, 4, 4).area(), 16)
		self.assertEqual(Rectangle(2, 2, 4, 4).area(), 4)
		self.assertEqual(Rectangle(-3, -2, 4, 0).area(), 14)
		
	def test_move_rectangles(self):
		self.assertEqual(Rectangle(0, 0, 4, 4).move(2, 2), Rectangle(2, 2, 6, 6))
		self.assertEqual(Rectangle(0, 0, 4, 4).move(-2, -2), Rectangle(-2, -2, 2, 2))
		self.assertEqual(Rectangle(0, 0, 4, 4).move(0.5, 0.5), Rectangle(0.5, 0.5, 4.5, 4.5))
		
	def test_intersection_rectangles(self):
		self.assertEqual(Rectangle(0, 0, 4, 4).intersection(Rectangle(2, 2, 6, 6)), Rectangle(2, 2, 4, 4))
		self.assertEqual(Rectangle(-4, -4, 0, 0).intersection(Rectangle(-2, -2, 2, 2)), Rectangle(-2, -2, 0, 0))
		
	def test_cover_rectangles(self):
		self.assertEqual(Rectangle(0, 0, 2, 2).cover(Rectangle(4, 4, 6, 6)), Rectangle(0, 0, 6, 6))
		self.assertEqual(Rectangle(1, 2, 10, 8).cover(Rectangle(5, 4, 12, 6)), Rectangle(1, 2, 12, 8))
	
	def test_make4_rectangles(self):
		self.assertEqual(Rectangle(0, 0, 4, 4).make4(), [Rectangle(0,0,2,2), Rectangle(2,0,4,2), Rectangle(0,2,2,4), Rectangle(2,2,4,4)])

		
if __name__ == '__main__':
	unittest.main()     # uruchamia wszystkie testy