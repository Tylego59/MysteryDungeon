from godot_toolkit.native_interface import (
	Node, CharacterBody2D, Vector2, Input, move_toward
)

class Player(CharacterBody2D):
	speed: float = 300.0
	
	def _ready(self) -> None:
		"""
		Called when the node and its children have entered the scene tree.
		"""
		print("Player script is ready. Speed:", self.speed)
		
		# Initialize velocity to a zero vector
		self.velocity = Vector2.ZERO
	
	def _physics_process(self, delta: float) -> None:
		input_vector: Vector2 = Input.get_vector("right", "left", "up", "down")
		
		if input_vector != Vector2.ZERO:
			self.velocity = input_vector.normalized() * self.speed
		else:
			self.velocity.x = move_toward(self.velocity.x, 0, self.speed * delta)
			self.velocity.y = move_toward(self.velocity.y, 0, self.speed * delta)
			
		self.move_and_slide()
