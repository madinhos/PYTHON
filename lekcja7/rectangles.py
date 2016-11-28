from points import Point

class Rectangle:
	def __init__(self, x1=0, y1=0, x2=0, y2=0):
    # Chcemy, aby x1 <= x2, y1 <= y2.
		if  x1 > x2 or y1 > y2: 
			raise ValueError("bledne dane inicjalizacyjne")	
		self.pt1 = Point(x1, y1)
		self.pt2 = Point(x2, y2)
		
		
	def __str__(self):
		return "([%s, %s], [%s, %s])" % (self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

	def __repr__(self):
		"Rectangle(%s, %s, %s, %s)" % (self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

	def __eq__(self, other):
		if not isinstance(other, Rectangle):
			raise ValueError("bledny argument")	
			
		if(self.pt1 == other.pt1 and self.pt2 == other.pt2):
			return True
		else:
			return False
			
	def __ne__(self, other):        # obsluga rect1 != rect2
		return not self == other	

	def center(self):
		return Point((self.pt1.x + self.pt2.x)/2, (self.pt1.y + self.pt2.y)/2)
		
	def area(self):
		return ((self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y))
		
	def move(self, x, y):
		if not (isinstance(x, int) or isinstance(y, int) or isinstance(x, float) or isinstance(y, float)):
			raise ValueError("bledne argumenty")	

		self.pt1.x += x
		self.pt2.x += x
		self.pt1.y += y
		self.pt2.y += y
		return self

	def intersection(self, other):
		if not isinstance(other, Rectangle):
			raise ValueError("bledny argument")	
		Result = Rectangle()
		Result.pt1.x = max(self.pt1.x, other.pt1.x)
		Result.pt2.x = min(self.pt2.x, other.pt2.x)
		Result.pt1.y = max(self.pt1.y, other.pt1.y)
		Result.pt2.y = min(self.pt2.y, other.pt2.y)
		return Result
		
	def cover(self, other):
		if not isinstance(other, Rectangle):
			raise ValueError("bledny argument")
		Result = Rectangle()
		Result.pt1.x = min(self.pt1.x, other.pt1.x)
		Result.pt2.x = max(self.pt2.x, other.pt2.x)
		Result.pt1.y = min(self.pt1.y, other.pt1.y)
		Result.pt2.y = max(self.pt2.y, other.pt2.y)
		return Result
		
	def make4(self):
		center = self.center()

		rec1 = Rectangle(self.pt1.x, self.pt1.y, center.x, center.y)
		rec2 = Rectangle(center.x, self.pt1.y, self.pt2.x, center.y)
		rec3 = Rectangle(self.pt1.x, center.y, center.x, self.pt2.y)
		rec4 = Rectangle(center.x, center.y, self.pt2.x, self.pt2.y)		
		return [rec1, rec2, rec3, rec4]



			