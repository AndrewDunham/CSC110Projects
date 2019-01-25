#Andrew Dunham
#V00908230
#December 3, 2018

import Die
import SL_Board
import Player

def main():
	# Your code goes here
	#Add and document suitable functions

	#Setting 
	die = Die.Die()
	p1 = Player.Player()
	p2 = Player.Player()
	board = boardData()

	#setting the players names
	p1.set_name("Aaron")
	p2.set_name("Quinn")
	#Setting the symbols so that players are identifited as different
	p1.set_symbol()
	p2.set_symbol()
	#If on the rare occasion both players symbols are the same, then loop until the symbols are different
	while p1.get_symbol() == p2.get_symbol():
		p1.set_symbol()
		p2.set_symbol()

	#Printing out needed statements. 
	print("\n\nSNAKES AND LADDERS")
	print("\nThe board:")
	print(board)
	print("Player 1 = ",p1)
	print("Player 2 = ",p2)

	#Setting starting turn
	whosTurn = "p1"
	#Looping through the turns until finished with the game.
	while p1.get_position or p2.get_positions < board.get_length:
		if whosTurn == "p1":
			playerFunction(die, p1, board)
			whosTurn = "p2"
		elif whosTurn == "p2":
			playerFunction(die, p2, board)
			whosTurn = "p1"

def playerFunction(die, currentPlayer, board):
	#Throwing die
	die.throw()
	#Check the value of the die.
	checkDie = die.get_faceUp()
	#Set new position of the player
	newPosition = (currentPlayer.get_position() + checkDie)
	#If the player position is greater than the board length, set board length to 
	if newPosition > board.get_length():
		currentPlayer.set_position(board.get_length())
		print(currentPlayer)
		#Because the player has reached the end of the board, print that they have won.
		print("WINNER", currentPlayer.get_name(),currentPlayer.get_symbol())
		quit()#Quit the program as the loop is infinite.

	else:
		#If the new position is on a ladder go to the end of the ladder
		if board.is_ladder(newPosition):
			newPosition = board.get_ladder_top(newPosition)
			currentPlayer.set_position(newPosition)
			print(currentPlayer)
		#If the new position is a snake, go to the end of the snake
		elif board.is_snake(newPosition):
			newPosition = board.get_snake_tail(newPosition)
			currentPlayer.set_position(newPosition)
			print(currentPlayer)
		else:
			#Set position of the player to the new position if it is not a snake or a ladder
			currentPlayer.set_position(newPosition)
			print(currentPlayer)




	

#This function can be called in your program. 	
def boardData():
	with open("boardConfig.txt","r") as fileHandle:
		size = int(fileHandle.readline().strip("\n"))
		snakeData = fileHandle.readline().split()
		for i in range(len(snakeData)):
			snakeData[i] = int(snakeData[i].strip("\n"))
		ladderData = fileHandle.readline().split()
		for i in range(len(ladderData)):
			ladderData[i] = int(ladderData[i].strip("\n"))
		
		# Convert snakes to a list of tuples
		snakes = []
		for i in range(0,len(snakeData)//2):
			snakes.append( (snakeData[2*i], snakeData[2*i+1]) )
		
		# Convert ladders to a list of tuples
		ladders = []
		for i in range(0,len(ladderData)//2):
			ladders.append( (ladderData[2*i], ladderData[2*i+1]) )
		newBoard = SL_Board.SL_Board(size,snakes,ladders)
		return newBoard

# Do not change anything below here. 		
if __name__ == "__main__":
	main()