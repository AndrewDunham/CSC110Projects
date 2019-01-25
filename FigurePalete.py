# Edit this file for Assignment #3
# Andrew Dunham
# V00908230
# October 20, 2018

def main():
	cont = True

	#printing informative statements
	print("I N T E G E R   F I G U R E S\n\n")
	print("   1: Rectangle")
	print("   2: Square")
	print("   3: Diamond")
	print("   4: Horizontal Line")
	print("   5: Vertical Line")
	print("   6: Triangle (top left)")
	print("   7: Triangle (bottom right)\n")

	print("Input Line 1: 1-7 specifies shape (0 to end)")
	print("Input Line 2: Symbol (0-9)")
	print("Input Line 3: Shape size (integer)")
	print("Input Line 4 (for rectangle): Shape width (integer)\n")
	while (cont ==True):
		shape = int(input("Line 1: "))
		if (shape < 1) or (shape > 7):
			cont = False
		else:
			symbol = int(input("Line 2: "))
			size = int(input("Line 3: "))
			if (shape == 1):
				width = int(input("Line 4: "))
		

#Transfering the collected data from input to the correct shape functions
		if shape ==  1:
			height = size
			rectangle(symbol, height, width)	
		elif shape == 2:
			width = size
			square(symbol, width)
		elif shape == 3: 
			width = size
			diamond(symbol, width)
		elif shape == 4:
			length = size
			horizLine(symbol, length)
		elif shape == 5:
			length = size
			vertLine(symbol, length)
		elif shape == 6:
			width = size
			leftTopTriangle(symbol, width)
		elif shape == 7:
			height = size
			rightBottomTriangle(symbol, height)
			
#Defining how the shapes will react
def rectangle(symbol, height, width):
	print()
	for line in range(0, height):
		for character in range(0, width):
			print(symbol,".", sep='', end='')
		print()
	print()

def square(symbol, width):
	print()
	for line in range(0, width):
		for character in range(0, width):
			print(symbol, ".", sep = '', end ='')
		print()
	print()

def horizLine(symbol, length):
	print()
	for character in range(0, length):
		print(symbol, ".", sep='', end='')
	print()
	print()

def vertLine(symbol, length):
	print()
	for character in range(0, length):
		print(symbol, '.', sep='')
	print()

def diamond(symbol, width):
	height = width
	_total = height//2
	symbolTotal = 1
	print()
	if (height % 2) == 0:
		for line in range(height//2):
			for underscore in range((height//2) - line):
				print("_.", sep='', end='')
			for character in range(1+ (line*2)):
				print(symbol, ".", sep='', end='')
			print()
		for line in range(height//2):
			for underscore in range(line+1):
				print("_.", sep='', end='')
			for character in range((height-1)-(2*line)):
				print(symbol, ".", sep='', end='')
			print()
		print()
	else:
		for line in range(height):
			for underscore in range(_total):
				print("_.", sep='', end='')
			for character in range(symbolTotal):
				print(symbol, ".", sep='', end='')
			if line <= (height/2)-1:
				_total -= 1
				symbolTotal += 2
			else:
				_total += 1
				symbolTotal -= 2
			print()	
		print()	

def leftTopTriangle(symbol, height):
	print()
	for line in range(0, height):
		for character in range(0, (height - line)):
			print(symbol, ".", sep='', end='')
		print()
	print()

def rightBottomTriangle(symbol, height):
	print()
	for line in range(1, height +1):
		for character in range (1, height +1):
			if character <= (height - line):
				print("_.", sep='', end='')
			else:
				print(symbol, ".", sep='', end='')
		print()
	print()
	

# *** Do not edit anything below this line ***
if __name__ == "__main__":
	main()