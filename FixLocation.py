x = get_pos_x()
y = get_pos_y()

if y != 0:
	move(South)
	
else:
	# If we are at the last column (x=5) and at the bottom (y=0)
	if x != 0: 
		move(West)
		