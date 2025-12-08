# Import core classes used for movement and input
from py4godot.classes.core import Vector2
from py4godot.classes.CharacterBody2D import CharacterBody2D # Assuming this path
from py4godot.classes.Input import Input # Assuming this path

# Note: The older py4godot usually requires classes to be manually extended.
# No @gdclass decorator is typically needed for extending engine classes.

class Player(CharacterBody2D):
	"""
	Python script for a 2D top-down character using the older py4godot library structure.
	Uses simple, snappy movement (zero friction/deceleration).
	"""

	# --- Configuration Variables ---
	speed: float = 300.0  # Movement speed in pixels per second
	# FRICTION removed for simple movement

	# --- Godot Lifecycle Methods ---

	def _init(self) -> None:
		"""
		Added for compatibility. Older py4godot often requires an explicit
		initialization method for proper class registration.
		"""
		pass

	def _ready(self) -> None:
		"""
		Called when the node is ready.
		"""
		print("Player script is ready. Using simple movement.")
		# Initialize velocity to a zero vector.
		self.velocity = Vector2(0, 0)

	def _physics_process(self, delta: float) -> None:
		"""
		Called every physics frame. Handles movement input and physics.
		"""
		# 1. Get raw input direction as a normalized Vector2.
		input_x = (Input.get_action_strength("right") - 
				   Input.get_action_strength("left"))
		input_y = (Input.get_action_strength("down") - 
				   Input.get_action_strength("up"))

		input_vector = Vector2(input_x, input_y)
		
		# 2. Movement Calculation
		if input_vector.length_squared() > 0:
			# If there is input, set velocity based on speed.
			self.velocity = input_vector.normalized() * self.speed
		else:
			# If no input, stop immediately. (Simple Movement)
			self.velocity = Vector2(0, 0)

		# 3. Apply motion
		self.move_and_slide()
		
		# --- DEBUG: CHECK VELOCITY ---
		# If this prints a non-zero value, the code is working and the issue is configuration.
		if self.velocity.length_squared() > 1:
			 print(f"Velocity is: ({self.velocity.x:.2f}, {self.velocity.y:.2f})")
