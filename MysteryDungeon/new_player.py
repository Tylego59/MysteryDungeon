from py4godot.classes.Area2D import Area2D
from py4godot import gdproperty, gdclass
from py4godot.classes.core import Vector2

@gdclass
class Player(Area2D):
	
	speed: int = gdproperty(int, 400)
	screen_size: float = gdproperty(float, 0)
	
	def _ready(self):
		screen_size = get_viewport_rect().size
		
		
	def _process(self, delta:float):
		velocity: Vector2 = gdproperty(Vector2, Vector2.new0())
		if Input.is_action_pressed("right"):
			velocity.x += 1
		if Input.is_action_pressed("left"):
			velocity.x -= 1
		if Input.is_action_pressed("down"):
			velocity.y += 1
		if Input.is_action_pressed("up"):
			velocity.y -= 1
		
		if velocity.length() > 0:
			velocity = velocity.normalized() * speed
		
		position += velocity * delta
		position = position.clamp(Vector2.new0(), screen_size)
