from ursina import Ursina, Entity, scene, time, color, mouse, window
from entities import create_floor, create_grid
from player import GamePlayer
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class Game(Entity):
    #==============================
    def __init__(self):
        """Initialize the game."""
        logging.debug("Initializing game...")
        # Create Ursina instance first with physics enabled
        self.app = Ursina()
        logging.debug("Created Ursina instance")
        window.vsync = True  # Disable vsync for physics performance
        logging.debug("Disabled vsync for physics performance")
        window.color = color.black  # Set sky/background color to black
        logging.debug("Set sky/background color to black")
        scene.physics = True  # Enable Bullet physics engine
        logging.debug("Enabled Bullet physics engine")
        scene.gravity = (0, -9.81, 0)  # Set gravity in m/s^2
        logging.debug("Set gravity to (0, -9.81, 0)")
        scene.physics_substeps = 10  # Increase physics accuracy
        logging.debug("Increased physics accuracy with 10 substeps")
        # Initialize entity after Ursina instance
        super().__init__(eternal=True)  # Make sure entity persists
        logging.debug("Initialized entity")
        
        # Create environment
        self.floor = create_floor()
        logging.debug("Created floor")
        self.grid = create_grid()
        logging.debug("Created grid")

        # Create player
        self.player = GamePlayer()
        logging.debug("Created player")
        
        # Set up initial state and handlers
        mouse.locked = True
        logging.debug("Locked mouse")
        mouse.visible = False
        logging.debug("Hid mouse cursor")
        self.app.update = self.update
        logging.debug("Set up update handler")

    #==============================
    def input(self, key):
        """Handle input events."""
        logging.debug(f"Received input event: {key}")
        if key == 'escape':
            # Toggle mouse state
            mouse.locked = not mouse.locked
            logging.debug(f"Toggled mouse locked state to {mouse.locked}")
            mouse.visible = not mouse.visible
            logging.debug(f"Toggled mouse visible state to {mouse.visible}")
        elif key in ['left mouse down', 'right mouse down']:
            # Forward all mouse inputs to player
            self.player.handle_input(key)
            logging.debug(f"Forwarded mouse input to player: {key}")

    #==============================
    def update(self):
        """Update game state each frame."""
        logging.debug("Updating game state...")
        pass  # Physics is now handled by Bullet engine
        logging.debug("Updated game state")

    #==============================
    def run(self):
        """Start the game."""
        logging.debug("Starting game...")
        self.app.run()
        logging.debug("Game started")

if __name__ == '__main__':
    game = Game()
    logging.debug("Created game instance")
    game.run()