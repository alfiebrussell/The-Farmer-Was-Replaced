def useWater():
	while get_water() < 0.5:
		if num_items(Items.Water) > 1:
			use_item(Items.Water)
		break