import math

class Simple:
	
	def __init__(self, axis, ordinate):
		self.axis = axis
		self.ordinate = ordinate

	def pythagoras(self):

		x = self.axis
		y = self.ordinate

		return math.sqrt(x * x + y * y)
