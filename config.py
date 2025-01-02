from ursina import color, Vec3

# Physics constants
GRAVITY = 15  # Slightly reduced for more natural falling
BOUNCE_FACTOR = 0.3  # Lower for less bouncy, more realistic cubes
FRICTION = 0.95  # Higher friction to help cubes settle

# Floor settings
FLOOR_SCALE = (20, 1, 20)
FLOOR_POSITION = (0, -0.5, 0)
FLOOR_FRICTION = 0.5

# Cube settings
CUBE_COLORS = [color.red, color.blue, color.green, color.yellow, color.orange, color.magenta]
CUBE_SCALE = (1, 1, 1)
CUBE_SPAWN_HEIGHT = 3.0
CUBE_THROW_FORCE = 8  # Increased for better throwing feel
CUBE_INITIAL_UP_VELOCITY = 3  # Slightly increased for better arc
CUBE_ROTATION_RANGE = (-15, 15)

# Grid settings
GRID_SIZE = 10
GRID_LINE_SCALE_VERTICAL = (0.01, 1, 20)
GRID_LINE_SCALE_HORIZONTAL = (20, 1, 0.01)
GRID_COLOR = color.gray
