#Andrew Dunham
#V00908230
#December 3, 2018

import random

class Die:

	def __init__(self):
		#Initializes the data attribute self.__faceUp
		self.__faceup = 1

	def throw(self):
		#Uses a random number generate to change the __faceUp attribute.
		self.__faceUp = random.randint(1, 6)

	def get_faceUp(self):
		#Returns the current value of the __faceUp attribute.
		return self.__faceUp