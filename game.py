import logging
from ursina import Entity, window, scene
from entities import create_floor, create_grid
from player import GamePlayer

class Game(Entity):
    def __init__(self):
        """Initialize the game."""
        # Create Ursina instance first with physics enabled
        self.app = Ursina()
        window.vsync = True  # Disable vsync for physics performance
        window.color = color.black  # Set sky/background color to black
        scene.physics = True  # Enable Bullet physics engine
        scene.gravity = (0, -9.81, 0)  # Set gravity in m/s^2
        scene.physics_substeps = 10  # Increase physics accuracy
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
        logging.debug("Input received: %s", key)
        if key == 'escape':
            # Toggle mouse state
            mouse.locked = not mouse.locked
            mouse.visible = not mouse.visible
        elif key in ['left mouse down', 'right mouse down']:
            # Forward all mouse inputs to player
            self.player.handle_input(key)
    
    def update(self):
        """Update game state each frame."""
        logging.debug("Game update called.")
        pass  # Physics is now handled by Bullet engine

    def run(self):
        """Start the game."""
        self.app.run()

if __name__ == '__main__':
    game = Game()
    game.run()
