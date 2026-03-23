import Waterdef
		
def work_column():
	size = get_world_size()
	for _ in range(size):	
		if can_harvest():
			harvest()
			plant(Entities.Carrot)
			Waterdef.useWater(Entities.Carrot)
		else:
			plant(Entities.Carrot)
			Waterdef.useWater(Entities.Carrot)
		move(North)
		
			


while True:
	size = get_world_size()
	
	
	for x in range(size):
		if not spawn_drone(work_column):
			work_column() 
		move(East)

	
	
	while get_pos_x() > 0: 
		move(West)
	while get_pos_y() > 0: 
		move(South)