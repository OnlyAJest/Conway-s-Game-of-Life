import Game_of_Life

if __name__ == "__main__":
	init_state = Game_of_Life.load_board(r"C:\Users\Administrator\Desktop\The Game of Life\board.txt")
	Game_of_Life.run_game(init_state, 0.5)

