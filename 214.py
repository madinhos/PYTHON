line = "Lorem ipsum dolor sit amet consectetur adipiscing elit"
print line
a = line.split()
print "najdluzszy wyraz -> ", max(a, key=len)
print "dlugosc -> ", len(max(a, key=len))

raw_input()