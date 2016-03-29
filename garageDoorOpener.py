#! Python 3.5
# Garage Door Opener exercise






# machine states
door_state = 'CLOSED'
door_reversed = ''





def command():

	global door_state
	global door_reversed
	commandInput = input('input command\n')

	if commandInput == 'button_clicked' and door_state == 'CLOSED':
		door_state = 'OPENING'
		print(door_state)
		return door_state, door_reversed

	elif commandInput == 'button_clicked' and door_state == 'OPENED':
		door_state = 'CLOSING'
		print(door_state)

	elif commandInput == 'button_clicked' and door_state == 'OPENING':
		door_state = 'STOPPED_WHILE_CLOSING'
		door_reversed = '0'
		print(door_state)

	elif commandInput == 'button_clicked' and door_state == 'CLOSING':
		door_state = 'STOPPED_WHILE_CLOSING'
		door_reversed = '1'
		print(door_state)

	elif commandInput == 'button_clicked' and door_state == 'STOPPED_WHILE_CLOSING' and door_reversed == '0':
		door_state = 'CLOSING'
		print(door_state)

	

	elif commandInput == 'button_clicked' and door_state == 'STOPPED_WHILE_CLOSING' and door_reversed == '1':
		door_state = 'OPENING'
		print(door_state)




	elif commandInput == 'cycle_complete' and door_state == 'OPENING':
		door_state = 'OPENED'
		print(door_state)

	elif commandInput == 'cycle_complete' and door_state == 'CLOSING':
		door_state = 'CLOSED'
		print(door_state)

	else:
		print('?????')






command()
command()
command()




