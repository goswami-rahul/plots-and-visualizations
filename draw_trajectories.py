import matplotlib.pyplot as plt
import math
import matplotlib.animation

def draw_graph(x, y):
	plt.plot(x, y)
	plt.xlabel('x-coordinate')
	plt.ylabel('y-coordinate')
	plt.title('Projectile motion of a ball')
	
def frange(start, final, interval):
	numbers = []
	while start < final:
		numbers.append(start)
		start += interval
	return numbers

def draw_trajectory(u, theta):
	
	intervals = 0.001  # the range of intervals (you can modify this value)
	theta = math.radians(theta)
	g = 9.8
	
	t_flight = 2*u*math.sin(theta)/g
	intervals = frange(0.0, t_flight, intervals)
	
	x = []
	y = []
	for t in intervals:
		x.append(u*math.cos(theta)*t)
		y.append(u*math.sin(theta)*t - 0.5*g*t*t)
	
	draw_graph(x, y)
	
	
if __name__ == '__main__':
	u_list = []
	theta_list = []
	print('Enter q to quit or s to show graph.')
	while True:
		try:
			u = input('Enter the initial velocity (m/s): ')
			if u == 'q' or u == 's':
				break
			u = float(u)
			theta = input('Enter the angle of projection (degrees): ')
			if theta == 'q':
				break
			theta = float(theta)
		except ValueError:
			print('You entered invalid input')
		else:
			u_list.append(u)
			theta_list.append(theta)
	data = zip(u_list, theta_list)
	leg = []
	if data and u == 's':
		for u, theta in data:
			s = "{:.1f} m/s, {:.1f} degree".format(u, theta)
			leg.append(s)
			draw_trajectory(u, theta)
		
		print("\nYou entered :")
		print("\n".join(leg))
		plt.legend(leg)
		plt.show()
	
