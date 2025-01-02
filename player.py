from ursina import mouse, Vec3, time
from ursina.prefabs.first_person_controller import FirstPersonController
from entities import create_throwable_cube
from config import CUBE_SPAWN_HEIGHT

class GamePlayer:
    def __init__(self, start_position=(0, 2, -5)):
        """Initialize the player with first person controller."""
        self.controller = FirstPersonController(position=start_position)
        # Invert mouse Y-axis by setting negative Y sensitivity
        self.controller.mouse_sensitivity = Vec3(-40, 40, 40)
    
    def throw_cube(self):
        """Create and throw a cube from player's position."""
        # Calculate spawn position
        spawn_pos = self.controller.position + self.controller.forward * 2
        spawn_pos.y = CUBE_SPAWN_HEIGHT
        
        # Create cube with throw direction and store it
        create_throwable_cube(
            spawn_position=spawn_pos,
            throw_direction=self.controller.forward.normalized()
        )
    
    def handle_input(self, key):
        """Handle player input."""
        if key == 'left mouse down' and mouse.locked:  # Only throw when mouse is locked
            self.throw_cube()
