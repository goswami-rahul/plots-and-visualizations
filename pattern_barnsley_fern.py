import random
import matplotlib.pyplot as plt
from typing import Tuple


def trans_1(p: Tuple[float, float]):
	x, y = p
	x, y = 0.85*x + 0.04*y, -0.04*x + 0.85*y + 16
	return x, y


def trans_2(p: Tuple[float, float]):
	x, y = p
	x, y = 0.2*x - 0.26*y, 0.23*x + 0.22*y + 1.6
	return x, y


def trans_3(p: Tuple[float, float]):
	x, y = p
	x, y = -0.15*x + 0.28*y, 0.26*x + 0.24*y + 0.44
	return x, y


def trans_4(p: Tuple[float, float]):
	x, y = p
	x, y = 0, 0.16*y
	return x, y


def transform(p: Tuple[float, float]):
	transformations = [trans_1, trans_2, trans_3, trans_4]
	probability = [0.85, 0.07, 0.07, 0.01]
	trans = random.choices(transformations, weights=probability)
	return trans[0](p)


def draw_fern(n, p):
	xi, yi = p
	x, y = [xi], [yi]
	for _ in range(n):
		xi, yi = transform((xi, yi))
		x.append(xi)
		y.append(yi)
	return x, y


if __name__ == '__main__':
	n = int(input("Enter the number of points in the Fern: "))
	x, y = draw_fern(n, (0.0, 0.0))
	plt.plot(x, y, '*')
	plt.title("Fern with {} points.".format(n))
	plt.show()