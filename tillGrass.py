def create_task(min_x, max_x):
	def task():
		while True:
			size = get_world_size()
			for _ in range(size):
				if get_ground_type() == Grounds.Soil:
					till()
				move(North)
			if get_pos_x() < max_x:
				move(East)
			else:
				while get_pos_x() > min_x:
					move(West)
	return task

size = get_world_size()
num_drones = 4
cols_per_drone = size // num_drones

for i in range(num_drones):
	start_x = i * cols_per_drone
	if i == num_drones - 1:
		end_x = size - 1
	else:
		end_x = (i + 1) * cols_per_drone - 1
	
	while get_pos_x() < start_x:
		move(East)
		
	logic = create_task(start_x, end_x)
	if not spawn_drone(logic):
		logic()

while get_pos_x() != 0:
	move(West)
while get_pos_y() != 0:
	move(South)