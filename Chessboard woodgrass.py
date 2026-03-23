import FixLocation
import WaterdefNoPlant


def workrule():
	while True:
		x = get_pos_x()
		y = get_pos_y()
	
		
		if (x + y) % 2 == 0:
			# --- TREE TILE LOGIC ---
			if can_harvest():
				harvest()
			# Trees have Soil.
			if get_ground_type() == Grounds.Grassland:
				till()
				WaterdefNoPlant.useWater()
				
			plant(Entities.Tree)
			use_item(Items.Water)
			use_item(Items.Water)
			WaterdefNoPlant.useWater()
			
		else:
			# --- GRASSLAND TILE LOGIC ---
			if can_harvest():
				harvest()
				WaterdefNoPlant.useWater()
			# If this tile was previously Soil, turn it back to Grassland
			if get_ground_type() == Grounds.Soil:
				till()
				WaterdefNoPlant.useWater()
			
			
	
		# --- MOVEMENT (SNAKE PATTERN) ---
		# Move North on even columns, South on odd columns
		if x % 2 == 0:
			if y < 5:
				move(North)
			else:
				move(East)
		else:
			if y > 0:
				move(South)
			else:
				# If we are at the bottom of the last column (x=5, y=0)
				if x == 5: 
					while get_pos_x() > 0:
						move(West)
						
				else:
					move(East)
					
while True:
	spawn_drone(workrule)
