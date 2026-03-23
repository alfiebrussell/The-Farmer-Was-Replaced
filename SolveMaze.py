import CreateMaze
import TreasureHunt
while True:
	change_hat(Hats.Gold_Hat)
	if CreateMaze.create_maze():
		if TreasureHunt.treasure_hunt():
			spawn_drone(TreasureHunt.treasure_hunt)
			continue

	