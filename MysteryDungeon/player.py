# IMPORTANT: The exact import paths (e.g., py4godot.classes.CharacterBody2D) 
# may vary slightly depending on your specific Python4Godot version and Godot 
# version (3.x vs 4.x). If you see an error, check the py4godot documentation
# for the precise location of the CharacterBody2D class.

# Import core classes used for movement and input
from py4godot.classes.core import Vector2
from py4godot.classes.CharacterBody2D import CharacterBody2D # Assuming this path
from py4godot.classes.Input import Input # Assuming this path

# NEW: Import gdproperty to expose variables to the Inspector
from py4godot import gdproperty 

# Note: The older py4godot usually requires classes to be manually extended.
# No @gdclass decorator is typically needed for extending engine classes.

class Player(CharacterBody2D):
	"""
	Python script for a 2D top-down character using the older py4godot library structure.
	Uses simple, snappy movement (zero friction/deceleration).
	"""

	# --- Configuration Variables (Exported Metadata) ---
	# This exposes 'speed' to the Godot Inspector.
	# NOTE: Ensure the gdproperty call is completely closed with ')' at the end.
	speed: float = gdproperty(float, 300.0)

	# Internal variable to hold the Input singleton instance
	input_instance: Input = None 

	# --- Godot Lifecycle Methods ---

	def _init(self) -> None:
		"""
		Added for compatibility. Older py4godot often requires an explicit
		initialization method for proper class registration.
		"""
		pass

	def _ready(self) -> None:
		"""
		Called when the node is ready. Accesses and demonstrates node metadata.
		"""
		print("Player script is ready. Using simple movement.")
		
		# --- API Documentation Change: Access Input Singleton ---
		# Per the py4godot documentation, singletons should be accessed via get_instance().
		self.input_instance = Input.get_instance()
		
		# ----------------------------------------------------
		# 1. SETTING ARBITRARY METADATA (Editor or Runtime)
		# This metadata is saved with the scene.
		self.set_meta("character_type", "Protagonist")
		self.set_meta("initial_health", 100)
		# ----------------------------------------------------

		# Accessing Standard Metadata: Node Name and Path
		node_name = self.get_name()
		node_path = self.get_path() 
		
		# ----------------------------------------------------
		# 2. RETRIEVING METADATA
		char_type = self.get_meta("character_type")
		initial_hp = self.get_meta("initial_health")
		# ----------------------------------------------------

		print(f"--- Node Metadata ---")
		print(f"Node Name: {node_name}")
		print(f"Scene Path: {node_path}")
		print(f"Exported Speed: {self.speed}")
		print(f"Custom Meta: Type='{char_type}', HP='{initial_hp}'")
		print("---------------------")

		# Initialize velocity to a zero vector.
		self.velocity = Vector2(0, 0)

	def _physics_process(self, delta: float) -> None:
		"""
		Called every physics frame. Handles movement input and physics.
		"""
		# 1. Get raw input direction as a normalized Vector2 using the instance.
		
		# NOTE: We now use self.input_instance instead of the static Input class.
		input_x = (self.input_instance.get_action_strength("ui_right") - 
				   self.input_instance.get_action_strength("ui_left"))
		input_y = (self.input_instance.get_action_strength("ui_down") - 
				   self.input_instance.get_action_strength("ui_up"))

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
