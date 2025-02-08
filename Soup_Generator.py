import Game_of_Life
import time
#import os

if __name__ == "__main__":
	def generate_soup(initial_state):
		Game_of_Life.render_board(initial_state)
		count = 20
		next_state = Game_of_Life.next_board_state(initial_state)

		while count != 0:
			print('')
			Game_of_Life.render_board(next_state)
			next_state = Game_of_Life.next_board_state(next_state)
			#count = count - 1
			#os.system('cls')
			time.sleep(0.05)
			print('\033[70A\033[2K', end='')

	
	init_state = Game_of_Life.random_state(70, 270)
	generate_soup(init_state)
