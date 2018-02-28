import random
import matplotlib.pyplot as plt
from typing import Tuple


def trans_1(p: Tuple[float, float]):
	x, y = p
	x, y = 0.5*x, 0.5*y
	return x, y


def trans_2(p: Tuple[float, float]):
	x, y = p
	x, y = 0.5*x + 0.5, 0.5*y + 0.5
	return x, y


def trans_3(p: Tuple[float, float]):
	x, y = p
	x, y = 0.5*x + 1, 0.5*y
	return x, y


def transform(p: Tuple[float, float]):
	transformations = [trans_1, trans_2, trans_3]
	trans = random.choice(transformations)
	return trans(p)


def draw_fern(n, p):
	xi, yi = p
	x, y = [xi], [yi]
	for _ in range(n):
		xi, yi = transform((xi, yi))
		x.append(xi)
		y.append(yi)
	return x, y


if __name__ == '__main__':
	n = int(input("Enter the number of points in the Pattern: "))
	x, y = draw_fern(n, (0.0, 0.0))
	plt.plot(x, y, '*')
	plt.title("Sierpinski triangle with {} points.".format(n))
	plt.show()