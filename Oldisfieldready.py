def is_field_ready():
	yMeasure = 0
	xMeasure = 0
	if get_pos_x() == 0:
		xMeasure = measure()
	if get_pos_y() == 21:
		yMeasure = measure()
	if xMeasure == yMeasure:
		return True
	else:
		return False