# Import core classes
from py4godot.classes.Area2D import Area2D
from py4godot.classes.core import Vector2
from py4godot.classes.Input import Input
from py4godot.classes.DisplayServer import DisplayServer

# Import py4godot decorators and types
from py4godot import gdproperty, gdclass

@gdclass
class Player(Area2D):
	"""
	Area2D-based movement script compatible with py4godot.
	This uses manual position updates, as is common for Area2D nodes.
	"""
	
	# 1. EXPORTED PROPERTIES (Metadata)
	# The float type should be used for better compatibility with delta time calculations.
	speed: float = gdproperty(float, 400.0)
	
	# Internal class variables
	screen_size: Vector2 = Vector2.new0()
	input_instance: Input = None
	
	def _init(self) -> None:
		"""Required for py4godot compatibility."""
		pass
		
	def _ready(self) -> None:
		"""
		Called when the node is ready. Sets up singleton access and screen size.
		"""
		# Get Singleton Instances
		self.input_instance = Input.get_instance()
		
		# Access the DisplayServer to get screen size (Viewport is also an option)
		display_server = DisplayServer.get_instance()
		self.screen_size = display_server.screen_get_size()
		
		print(f"Player initialized. Screen size: ({self.screen_size.x}, {self.screen_size.y})")
		
		
	def _process(self, delta: float) -> None:
		"""
		Called every frame. Handles input and manual position updating.
		"""
		# 1. Set velocity to zero initially
		velocity: Vector2 = Vector2.new0()
		
		# 2. Get Input using the singleton instance
		if self.input_instance.is_action_pressed("right"):
			velocity.x += 1.0
		if self.input_instance.is_action_pressed("left"):
			velocity.x -= 1.0
		if self.input_instance.is_action_pressed("down"):
			velocity.y += 1.0
		if self.input_instance.is_action_pressed("up"):
			velocity.y -= 1.0
		
		# 3. Calculate final velocity
		if velocity.length_squared() > 0:
			# Normalize and apply speed (using self.speed)
			velocity = velocity.normalized() * self.speed
			
		# 4. Calculate new position
		new_position = self.get_position() + velocity * delta
		
		# 5. Clamp the position to keep the player on screen
		# Note: Vector2.new0() is (0, 0)
		# We assume get_position() and set_position() methods exist for Area2D
		# Clamping ensures the new position is between (0, 0) and the screen size.
		new_position.x = max(0.0, min(new_position.x, self.screen_size.x))
		new_position.y = max(0.0, min(new_position.y, self.screen_size.y))
		
		# 6. Apply the new position
		self.set_position(new_position)
		
		# Optional Debugging:
		# print(f"Pos: ({new_position.x:.1f}, {new_position.y:.1f}), Speed: {self.speed}")
