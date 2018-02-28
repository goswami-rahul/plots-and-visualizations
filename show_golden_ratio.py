import matplotlib.pyplot as plt

def draw_graph(x, y):
	plt.plot(x, y)
	plt.xlabel('Numbers')
	plt.ylabel('Ratio')
	plt.title('Ratio between consecutive fibonacci numbers')

def draw(n):
	fib = [1, 1]
	for i in range(2, n+1):           # generate fiboncci numbers
		fib.append(fib[i-1]+fib[i-2])

	ratios = [fib[i] / fib[i - 1] for i in range(1, n+1)]
	draw_graph(range(1, n+1), ratios)

if __name__ == '__main__':
	try:
		n = int(input('Enter the number upto which Golden Ratio is to be plotted: '))
	except ValueError:
		print('Invalid Input')
	else:
		draw(n)
		plt.show()
		
