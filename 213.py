line = "Lorem ipsum dolores"
print line
counter = 0
a = line.split()

for w in a:
  counter += len(w)
	

print "laczna dlugosc wyrazow -> ", counter

raw_input()