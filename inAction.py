import matplotlib.pyplot as plt
import matplotlib.animation as animation
from math import sqrt
import random
from Perceptron import *
from Point import *

width = 500
height = 500
num = 300
points = []
xdata, ydata = [], []
count = 0
anim_running = True

def f(x, width, height):
	normX = (x - -width)/(width - -width)
	normY = 0.3 * normX + 0.2
	y = normY * height * 2 - height
	return y

def animate(i):
	ax.clear()
	plt.autoscale(enable=False, axis='both', )
	ax.set_xlim(-width, width)
	ax.set_ylim(-height, height)
	ax.plot([-width, width], [f(-width, width, height), f(width, width, height)], color = 'c')

	global count
	for point in points:
		inputs = [point.x, point.y, point.bias]
		target = point.label
		guess = brain.guess(inputs)
		
		if point.label == 1:
			circle = plt.Circle((point.x, point.y), 10, color='k', fill=True)
		else:
			circle = plt.Circle((point.x, point.y), 10, color='k', fill=False)
		ax.add_artist(circle)

		if guess == target:
			circle = plt.Circle((point.x, point.y), 2, color='g')
		else:
			circle = plt.Circle((point.x, point.y), 2, color='r')
		ax.add_artist(circle)

	ax.plot([-width, width], [brain.guessY(-width), brain.guessY(width)], color = 'm')
	
	for i in range(1):
		point = points[count]
		inputs = [point.x, point.y, point.bias]
		target = point.label
		brain.train(inputs, target)
		
		count += 1
		if count == len(points):
			count = 0


	

def onClick(event):
    global anim_running
    if anim_running:
        ani.event_source.stop()
        anim_running = False
    else:
        ani.event_source.start()
        anim_running = True


brain = Perceptron(lr=0.1)

for i in range(num):
	points.append(Point(width, height))

fig, ax = plt.subplots()
plt.autoscale(enable=False, axis='both', )
ax.set_xlim(-width, width)
ax.set_ylim(-height, height)

fig.canvas.mpl_connect('button_press_event', onClick)

ani = animation.FuncAnimation(fig, animate, interval=1)

plt.show()
