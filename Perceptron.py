import random
def sign(n):
	if n>= 0:
		return 1
	else:
		return -1
 
class Perceptron(object):
	
	def __init__(self, n=3, lr=0.1):
		self.lr = 0.1
		self.weights = []
		for i in range(n):
			rand = random.random()
			self.weights.append(rand * random.randrange(-1, 1, 2))

	def guess(self, inputs):
		sum = 0
		for i in range(len(self.weights)):
			sum += inputs[i]*self.weights[i]

		output = sign(sum)
		return output
 
	def train(self, inputs, target):
		guess = self.guess(inputs)
		error = target - guess
		for i in range(len(self.weights)):
			self.weights[i] += error * inputs[i] * self.lr
	
	def guessY(self, x):
		return -(self.weights[2]/self.weights[1])-((self.weights[0]/self.weights[1])*x)