import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def z(i,j,k):
	return (20./7.) * k

def x(i,j,k):
	distFromCenter = 5 + (5./4.)*i
	angle = alpha*j
	return distFromCenter*np.cos(angle)

def y(i,j,k):
	distFromCenter = 5 + (5./4.)*i
	angle = alpha * j
	return distFromCenter * np.sin(angle)


alpha = (2*np.pi)/20
if __name__ == "__main__":
	
	angulars = [i for i in range(20)]
	radials = [i for i in range(5)]
	zs = [i for i in range(8)]

	plotXs = []
	plotYs = []
	plotZs = []
	for i in radials:
		for j in angulars:
			for k in zs:
				#print(x(i,j,k),y(i,j,k),z(i,j,k))
				plotXs.append(x(i,j,k))
				plotYs.append(y(i,j,k))
				plotZs.append(z(i,j,k))

	
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	ax.scatter(plotXs, plotYs, plotZs)
	plt.show()



