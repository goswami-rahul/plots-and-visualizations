import matplotlib.pyplot as plt
import math
import matplotlib.animation

def frange(start, final, interval):
	numbers = []
	while start < final:
		numbers.append(start)
		start += interval
	return numbers

def update_pos(i, circle, intervals, u, theta):
	t = intervals[i]
	g = 0.98
	x = u*math.cos(theta)*t
	y = u*math.sin(theta)*t - 0.5*g*t*t
	circle.center = x, y
	return (circle,)  # returns a tuple

def animation(u, theta):
	
	size = 3 # size of point (keep it between [1 - 5])
	
	theta = math.radians(theta)
	g = 0.98
	t_flight = 2*u*math.sin(theta)/g
	intervals = frange(0.0, t_flight, 0.01*u)
	xmax = abs(int(u*math.cos(theta)*t_flight))
	xmax += xmax*0.1
	ymax = abs(int(u*math.sin(theta)*t_flight/2 - 0.5*g*(t_flight/2)**2))
	ymax += ymax*0.1
	mx = max(xmax, ymax)
	fig = plt.gcf()
	ax = plt.axes(xlim=(-mx, mx), ylim=(0, mx))
	ax.set_aspect("equal")
	circle = plt.Circle((0, 0), mx*0.01*size)
	ax.add_patch(circle)
	anim = matplotlib.animation.FuncAnimation(fig, update_pos, frames=len(intervals)
		, fargs=(circle, intervals, u, theta), interval=1, repeat_delay=1000)
	plt.title("Projectile Motion")
	plt.xlabel("X")
	plt.ylabel("Y")
	plt.show()

if __name__ == '__main__':
	try:
		u = float(input('Enter the initial velocity (m/s): '))
		theta = float(input('Enter the angle of projection (degree): '))
	except ValueError:
		print("Invalid input.")
	else:
		animation(u, theta)
