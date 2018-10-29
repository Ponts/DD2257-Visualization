def getCord(a,b,c):
	return float((c-a))/float((b-a))

def getAsympts(f11,f21,f12,f22):
	x = (f11-f12)/(f22+f11-f12-f21)
	y = (f11-f21)/(f22+f11-f12-f21)
	return x,y

def triPolate(fs, x, z, y):
	c000, c100, c101, c001, c010, c110, c111, c011 = fs;
	c00 = c000*(1-x) + c100*x
	c01 = c001*(1-x) + c101*x
	c10 = c010*(1-x) + c110*x
	c11 = c011*(1-x) + c111*x

	c0 = c00*(1-y) + c10*y
	c1 = c01*(1-y) + c11*y

	c = c0*(1-z) + c1*z

	return c

def backToFront(C, a):
	c = 0.
	al = 0.
	for i in reversed(range(len(C))):
		#print(i)
		c = (1-a[i])*c + a[i]*C[i]
		al = (1-a[i])*al + a[i]
		print("C[" + str(i) + "] = " + str(c))
		print("A[" + str(i) + "] = " + str(al))
	return c

def frontToBack(C,A):
	c = 0.
	a = 0.
	for i in range(len(C)):
		c = c + (1-a)*A[i]*C[i]
		print("C[" + str(i) + "] = " + str(c))
		a = a + (1-a)*A[i]
		print("A[" + str(i) + "] = " + str(a))
		if a > 0.99:
			print("We done at index " + str(i))
			break
	return c, a

def midpointDecider(f00,f10,f01,f11,c):
	print((f00+f10+f01+f11)/4)
	return c > (f00+f10+f01+f11)/4

def asympDec(f00,f10,f01,f11,c):
	x,y = getAsympts(f00,f10,f01,f11)
	print(x,y)
	b = (1-y)*((1-x)*f00 + x*f10) + y*((1-x)*f01 + x*f11)
	print(b)
	return c > b

def fails(f00,f10,f01,f11,c):
	return midpointDecider(f00,f10,f01,f11,c) != asympDec(f00,f10,f01,f11,c)


if __name__ == "__main__":
	print(getCord(3,2,0))
	#fs = [-1,2,-2,1,4,-2,1,-2]
	#print(triPolate(fs,1/3,1/3,0.))
	#print(getAsympts(2,-4,-2,1))
	#print(triPolate(fs,1,0,0))
	#Cs = [0.,2.,4.,2.,8.,7.,9.,5.,1.]
	#As = [1./6,1./3,1./6,1./6,1./2,1./6,1./3,1./6,1./6]
	#frontToBack(Cs,As)
	#f00 = -1.
	#f10 = 4.
	#f01 = 2.
	#f11 = -2.
	#print(midpointDecider(f00,f10,f01,f11,0))
	#print(asympDec(f00,f10,f01,f11,0))
	#print(fails(f00,f10,f01,f11,0))