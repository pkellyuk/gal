from ursina import Entity, Vec3, random, color
from config import (
    FLOOR_SCALE, FLOOR_POSITION, FLOOR_FRICTION,
    CUBE_COLORS, CUBE_SCALE, CUBE_SPAWN_HEIGHT,
    CUBE_THROW_FORCE, CUBE_INITIAL_UP_VELOCITY, CUBE_ROTATION_RANGE,
    GRID_SIZE, GRID_LINE_SCALE_VERTICAL, GRID_LINE_SCALE_HORIZONTAL, GRID_COLOR
)

def create_floor():
    """Create the game floor with collision."""
    return Entity(
        model='cube',
        scale=FLOOR_SCALE,
        color=color.white,
        texture='white_cube',
        texture_scale=(20,20),
        position=FLOOR_POSITION,
        rotation_x=180,  # Flip the floor over
        collider='box',
        friction=FLOOR_FRICTION
    )

def create_grid():
    """Create grid lines on the floor."""
    grid_entities = []
    for i in range(-GRID_SIZE, GRID_SIZE + 1):
        # Vertical lines
        grid_entities.append(
            Entity(
                model='quad',
                scale=GRID_LINE_SCALE_VERTICAL,
                color=GRID_COLOR,
                position=(i, -0.01, 0),
                rotation_x=180
            )
        )
        # Horizontal lines
        grid_entities.append(
            Entity(
                model='quad',
                scale=GRID_LINE_SCALE_HORIZONTAL,
                color=GRID_COLOR,
                rotation=(270, 0, 0),
                position=(0, -0.01, i)
            )
        )
    return grid_entities

def create_throwable_cube(spawn_position, throw_direction):
    """Create a physics-enabled cube that can be thrown."""
    new_cube = Entity(
        model='cube',
        color=random.choice(CUBE_COLORS),
        scale=CUBE_SCALE,
        position=spawn_position,
        collider='box'
    )
    
    # Enable physics and initialize attributes
    new_cube.rigidbody = True
    new_cube.dy = CUBE_INITIAL_UP_VELOCITY
    new_cube.dx = throw_direction.x * CUBE_THROW_FORCE
    new_cube.dz = throw_direction.z * CUBE_THROW_FORCE
    new_cube.angular_velocity = Vec3(0, 0, 0)
    new_cube.energy = 0
    
    # Add random rotation
    new_cube.rotation = Vec3(
        random.uniform(*CUBE_ROTATION_RANGE),
        random.uniform(*CUBE_ROTATION_RANGE),
        random.uniform(*CUBE_ROTATION_RANGE)
    )
    
    return new_cube
