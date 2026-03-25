import WaterdefNoPlant
import isfieldready



def manage_pumpkin():
	# Check tile status
	entity = get_entity_type()
	
	# If dead, harvest and replant immediately
	if entity == Entities.Dead_Pumpkin:
		harvest()
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Pumpkin)
		WaterdefNoPlant.useWater()
	
	# If empty, plant immediately
	elif entity == None:
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Pumpkin)
		WaterdefNoPlant.useWater()
		
	# Always keep it watered
	WaterdefNoPlant.get_water()

def create_task(min_x, max_x):
	def task():
		while True:
			size = get_world_size()
			
			#Work strictly within assigned columns
			for x in range(min_x, max_x + 1):
				# Move to the specific column
				while get_pos_x() < x:
					move(East)
				while get_pos_x() > x:
					move(West)
				
				# Zig zag through the rows to ensure every tile is checked
				for i in range(size):
					y = i
					if x % 2 != 0:
						y = (size - 1) - i
						
					while get_pos_y() < y:
						move(North)
					while get_pos_y() > y:
						move(South)
					
					# Function call to Replant/Water this specific tile
					manage_pumpkin()

			# Pumpkin Trigger (Leader Drone Only)
			if min_x == 0:
				# Move to 0,0 quickly
				while get_pos_x() > 0:
					move(West)
				while get_pos_y() > 0:
					move(South)
				
			
				if isfieldready.is_field_ready() == True:
					harvest()
				else:
					continue
				
				# Return to start of lane 0 immediately
				while get_pos_y() > 0:
					move(South)
				while get_pos_x() > 0:
					move(West)
			
	return task

# --- Initialize ---
change_hat(Hats.Traffic_Cone)

size = get_world_size() # 22
num_drones = 4
cols_per_drone = size // num_drones

for i in range(num_drones):
	start_x = i * cols_per_drone
	if i == num_drones - 1:
		end_x = size - 1
	else:
		end_x = (i + 1) * cols_per_drone - 1
	
	# Position the player to spawn the drone in its own lane
	while get_pos_x() < start_x:
		move(East)
	while get_pos_x() > start_x:
		move(West)
		
	logic = create_task(start_x, end_x)
	if not spawn_drone(logic):
		logic()