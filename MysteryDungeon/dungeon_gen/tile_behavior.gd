extends Node
enum TerrainType {FLOOR, WALL}
var terrain = TerrainType.FLOOR
func refresh_sprite():
	if terrain == TerrainType.WALL:
		
