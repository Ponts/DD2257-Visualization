import numpy as np


def w0(x,y):
	return 1./(np.sqrt(x**2 + y**2))

def w1(x,y):
	return 1./(np.sqrt((x-1)**2 + y**2))

def w2(x,y):
	return 1./(np.sqrt((x)**2 + (y-1)**2))

def shepard(s,x,y):
	w = []
	w.append(w0(x,y))
	w.append(w1(x,y))
	w.append(w2(x,y))
	tot = sum(w)
	ret = 0.
	for i in range(len(w)):
		ret += (w[i]/tot)*s[i]
	return ret

def triangle(s,x,y):
	return (1-x-y)*s[0] + x*s[1] + y*s[2]

if __name__ == "__main__":
	s = [1,2,3]
	x = 2/3
	y = 2/3
	print(shepard(s,x,y))

	
	