#CSC 110 201809 Assignment 5
#Andrew Dunham
#V00908230
#November 22, 2018

def main():
	#Setting and opening the files
	inputFile = open("storyIn.txt", "r")
	outputFile = open("analysisOut.txt", "w")

	#Spliting the file into a list.
	wordlist = inputFile.read().split()
	
	#Ignore the following characters for wordlist.
	wordlist = [string.replace('(', '') for string in wordlist]
	wordlist = [string.replace(')', '') for string in wordlist]
	wordlist = [string.replace('?', '') for string in wordlist]
	wordlist = [string.replace('!', '') for string in wordlist]
	wordlist = [string.replace(',', '') for string in wordlist]
	wordlist = [string.replace('.', '') for string in wordlist]
	wordlist = [string.replace(';', '') for string in wordlist]
	wordlist = [string.replace(':', '') for string in wordlist]
	wordlist = [string.replace(' ', '') for string in wordlist]
	wordlist = [string.replace('\n', '') for string in wordlist]


	#Converting list into lowercase only.
	lowerList = map(lambda item:item.lower(), wordlist)

	#send data to the wordTotal function and return with the correct information.
	wTotal = wordTotal(wordlist)
	#Output the word total to the output file.
	outputFile.write("Words:" + str(wTotal) + "\n")

	#Send data to the wordFrequency function and return with the dictionary of information.
	wFrequency = wordFrequency(lowerList)
	#Output the word frequency to the output file.
	for itemKey in sorted(wFrequency.keys()):
		outputFile.write (str(wFrequency[itemKey]) + ": " + str(itemKey)+ "\n")

	#Send data to letterCount function and return with both variables.
	upper, lower = letterCount(wordlist)
	#Ouput upper and lowercase counts to the output file.
	outputFile.write("Upper Case Letters: " + str(upper) + "\n")
	outputFile.write("Lower Case Letters: " + str(lower) + "\n")

	#Send data to the letterFrequency function and return with the dictionary of information. 
	lFrequency = letterFrequency(wordlist)
	#Output the dictionary information to the output file.
	for itemKey in sorted(lFrequency.keys()):
		outputFile.write (str(itemKey) + ": " + str(lFrequency[itemKey])+ "\n")

def wordTotal(wordlist):
# Input: a 1 dimensional list of words
# Returns: an integer, the number of words
	wordCount = 0
	for word in wordlist:
		wordCount += 1

	#print("Words:", wordCount,sep = '')
	return(wordCount)

def wordFrequency(wordlist):
# Input: a 1 dimensional list of words
# Returns: a dictionary with key = word (string)
# and value = number of occurrences

	
	#initializing empty dictionary
	wordCounter = {}

	#loop through every word in the wordlist
	for item in wordlist:
		if item not in wordCounter:
			wordCounter[item] = 1
		else:
			wordCounter[item] += 1

	#Return information
	return(wordCounter)

def letterCount(wordlist):
# Input: a 1 dimensional list of words
# Returns: two integers: count of lower case letters
# and count of upper case letters

	#Empty integer variables to store values in.
	lowerCase = 0
	upperCase = 0

	#Changing list into a string to be able to correctly identify upper or lower case characters.
	stringified = ''.join(wordlist)

	#Loop through ever letter and save to the specific variable depending on if the letter is upper or lowercase
	for letter in stringified:
		if (letter.islower()):
			lowerCase += 1
		if (letter.isupper()):
			upperCase = upperCase + 1

	#Return the information.
	return(upperCase, lowerCase)

def letterFrequency(wordlist):
# Input: a 1 dimensional list of words
# Returns: a dictionary with key = alpha-numeric
# letters and value = number of occurrences

	#Creating an empty dictionary to store the letter frequency in.
	letterCounter = {}

	#Change the wordlist into one single concatenated string to more easily find letter frequency. 
	stringified = ''.join(wordlist)

	#Loop through each letter that is found in the lengthy string.
	for letter in stringified:
		if letter not in letterCounter:
				letterCounter[letter] = 1
		else:
			letterCounter[letter] += 1

	#return the filled dictionary
	return(letterCounter)

# Do not change *anything* below this line
if __name__ == "__main__":
	main()
	