
class Node:
	"""Klasa reprezentujaca wezel drzewa binarnego."""

	def __init__(self, data=None, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

	def __str__(self):
		return str(self.data)
		
def btree_print_indented(top, level=0):
	if top is None:
		return
	btree_print_indented(top.right, level+1)
	print "%s* %s" % ('   '*level, top)
	btree_print_indented(top.left, level+1)
	
def count_leafs(top): 
	count = 0
	if top is None:
		return
	if top.left == None and top.right == None:
		count +=1
	if top.left:
		count += count_leafs(top.left)
	if top.right:
		count += count_leafs(top.right)
	return count	

def count_total(top):
    if top is None:
        return 0
    return count_total(top.left) + top.data + count_total(top.right)
		
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)
root2.left.right = Node(5)
root2.right.left = Node(6)
root2.right.right = Node(7)
root2.left.left.left = Node(8)
root2.left.left.right = Node(9)
root2.left.right.left = Node(10)
root2.left.right.right = Node(11)
root2.right.left.left = Node(12)
root2.right.left.right = Node(13)
root2.right.right.left = Node(14)
root2.right.right.right = Node(15)

btree_print_indented(root)
print("Liczba lisci: ", count_leafs(root))
print("Suma liczb: ", count_total(root))

btree_print_indented(root2)
print("Liczba lisci: ", count_leafs(root2))
print("Suma liczb: ", count_total(root2))