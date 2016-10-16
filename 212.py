line = "Lorem ipsum dolor sit amet consectetur adipiscing elit"

temp = line.split()
a = ""
b = ""
for w in temp:
	a = a + w[0:1]
	b = b + w[len(w)-1:len(w)]
	
print line
print "napis z pierwszych znakow -> ", a
print "napis z ostatnich znakow ->", b
raw_input()
