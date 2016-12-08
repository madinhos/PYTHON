from points import Point

class Triangle:
	def __init__(self, x1=0, y1=0, x2=0, y2=0, x3=0, y3=0):
		
#sprawdzanie czy pkt sa wspolliniowe obliczajac wyznacznik macierzy
# 	  |x1 y1 1|		
#     det |x2 y2 1| == 0
# 	  |x3 y3 1|	
		det = x1*y2*1 + x2*y3*1 + x3*y1*1 - 1*y2*x3 - 1*y3*x1 - 1*y1*x2
		if  (det == 0):
			raise ValueError("bledne dane inicjalizacyjne")	
			
		self.pt1 = Point(x1, y1)
		self.pt2 = Point(x2, y2)
		self.pt3 = Point(x3, y3)
	
	def __str__(self):
		return "[(%s, %s), (%s, %s), (%s, %s)]" % (self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y, self.pt3.x, self.pt3.y)
		
	def __repr__(self):
		return "Triangle(%s, %s, %s, %s, %s, %s)" % (self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y, self.pt3.x, self.pt3.y)
	
	def __eq__(self, other):
		if not isinstance(other, Triangle):
			raise ValueError("bledny argument")	
			
		if(self.pt1 == other.pt1 and self.pt2 == other.pt2 and self.pt3 == other.pt3):
			return True
		else:
			return False	
			
	def __ne__(self, other):        # obsluga tr1 != tr2
		return not self == other
	
	def center(self):
		x = (self.pt1.x + self.pt2.x + self.pt3.x)/3
		y = (self.pt1.y + self.pt2.y + self.pt3.y)/3
		return Point(x,y)
		
	def area(self):
		return (abs((self.pt1.x * (self.pt2.y - self.pt3.y) + self.pt2.x * (self.pt3.y - self.pt1.y) + self.pt3.x * (self.pt1.y - self.pt2.y)) / 2))
		
	def move(self, x, y):
		if not (isinstance(x, int) or isinstance(y, int) or isinstance(x, float) or isinstance(y, float)):
			raise ValueError("bledne argumenty")	
		
		self.pt1.x += x
		self.pt2.x += x
		self.pt3.x += x
		self.pt1.y += y
		self.pt2.y += y
		self.pt3.y += y

		return self
		
	def make4(self):	
		ab = Point((self.pt1.x + self.pt2.x)/2, (self.pt1.y + self.pt2.y)/2) #srodek odcinka pt1 i pt2
		bc = Point((self.pt2.x + self.pt3.x)/2, (self.pt2.y + self.pt3.y)/2) #srodek odcinka pt2 i pt3
		ca = Point((self.pt3.x + self.pt1.x)/2, (self.pt3.y + self.pt1.y)/2) #srodek odcinka pt3 i pt1

		tr1 = Triangle(self.pt1.x, self.pt1.y, ab.x, ab.y, ca.x, ca.y)
		tr2 = Triangle(ab.x, ab.y, self.pt2.x, self.pt2.y, bc.x, bc.y)
		tr3 = Triangle(ca.x,ca.y, ab.x, ab.y, bc.x, bc.y)
		tr4 = Triangle(ca.x, ca.y, bc.x, bc.y, self.pt3.x, self.pt3.y)
		print(tr1, tr2,tr3,tr4)
		return [tr1, tr2, tr3 ,tr4]
		














	
		
