from ursina import Entity, Vec3, random, color, time, Text, camera, window, Button, ButtonList
from config import (
    FLOOR_SCALE, FLOOR_POSITION, FLOOR_FRICTION,
    CUBE_COLORS, CUBE_SCALE, CUBE_SPAWN_HEIGHT,
    CUBE_THROW_FORCE, CUBE_INITIAL_UP_VELOCITY, CUBE_ROTATION_RANGE,
    GRID_SIZE, GRID_LINE_SCALE_VERTICAL, GRID_LINE_SCALE_HORIZONTAL, GRID_COLOR
)

#==============================
def create_floor():
    """Create the game floor with physics."""
    return Entity(
        model='cube',
        scale=FLOOR_SCALE,
        color=color.white,
        texture='white_cube',
        texture_scale=(100,100),
        position=FLOOR_POSITION,
        rotation_x=180,  # Flip the floor over
        collider='box',
        rigidbody=True,
        mass=0,  # Zero mass makes it static/immovable
        friction=FLOOR_FRICTION,
        restitution=0.3
    )

#==============================
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