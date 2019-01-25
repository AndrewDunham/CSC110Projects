#Andrew Dunham
#V00908230
#December 3, 2018

import random
import string

class Player:

	def __init__(self):
	#Initializes the data attributes self.__name and self.__symbol, both should
	#be empty strings. It also initializes the attribute self.__position to 1.
		self.__name = ""
		self.__symbol = ""
		self.__position = 1

	def set_name(self, name):
	#	Changes the attribute self.__name to the parameter passed as name
		self.__name = name

	def set_symbol(self):
	#	Changes the attribute self.__symbol to a random character in the range ‘a’ to 
	#	‘z’ (inclusive of both ‘a’ and ‘z’).
	#	Getting a random letter
		randLetters = string.ascii_letters
		self.__symbol = random.choice(randLetters).lower()

	def get_name(self):
	#	returns the current value of the self.__name attribute
		return self.__name
		
	def get_symbol(self):
	#	returns the current value of the self.__symbol attribute
		return self.__symbol

	def set_position(self, position):
	#	Changes the attribute self.__position to the parameter passed as position.
		self.__position = position

	def get_position(self):
	#	returns the current value of the self.__position attribute
		return self.__position

	def __str__(self):
	#	returns a string that contains the current value of each of the three attributes in the following format:
	#	valueofself.__name (valueofself.__symbol): self.__position
		return self.__name + "(" + self.__symbol + "): " + str(self.__position)