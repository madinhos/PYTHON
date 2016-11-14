from fractions import gcd

def add_frac(frac1, frac2):
	result = [0,0]
	if (frac1[1] == frac2[1]):
		result = [frac1[0]+frac2[0], frac1[1]]
		
	if (frac1[1] != frac2[1] and frac1[0] != 0) and (frac2[0] != 0):
		mianownik = frac1[1] * frac2[1]
		licznik = frac1[0]*frac2[1] + frac2[0]*frac1[1]
		result = [licznik, mianownik]
		
	if((frac1[0] == 0) and (frac2[0] == 0)):
		result = [0,0]
		
	if((frac1[0] == 0) and (frac2[0] != 0)):
		result = frac2
		
	if((frac1[0] != 0) and (frac2[0] == 0)):
		result = frac1
	
	return result
	
def sub_frac(frac1, frac2):
	result = [0,0]
	if (frac1[1] == frac2[1]):
		result = [frac1[0]-frac2[0], frac1[1]]
		
	if (frac1[1] != frac2[1] and frac1[0] != 0) and (frac2[0] != 0):
		mianownik = frac1[1] * frac2[1]
		licznik = frac1[0]*frac2[1] - frac2[0]*frac1[1]
		result = [licznik, mianownik]
		
	if((frac1[0] == 0) and (frac2[0] == 0)):
		result = [0,0]
		
	if((frac1[0] == 0) and (frac2[0] != 0)):
		result = frac2
		
	if((frac1[0] != 0) and (frac2[0] == 0)):
		result = frac1
	
	return result	
	
def mul_frac(frac1, frac2):
	result = [0,0]	
	if (frac1[0] != 0) and (frac2[0] != 0):
		mianownik = frac1[1] * frac2[1]
		licznik = frac1[0] * frac2[0]
		result = [licznik, mianownik]
		
	if((frac1[0] == 0) or (frac2[0] == 0)):
		result = [0,0]
			
	return result	
	
def div_frac(frac1, frac2):
	result = [0,0]
	if (frac1[0] != 0) and (frac2[0] != 0):
		frac2[0], frac2[1] = frac2[1], frac2[0]
		mianownik = frac1[1] * frac2[1]
		licznik = frac1[0] * frac2[0]
		result = [licznik, mianownik]
		
	if((frac1[0] == 0) or (frac2[0] == 0)):
		result = [0,0]
			
	return result	

def is_positive(frac):
	if ((frac[0] * frac[1]) > 0):
		return True
	else:
		return False
		
def is_zero(frac):	
    if frac[0] == 0:
        return True
    else:
        return False
		
def cmp_frac(frac1, frac2):
	temp = sub_frac(frac1, frac2)
	if is_zero(temp):
		return 0
	elif is_positive(temp):
		return 1
	else:
		return -1

def frac2float(frac):      
    return float(frac[0])/float(frac[1])		
		