import unittest
from fracs import *

class TestFractions(unittest.TestCase):
    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
		self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
		self.assertEqual(add_frac([-1, 2], [1, 3]), [-1, 6])
		self.assertEqual(add_frac([1, 4], [1, 4]), [2, 4])
		self.assertEqual(add_frac([0, 2], [1, 4]), [1, 4])
		self.assertEqual(add_frac([1, 3], [0, 4]), [1, 3])
		
    def test_sub_frac(self):
		self.assertEqual(sub_frac([3, 4], [1, 4]), [2, 4])
		self.assertEqual(sub_frac([-1, 2], [-2, 8]), [-4, 16])
		self.assertEqual(sub_frac([3, 4], [1, 8]), [20, 32])
		self.assertEqual(sub_frac([0, 2], [1, 4]), [1, 4])
		self.assertEqual(sub_frac([1, 3], [0, 4]), [1, 3])
		
    def test_mul_frac(self): 
		self.assertEqual(mul_frac([2, 4], [1, 4]), [2, 16])
		self.assertEqual(mul_frac([2, 3], [3, 5]), [6, 15])
		self.assertEqual(mul_frac([0, 3], [3, 5]), [0, 0])
		self.assertEqual(mul_frac([2, 3], [0, 5]), [0, 0])
		self.assertEqual(mul_frac([0, 3], [0, 5]), [0, 0])
		
    def test_div_frac(self): 
		self.assertEqual(div_frac([2, 4], [1, 4]), [8, 4])
		self.assertEqual(div_frac([2, 3], [3, 5]), [10, 9])
		self.assertEqual(div_frac([0, 3], [3, 5]), [0, 0])
		self.assertEqual(div_frac([2, 3], [0, 5]), [0, 0])
		self.assertEqual(div_frac([0, 3], [0, 5]), [0, 0])

    def test_is_positive(self): 
		self.assertEqual(is_positive([2, 4]), True)
		self.assertEqual(is_positive([-2, 4]), False)
		self.assertEqual(is_positive([0, 4]), False)

    def test_is_zero(self): 
		self.assertEqual(is_zero([0, 4]), True)
		self.assertEqual(is_zero([1, 4]), False)

    def test_cmp_frac(self): 
		self.assertEqual(cmp_frac([3, 4], [2, 4]), 1)
		self.assertEqual(cmp_frac([1, 4], [2, 4]), -1)
		self.assertEqual(cmp_frac([3, 5], [3, 5]), 0)
				
    def test_frac2float(self): 
		self.assertEqual(frac2float([1,2]),0.5)
		self.assertEqual(frac2float([1,4]),0.25)

    def tearDown(self):  pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
	
raw_input()	