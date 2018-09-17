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
	for i in reversed(range(len(C))):
		print(i)
		c = (1-a[i])*c + a[i]*C[i]
	return c

def frontToBack(C,A):
	c = 0.
	a = 0.
	for i in range(len(C)):
		c = c + (1-a)*A[i]*C[i]
		print(a)
		a = a + (1-a)*A[i]
		if a > 0.99:
			print("We done at index " + str(i))
			break
	return c, a


if __name__ == "__main__":
	#print(getCord(3,2,0))
	fs = [-1,2,-2,1,4,-2,1,-2]
	#print(triPolate(fs,1/3,1/3,0.))
	#print(getAsympts(2,-4,-2,1))
	#print(triPolate(fs,1,0,0))
	Cs = [0.,2.,4.,2.,8.,7.,9.,5.,1.]
	As = [1./6,1./3,1./6,1./6,1./2,1./6,1./3,1./6,1./6]
	print(frontToBack(Cs,As))