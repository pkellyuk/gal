from ursina import color, Vec3

# Physics constants
GRAVITY = 20
BOUNCE_FACTOR = 0.6
FRICTION = 0.8

# Floor settings
FLOOR_SCALE = (20, 1, 20)
FLOOR_POSITION = (0, -0.5, 0)
FLOOR_FRICTION = 0.5

# Cube settings
CUBE_COLORS = [color.red, color.blue, color.green, color.yellow, color.orange, color.magenta]
CUBE_SCALE = (1, 1, 1)
CUBE_SPAWN_HEIGHT = 3.0
CUBE_THROW_FORCE = 5
CUBE_INITIAL_UP_VELOCITY = 2
CUBE_ROTATION_RANGE = (-15, 15)

# Grid settings
GRID_SIZE = 10
GRID_LINE_SCALE_VERTICAL = (0.01, 1, 20)
GRID_LINE_SCALE_HORIZONTAL = (20, 1, 0.01)
GRID_COLOR = color.gray
