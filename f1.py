import FixLocation
import WaterdefNoPlant

while True:

	if get_entity_type() == Entities.Pumpkin:
		use_item(Items.Water)
	# 4. MOVEMENT LOGIC (Snake Pattern)
	x = get_pos_x()
	y = get_pos_y()
	size = get_world_size() # Using world size is better than hardcoding 5
		
	if x % 2 == 0:
		if y < size - 1:
			move(North)
		else:
			move(East)
	else:
		if y > 0:
			move(South)
		else:
			if x == size - 1: 
				while get_pos_x() > 0:
					move(West)
			else:
				move(East)