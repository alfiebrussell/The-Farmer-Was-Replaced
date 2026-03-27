def is_field_ready():
	if get_pos_x() != 0 and get_pos_y() != 0:
		for i in range (0, get_pos_x()):
			move(West)
		for i in range (0, get_pos_y()):
			move(South)
	ZeroPosMeasure = measure()
	move(South)
	TopPMeasure = measure()
	move(North)
	if ZeroPosMeasure == TopPMeasure:
		return True
	else:
		return False
	