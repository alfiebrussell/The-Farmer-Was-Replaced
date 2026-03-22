def useWater():
	while get_water() < 0.5:
		use_item(Items.Water)
		get_water()
		break