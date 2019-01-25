#CSC 110 201809 Assignment 4
#Andrew Dunham
#V00908230
#November 8, 2018

def main():
	print("MATRIX ARITHMETIC\n")
	print("Inputting Matrices A, B and D and scalar c . . . . . .")

	#Output file name
	outputFile = "MatrixResult.txt"

	#Clearout the file
	with open(outputFile, "w") as writtenFile:
		writtenFile.write("")

	reiteration = 0
	
	#Loop until unable to find another set of matrixes
	while(True):
		with open("MatrixIn.txt", "r") as readFile:
		#Go through all the lines in the file in intervals of 4 and break when finished
			try: 

				for num in range(0, reiteration * 4):
					lineJump = readFile.readline()

				A = getMatrix(readFile.readline())
				B = getMatrix(readFile.readline())
				c = int(readFile.readline())
				D = getMatrix(readFile.readline())
			except (ValueError):
				break
		#Write the Matrixes to to the outputFiles
		outputMatrix("A", A, outputFile)
		outputMatrix("B", B, outputFile)

		with open(outputFile, 'a') as writtenFile:
			writtenFile.write("c=\t" + str(c) + "\n")

		outputMatrix("D", D, outputFile)

		outputMatrix("A+B", addMatrix(A,B), outputFile)
		outputMatrix("A-C", subtractMatrix(A,B), outputFile)
		outputMatrix("cA", scalarMultiply(c,A), outputFile)
		outputMatrix("A dot D", dot(A, D), outputFile)
		#reiterate + 1
		reiteration += 1

	print(". . . . Result Written to file: MatrixResult.txt")
	
def getMatrix(inFileHandle):
# returns a 2-dimensional list:
# containing a matrix whose data was in the file
	array = inFileHandle.split(" ")
	
	#Empty Matrix with correct length
	Matrix = [[0 for num in range(int(array[1]))] for num2 in range(int(array[0]))]
	
	for num in range(0, int(array[0])):
		for num2 in range(0, int(array[1])):
			Matrix[num][num2] = int(array[int(num * int(array[1])) + num2 + 2])
			
	return(Matrix)

def addMatrix(one, theOther):
# returns a 2-dimensional list: the sum of one + theOther

	rangeOfX = len(one[0])
	rangeOfY = len(one)

	matrixSum = [[0 for num in range(rangeOfX)] for num2 in range(rangeOfY)]

	for num in range (rangeOfY):
		for num2 in range(rangeOfY):
			matrixSum[num][num2] = one[num][num2] + theOther[num][num2]

	return(matrixSum)

def subtractMatrix(one, theOther):
# returns a 2-dimensional list: the difference: one - theOther
	
	rangeOfX = len(one[0])
	rangeOfY = len(one)

	matrixSum = [[0 for num in range(rangeOfX)] for num2 in range(rangeOfY)]

	for num in range (rangeOfY):
		for num2 in range(rangeOfY):
			matrixSum[num][num2] = one[num][num2] - theOther[num][num2]

	return(matrixSum)

def scalarMultiply(scalar, matrix):
#returns the matrix product of (scalar value) * matrix
	scalMatrix = [[0 for num in range(len(matrix[0]))] for num2 in range(len(matrix))]
	
	for num in range(len(matrix)):
		for num2 in range(len(matrix[0])):
			scalMatrix[num][num2] = matrix[num][num2] * scalar
			
	return(scalMatrix)


def dot(one, theOther):
#returns the matrix dot product: one <dot> theOther
	rangeOfX = max(len(one[0]), len(theOther[0]))
	rangeOfY = max(len(one), len(theOther))

	dotproMatrix = [[0 for num in range(rangeOfX)] for num2 in range(rangeOfY)]

	for num in range(0, rangeOfY):
		for num2 in range(0, rangeOfX):
			for num3 in range(0, len(one[0])):
				dotproMatrix[num][num2] += one[num][num3] * theOther[num3][num2]
	return(dotproMatrix)

def outputMatrix(name,matrix, outFileHandle):
#writes the name, an ‘=’ and a matrix to the opened file
#pointed to by outFileHandle
	with open(outFileHandle, 'a') as writtenFile:
		writtenFile.write(str(name) + "=")

		for num in range(len(matrix)):
			for num2 in range(len(matrix[0])):
				writtenFile.write("\t" + str(matrix[num][num2]))
			writtenFile.write("\n")


# Do not change *anything* below this line
if __name__ == "__main__":
	main()