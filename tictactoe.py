#!/usr/local/bin/python3.3

board = ["" for i in range(9)]

def game():
	row1 = "| {} | {} | {} |".format(board[0],board[1],board[2])
	row2 = "| {} | {} | {} |".format(board[3],board[4],board[5])
	row3 = "| {} | {} | {} |".format(board[6],board[7],board[8])
	print()
	print(row1)	
	print(row2)
	print(row3)
	print()

def is_won(icon):
	if (board[0] == icon and board[1] == icon and board[2] == icon) or\
	   (board[3] == icon and board[4] == icon and board[5] == icon) or\
	   (board[6] == icon and board[7] == icon and board[8] == icon) or\
	   (board[0] == icon and board[3] == icon and board[6] == icon) or\
	   (board[1] == icon and board[4] == icon and board[7] == icon) or\
	   (board[2] == icon and board[5] == icon and board[8] == icon) or\
	   (board[0] == icon and board[4] == icon and board[8] == icon):
	   return True
	else:
	   	False 

def draw():
	if "" not in board:
		return True
	else:
		False
		
def player_move(icon):
	if icon == "X":
		number = 1
	elif icon == "O":
		number = 2
	choice = int(input("Player{} (1-9): ".format(number)).strip())
	if board[choice - 1] == "":
		board[choice - 1] = icon
	else:
		print("The Number is Already Taken")	

while True:
	game()
	player_move("X")
	game()
	if is_won("X"):
		print("X!!! WIN")
		break
	elif draw():
		print("Its Draw")
		break
	player_move("O")
	game()
	if is_won("O"):
		print("O!! WIN")
		break
	elif draw():
		print("Its Draw")
		break
	
	
	
	




