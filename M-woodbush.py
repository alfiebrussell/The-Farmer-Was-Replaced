		
import FixLocation
import WaterdefNoPlant

def create_workrule(min_x, max_x):
	def drone_logic():
		while True:
			x = get_pos_x()
			y = get_pos_y()
			world_size = get_world_size()
			
			# --- TILE LOGIC ---
			if (x + y) % 2 == 0:
				# Tree Tile Logic
				if can_harvest():
					harvest()
				
				if get_ground_type() == Grounds.Grassland:
					till()
					WaterdefNoPlant.useWater()
					
				plant(Entities.Tree)
				use_item(Items.Water)
				use_item(Items.Water)
				WaterdefNoPlant.useWater()
				if num_items(Items.Fertilizer) > 0:
					
					harvest()
					plant(Entities.Tree)
					use_item(Items.Fertilizer)
				
			else:
				# --- GRASSLAND TILE LOGIC ---
				if can_harvest():
					harvest()
					plant(Entities.Bush)
					WaterdefNoPlant.useWater()
					if num_items(Items.Fertilizer) > 0:
						
						harvest()
						plant(Entities.Bush)
						use_item(Items.Fertilizer)
				# If this tile was previously Grassland, turn it back to Soil
				if get_ground_type() == Grounds.Soil:
					till()
					WaterdefNoPlant.useWater()
			
			# --- MOVEMENT LOGIC (Snake pattern within slice) ---
			if x % 2 == 0:
				# Even columns move North
				if y < world_size - 1:
					move(North)
				else:
					# At the top of the column
					if x < max_x:
						move(East)
					else:
						# Reached the end of the drone's section
						# Move back to start of section
						while get_pos_x() > min_x:
							move(West)
						while get_pos_y() > 0:
							move(South)
			else:
				# Odd columns move South
				if y > 0:
					move(South)
				else:
					# At the bottom of the column
					if x < max_x:
						move(East)
					else:
						# Reached the end of the drone's section
						while get_pos_x() > min_x:
							move(West)
	
	return drone_logic

# --- MAIN SETUP ---
size = get_world_size()
num_drones = 4
cols_per_drone = size // num_drones

for i in range(num_drones):
	# Calculate boundaries for this drone
	start_x = i * cols_per_drone
	
	# If it is the last drone, give it the remaining columns (in case size isn't divisible by 4)
	if i == num_drones - 1:
		end_x = size - 1
	else:
		end_x = (i + 1) * cols_per_drone - 1
	
	# Create the specialized logic for this drone's slice
	logic = create_workrule(start_x, end_x)
	
	# Move the main drone to the spawn starting point
	while get_pos_x() < start_x:
		move(East)
		
	# Attempt to spawn a drone; if fails, the main drone takes the last logic block
	if not spawn_drone(logic):
		logic()
