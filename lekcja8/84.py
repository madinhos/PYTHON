import math
#wzor Herona pozwala obliczyc pole kwadratu znajac wylacznie dlugosci bokow
def heron(a, b, c):
	if a+b <= c or a+c <= b or b+c<=a:
		raise ValueError("niewlasciwe parametry")
	p = (a+b+c)*0.5
	s = math.sqrt((a+b+c)*(a+b-c)*(a-b+c)*(-a+b+c))/4
	return s

print("podaj dlugosci bokow trojkata")
a = float(input())
b = float(input())
c = float(input())

try:
	p = heron(a, b, c)
	print("pole trojkata wynosi:", p)
except ValueError:
	print("niewlasciwe parametry")