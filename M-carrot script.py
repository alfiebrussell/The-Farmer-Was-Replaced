import Waterdef
		
def work_column():
	size = get_world_size()
	for _ in range(size):	
		if can_harvest():
			harvest()
			change_hat(Hats.Pumpkin_Hat)
			plant(Entities.Carrot)
			#Waterdef.useWater(Entities.Carrot)
			if num_items(Items.Fertilizer) > 0:
				
				harvest()
				plant(Entities.Carrot)
				use_item(Items.Fertilizer)
		else:
			plant(Entities.Carrot)
			#Waterdef.useWater(Entities.Carrot)
			if num_items(Items.Fertilizer) > 0:
				harvest()
				plant(Entities.Carrot)
				use_item(Items.Fertilizer)
		move(North)
		
			


while True:
	size = get_world_size()
	
	
	for x in range(size):
		if not spawn_drone(work_column):
			change_hat(Hats.Pumpkin_Hat)
			work_column() 
		move(East)

	
	
	while get_pos_x() > 0: 
		move(West)
	while get_pos_y() > 0: 
		move(South)