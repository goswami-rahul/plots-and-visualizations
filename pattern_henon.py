import random
import matplotlib.pyplot as plt

def trans(p):
	x, y = p
	x, y = y + 1 - 1.4*x**2, 0.3*x
	return x, y

def draw(n, p):
	xi, yi = p
	x = [xi]
	y = [yi]
	for _ in range(n):
		xi, yi = trans((xi, yi))
		x.append(xi)
		y.append(yi)
	plt.plot(x, y, '*')
	plt.title('Henon pattern for %d points' % n)
	plt.show()
	
if __name__ == '__main__':
	n = int(input("Enter the number of points : "))
	draw(n, (1, 1))
