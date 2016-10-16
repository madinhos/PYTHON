line = "Lorem ipsum dolor sit amet consectetur adipiscing elit"
print line
print "Sortowanie aflabetyczne", sorted(line.split(), key=lambda v: (v.upper(), v[0].islower()))
print "Sortowanie po dlugosci", sorted(line.split(), key=len)
raw_input()