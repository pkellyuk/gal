from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

app = Ursina()

# Enable physics
from ursina.prefabs.first_person_controller import FirstPersonController

# Create a grid textured floor with proper physics collision
floor = Entity(
    model='cube',
    scale=(20,1,20),
    color=color.white,
    texture='white_cube',
    texture_scale=(20,20),
    position=(0,-0.5,0),
    collider='box',
    friction=0.5
)
# Add grid lines
for i in range(-10, 11):
    Entity(model='quad', scale=(0.01, 1, 20), color=color.gray, position=(i,0.01,0))
    Entity(model='quad', scale=(20, 1, 0.01), color=color.gray, rotation=(90,0,0), position=(0,0.01,i))

# Create player
player = FirstPersonController(position=(0, 2, -5))

def create_falling_cube():
    # Create a cube with random color at camera's position
    colors = [color.red, color.blue, color.green, color.yellow, color.orange, color.magenta]
    
    # Calculate spawn position with fixed height from ground
    spawn_pos = player.position + player.forward * 2  # Get position 2 units in front
    spawn_pos.y = 3.0  # Higher fixed height from ground for better visibility
    
    # Create physics cube
    new_cube = Entity(
        model='cube',
        color=random.choice(colors),
        scale=(1,1,1),
        position=spawn_pos,
        collider='box'
    )
    
    # Enable physics
    new_cube.rigidbody = True
    
    # Add initial velocity and rotation
    throw_direction = player.forward.normalized()
    new_cube.dy = 2  # Initial upward velocity
    new_cube.dx = throw_direction.x * 5  # Forward velocity x
    new_cube.dz = throw_direction.z * 5  # Forward velocity z
    
    # Add slight random rotation for natural movement
    new_cube.rotation = Vec3(
        random.uniform(-15, 15),
        random.uniform(-15, 15),
        random.uniform(-15, 15)
    )

def input(key):
    if key == 'escape':
        mouse.locked = not mouse.locked
    if key == 'left mouse down':
        create_falling_cube()

def update():
    # Apply physics to all cubes
    for entity in scene.entities:
        if hasattr(entity, 'rigidbody') and entity.rigidbody:
            # Apply gravity
            if not hasattr(entity, 'dy'):
                entity.dy = 0
            entity.dy -= 20 * time.dt  # Gravity acceleration
            
            # Update position
            entity.y += entity.dy * time.dt
            if hasattr(entity, 'dx'):
                entity.x += entity.dx * time.dt
            if hasattr(entity, 'dz'):
                entity.z += entity.dz * time.dt
            
            # Floor collision
            if entity.y < 0.5:  # Cube height is 1, so bottom at 0.5
                entity.y = 0.5
                if entity.dy < 0:  # Only bounce if moving downward
                    entity.dy = -entity.dy * 0.6  # Bounce with energy loss
                    # Apply friction to horizontal movement
                    if hasattr(entity, 'dx'):
                        entity.dx *= 0.8
                    if hasattr(entity, 'dz'):
                        entity.dz *= 0.8

app.run()
