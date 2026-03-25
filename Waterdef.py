def useWater(plantType):
	while get_water() < 0.99:
		if num_items(Items.Water) > 1:
			use_item(Items.Water)
			get_water()
		break
	if num_items(Items.Fertilizer) > 0:
		use_item(Items.Fertilizer)
		harvest()
		plant(plantType)
		
		