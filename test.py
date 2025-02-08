from Game_of_Life import next_board_state 

if __name__ == "__main__":
	#Dead cells with no live neighbours should stay dead.
	init_state1 = [
				[0, 0, 0], 
				[0, 0, 0], 
				[0, 0, 0]
						]
	expected_state1 = [
				[0, 0, 0], 
				[0, 0, 0], 
				[0, 0, 0]
						]
	actual_state1 = (next_board_state(init_state1))

	if expected_state1 == actual_state1:
		print ("Test 1 is success.")
	else: 
		print("Error on Test 1")
		print("Expected Output", expected_state1)
		print ("Actual Output", actual_state1)

	#Dead cells with exactly 3 neighbours should come to life.
	init_state2 = [
				[0, 1, 0], 
				[1, 1, 0], 
				[0, 0, 0]
						]
	expected_state2 = [
				[1, 1, 0], 
				[1, 1, 0], 
				[0, 0, 0]
						]
	actual_state2 = (next_board_state(init_state2))

	if expected_state2 == actual_state2:
		print ("Test 2 is success.")
	else: 
		print("Error on Test 2")
		print("Expected Output", expected_state2)
		print ("Actual Output", actual_state2)

	#Alive Cells cells with no neighbours, or less than 2 neighbours should die.
	init_state3 = [
				[1, 0, 0], 
				[0, 0, 1], 
				[1, 0, 1]
						]
	expected_state3 = [
				[0, 0, 0], 
				[0, 0, 0], 
				[0, 1, 0]
						]
	actual_state3 = (next_board_state(init_state3))

	if expected_state3 == actual_state3:
		print ("Test 3 is success.")
	else: 
		print("Error on Test 3")
		print("Expected Output", expected_state3)
		print ("Actual Output", actual_state3)

	#Alive Cells cells with 2 or 3 neighbours should survive
	init_state4 = [
				[1, 0, 0], 
				[0, 1, 1], 
				[0, 1, 0]
						]
	expected_state4 = [
				[0, 1, 0], 
				[1, 1, 1], 
				[0, 1, 1]
						]
	actual_state4 = (next_board_state(init_state4))

	if expected_state4 == actual_state4:
		print ("Test 4 is success.")
	else: 
		print("Error on Test 4")
		print("Expected Output", expected_state4)
		print ("Actual Output", actual_state4)
		

#Alive Cells cells with more than 3 neighbours should die
	init_state5 = [
				[1, 1, 0], 
				[1, 1, 1], 
				[0, 0, 0]
						]
	expected_state5 = [
				[1, 0, 1], 
				[1, 0, 1], 
				[0, 1, 0]
						]
	actual_state5 = (next_board_state(init_state5))

	if expected_state5 == actual_state5:
		print ("Test 5 is success.")
	else: 
		print("Error on Test 5")
		print("Expected Output", expected_state5)
		print ("Actual Output", actual_state5)