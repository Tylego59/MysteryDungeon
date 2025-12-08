from py4godot.classes.Area2D import Area2D
from py4godot import gdproperty, gdclass, gdnativetype

@gdclass
class Player(Area2D):
	speed: int = gdproperty(gdnativetype(int), 400)
