from random import random, randrange

class Point(object):
	def __init__(self, width, height):
		self.y = random() * width * 2 - width # * randrange(-1, 1, 2)
		self.x = random() * height * 2 - height # * randrange(-1, 1, 2)
		self.bias = 1

		if f(self.x, width, height)>self.y:
			self.label = 1
		else:
			self.label = -1

def f(x, width, height):
	normX = (x - -width)/(width - -width)
	normY = 0.3 * normX + 0.2
	y = normY * height * 2 - height
	return y