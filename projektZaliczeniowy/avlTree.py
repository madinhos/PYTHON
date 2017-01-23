#Projekt zaliczeniowy "Drzewo AVL" ---- Jaroslaw Madej

class Node:
	def __init__(self, data=None, left=None, right=None, parent=None):
		self.data = data
		self.left = left
		self.right = right
		self.parent = parent
		self.bf = None		 #wspolczynnik zrownowazenia
		
	def __str__(self):
		return str(self.data)
	
	
class AVLTree:
	def __init__(self):
		self.root = None

	#Wstawianie wezla do drzewa
	def insert(self, data):
		w = Node()
		p = Node()
		
		p = self.root
		w.data = data
		w.left = w.right = w.parent = None
		w.bf = 0
		
		#Etap 1 - wstawianie wezla
		
		if self.root is None:
			self.root = w
			return
		else:
			while True:
				if(data < p.data):
					if p.left is None:
						p.left = w
						break
					p = p.left
				else:
					if p.right is None:
						p.right = w
						break
					p = p.right
		w.parent = p
		p = w.parent

		#Etap 2 - rownowazenie drzewa
		
		if(p.bf):
			p.bf = 0
		else:
			if(p.left == w):
				p.bf = 1
			else:
				p.bf = -1
			
			r = p.parent
			t = False
			while r:
				if r.bf:
					t = True
					break
				if r.left == p:
					r.bf = 1
				else:
					r.bf = -1
				p = r
				r = r.parent
			if t:
				if r.bf == 1:
					if  (r.right == p): r.bf = 0
					else:
						if(p.bf == -1): self.LR(r)
						else:
							self.LL(r)
				else:
					if(r.left == p): r.bf = 0
					else:
						if p.bf == 1: self.RL(r)
						else: self.RR(r)
						
			
			
	#Rotacja RL
	def RL(self, A):
		B = A.right
		C = B.left
		p = A.parent
		
		B.left = C.right
		if B.left:
			B.left.parent = B
		
		A.right = C.left
		if A.right:
			A.right.parent = A 

		C.left = A 
		C.right = B 
		A.parent = B.parent = C
		C.parent = p
		
		if(p):
			if p.left == A:
				p.left = C
			else:
				p.right = C
		else: 
			self.root = C
			
		if C.bf == -1: A.bf = 1
		else: A.bf = 0
		
		if C.bf == 1: B.bf = -1
		else: B.bf = 0
		
		C.bf = 0
		
	#Rotacja LR		
	def LR(self, A):
		B = A.left
		C = B.right
		p = A.parent
		
		B.right = C.left
		if B.right:
			B.right.parent = B
		
		A.left = C.right
		if A.left:
			A.left.parent = A 

		C.right = A 
		C.left = B 
		A.parent = B.parent = C
		C.parent = p
		
		if(p):
			if p.left == A:
				p.left = C
			else:
				p.right = C
		else: 
			self.root = C
			
		if C.bf == 1: A.bf = -1
		else: A.bf = 0
		
		if C.bf == -1: B.bf = 1
		else: B.bf = 0
		
		C.bf = 0
	
	#Rotacja RR
	def RR(self, A):
		B = A.right
		p = A.parent
		A.right = B.left
		
		if(A.right):
			A.right.parent = A
		
		B.left = A
		B.parent = p
		A.parent = B

		if(p):
			if(p.left == A):
				p.left = B
			else:
				p.right = B
		else:
			self.root = B
			
		if(B.bf == -1):
			A.bf = B.bf = 0
		else:
			A.bf = -1
			B.bf = 1
		
	#Rotacja LL	
	def LL(self, A):
		B = A.left
		p = A.parent
		A.left = B.right
		
		if(A.left):
			A.left.parent = A
		
		B.right = A
		B.parent = p
		A.parent = B

		if(p):
			if(p.left == A):
				p.left = B
			else:
				p.right = B
		else:
			self.root = B
			
		if(B.bf == 1):
			A.bf = B.bf = 0
		else:
			A.bf = 1
			B.bf = -1

	#Znajdowanie poprzednika wezla p		
	def predAVL(self, p):
		r = Node()
		
		if p:
			if p.left:
				p = p.left
				while p.right:
					p = p.right
			else:
				while p and p.right != r:
					r=p
					p = p.parent
		return p
			
	#Usuwanie wezla z drzewa	o wartosci n	
	def removeNode(self, n):
		x = Node();
		x = self.findNode(n)
		
		if x is None:
			print "Nie znaleziono podanego wezla"
			return
			
		nest = True	#zmienna wskazujaca zagniezdzenie
		t = y = z = Node()
		
		if(x.left and x.right):
			temp = self.predAVL(x)
			y = self.removeNode(temp.data)
			nest = False
		else:
			if x.left:
				y = x.left
				x.left = None
			else:
				y = x.right
				x.right = None
			x.bf = 0
			nest = True
		
		if y:
			y.parent = x.parent
			y.left = x.left
			if y.left: y.left.parent = y
			y.right = x.right 
			if y.right: y.right.parent = y 
			
		if x.parent:
			if x.parent.left == x: x.parent.left = y 
			else: x.parent.right = y
		else: self.root = y 
		
		if nest:
			z = y 
			y = x.parent 
			while y:
				#Przypadek nr 1
				if y.bf is None:
					if y.left == z: y.bf = -1
					else: y.bf = 1
					break
				else:
					#Przypadek nr 2
					if (y.bf == 1 and y.left == z) or (y.bf == -1 and y.right == z):
						y.bf = 0
						z = y
						y = y.parent
					else:
						if y.left == z: t = y.right
						else: t = y.left
						
						if t.bf is None:
							#Przypadek nr 3A
							if y.bf == 1: self.LL(y)
							else: self.RR(y)
							break
						elif y.bf == t.bf:
							#Przypadek nr 3B
							if y.bf == 1: self.LL(y)
							else: self.RR(y)
							z = t
							y = t.parent
						else:
							#Przypadek nr 3C
							if y.bf == 1: self.LR(y)
							else: self.RL(y)
							z = y.parent
							y = z.parent
		return x
	
	#Funkcja szukajaca wezla o wartosci k w drzewie AVL
	def findNode(self, k):
		p = Node()
		p = self.root
		while  p and p.data != k:
			if k < p.data:
				p = p.left
			else:
				p = p.right
		return p
			
#Wyswietlanie drzewa AVL			
def printTree(top, level=0):
	if top is None:
		return
	printTree(top.right, level+1)
	print "%s* %s:%s" % ('   '*level, top, top.bf)
	printTree(top.left, level+1)

	
	
#Prosta obsluga drzewa AVL poprzez terminal
"""	
avl = AVLTree()	

while True:
	print "1. Wstaw wezel do drzewa AVL"
	print "2. Usun wezel z drzewa avl"
	print "3. Wyswietl drzewo"
	print "4. Wyjscie"
	
	n = int(raw_input())
	if n == 1:
		print "Podaj wartosc wstawianego wezla"
		x = int(raw_input())
		if type(x) is int:
			avl.insert(x)
		else:
			"Podano niepoprawna wartosc"
	elif n == 2:
		print "Podaj wartosc usuwanego wezla"
		x = int(raw_input())
		if type(x) is int:
			avl.removeNode(x)
		else:
			"Podano niepoprawna wartosc"
	elif n == 3:
		printTree(avl.root)
	elif n == 4:
		break
	
	print "\n\n"
"""
	


	
