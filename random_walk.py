import random
import matplotlib.pyplot as plt

class RandomWalk():
	"""A class to generate random walks."""
	def __init__(self, num_points=5000):
		self.num_points = num_points
		self.x_values = [0]
		self.y_values = [0]
	
	def fill_walk(self):
		
		while len(self.x_values) < self.num_points:
			
			x_step = self.get_step()
			y_step = self.get_step()
			if x_step == 0 and y_step == 0:
				continue
			next_x = self.x_values[-1] + x_step
			next_y = self.y_values[-1] + y_step
			
			self.x_values.append(next_x)
			self.y_values.append(next_y)
	
	def get_step(self):
		dir = random.choice([1, -1])
		dist = random.choice(range(6))
		step = dir * dist
		return step


if __name__ == '__main__':
	choice = input("For line plot enter 'L'\nFor scatter plot enter 'S'\n")
	n = int(input("No. of points : "))	
	
	rw  = RandomWalk(5000)
	rw.fill_walk()
	
	plt.scatter(0, 0, s=15, c='green')
	
	if choice == 'S':
		plt.scatter(rw.x_values, rw.y_values, s=10, c=list(range(rw.num_points)), cmap=plt.cm.spring)
	elif choice == 'L':
		plt.plot(rw.x_values, rw.y_values, linewidth=1)
	
	plt.scatter(rw.x_values[-1], rw.y_values[-1], s=15, c='red')
	
	ax = plt.axes()
	ax.get_xaxis().set_visible(False)
	ax.get_yaxis().set_visible(False)
	ax.legend(['Start', 'Path', 'End'])
	plt.title('For n = %d' % n)
	plt.show()
			
