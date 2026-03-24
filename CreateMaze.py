def create_maze():
	clear()
	plant(Entities.Bush)
	while get_entity_type()==Entities.Bush:
			if num_items(Items.Weird_Substance) > get_world_size():
				use_item(Items.Weird_Substance, get_world_size())
				return 1
			if can_harvest():
				harvest()
				plant(Entities.Bush)
			if num_items(Items.Fertilizer)==0:
				# I do not have trade unlocked
				#trade(Items.Fertilizer)
				return 0
			
			use_item(Items.Fertilizer)

	return 1
