import random

def random_state(height, width):
	board_state = [[0 for x in range(width)] for x in range(height)]
	for row in range(height):
		for column in range(width):
			seed = random.random()
			if seed > 0.5:
				board_state[row][column] = 1
			else: 
				board_state[row][column] = 0 
	return board_state

def render_board(board_state):
	#print ("-"*(len(board_state[0])+2))
	for count in range(len(board_state)):
		line = "|"
		for item in (board_state[count]):
			if item == 1:
				line = line + "■"
			else: 
				line = line + " "
		line += "|"
		print(line)
	#print ("-"*(len(board_state[0])+2))

def next_board_state(board_state):
	rows = len(board_state)
	columns = len(board_state[0])
	
	next_state = [[0 for x in range(columns)] for x in range(rows)]

	neighbour_directions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (+1, 0), (-1, +1), (0, +1), (+1, +1)]
	cell_state = 0
	#count = 0

	for row in range(rows):
		for column in range(columns):

			live_cell_count = 0

			if board_state[row][column] == 1:
				cell_state = 1
				
			for x, y in neighbour_directions:

				neighbour_row = row + x
				neighbour_column = column + y
				
				if (neighbour_row >= 0 and neighbour_row < rows) and (neighbour_column >=0 and neighbour_column < columns):
					if board_state[neighbour_row][neighbour_column] == 1:
						#print ("One Neightbour at " + str(neighbour_row+1) + " " + str(neighbour_column+1))
						live_cell_count += 1

			if live_cell_count > 3:
				next_state[row][column] = 0
				#print ("Dead from overpopulation")

			elif live_cell_count == 3 and cell_state == 0:
				next_state[row][column] = 1
				#print("Reproduction gives life")

			elif cell_state == 1 and (live_cell_count >= 2 and live_cell_count <= 3):
				next_state[row][column] = 1
				#print ("Survives")

			elif cell_state == 1 and live_cell_count < 2:
				next_state[row][column] = 0
				#print("Dead from underpopulation")

			
			cell_state = 0

			#count += 1
			#print ("Cell", str(count)+ " completed, had " + str(live_cell_count) + " neighbours. Moving to next cell")


	return	(next_state)



			#if (row == 0) or (row == rows - 1) or (column == 0) or (column == columns - 1):
				#if (row == 0 and column == 0) or (row == 0 and column == columns -1) or (row == rows - 1 and column == 0) or (row == rows - 1 and column == columns - 1):
					#print (str(row) + str(column) + "There are 3 neighbours")
				#else:
					#print (str(row) + str(column) + "There are 5 neighbours")
			#else:
				#print (str(row) + str(column) +  "There are 8 neighbours")

#render_board(random_state(40, 100))

