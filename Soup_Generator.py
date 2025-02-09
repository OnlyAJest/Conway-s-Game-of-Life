import Game_of_Life
import time
#import os

if __name__ == "__main__":
	init_state = Game_of_Life.random_state(70, 280)
	Game_of_Life.run_game(init_state, 0.05)
