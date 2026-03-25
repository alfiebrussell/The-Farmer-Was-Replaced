def is_field_ready():
	size = get_world_size()
	for x in range(size):
		for y in range(size):
			
			if get_entity_type() != Entities.Pumpkin:
				return False
	return True