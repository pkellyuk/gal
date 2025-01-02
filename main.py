from ursina import Ursina, Entity, scene, time, color, mouse
from entities import create_floor, create_grid
from player import GamePlayer
from physics import apply_physics

class Game(Entity):
    def __init__(self):
        """Initialize the game."""
        # Create Ursina instance first
        self.app = Ursina()
        
        # Initialize entity after Ursina instance
        super().__init__(eternal=True)  # Make sure entity persists
        
        # Create environment
        self.floor = create_floor()
        self.grid = create_grid()
        
        # Create player
        self.player = GamePlayer()
        
        # Set up initial state and handlers
        mouse.locked = True
        mouse.visible = False
        self.app.update = self.update
    
    def input(self, key):
        """Handle input events."""
        if key == 'escape':
            # Toggle mouse state
            mouse.locked = not mouse.locked
            mouse.visible = not mouse.visible
        elif key == 'left mouse down':
            # Only forward to player when mouse is locked (game mode)
            self.player.handle_input(key)
    
    def update(self):
        """Update game state each frame."""
        # Apply physics to all entities
        for entity in scene.entities:
            apply_physics(entity, time.dt)
    
    def run(self):
        """Start the game."""
        self.app.run()

if __name__ == '__main__':
    game = Game()
    game.run()
