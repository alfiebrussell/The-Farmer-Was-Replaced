import FixLocation
import WaterdefNoPlant

# Define the logic for a single tile
def manage_pumpkin():
	# If there's a dead pumpkin, we MUST harvest it to replant
	if get_entity_type() == Entities.Dead_Pumpkin:
		harvest()
	
	# If the ground is empty, till and plant
	if get_entity_type() == None:
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Pumpkin)
		
	# Always ensure it is watered
	WaterdefNoPlant.get_water()

# Define the logic for a drone (or farmer) to do one full column
def work_column():
	size = get_world_size()
	for _ in range(size):
		manage_pumpkin()
		move(North)

# Function to check if the entire field is full of pumpkins
def is_field_ready():
	size = get_world_size()
	for x in range(size):
		for y in range(size):
			#
			if get_entity_type() != Entities.Pumpkin:
				return False
			move(North)
		move(East)
	return True

# --- Main Execution ---
change_hat(Hats.Traffic_Cone)

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
	
	
	if is_field_ready():
		harvest()