while True:
	change_hat(Hats.Purple_Hat)
	if can_harvest():
		harvest()
		plant(Entities.Bush)
	else:
		plant(Entities.Bush)

		

	x = get_pos_x()
	y = get_pos_y()
		
	# If X is even (0, 2, 4...)
	if x % 2 == 0:
		if y < 5:
			move(North)
		else:
			move(East)
	# If X is odd (1, 3, 5...)
	else:
		if y > 0:
			move(South)
		else:
			# If we are at the last column (x=5) and at the bottom (y=0)
			if x == 5: 
				while get_pos_x() > 0:
					move(West)
			else:
				move(East)