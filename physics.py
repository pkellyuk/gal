from ursina import time
from config import GRAVITY, BOUNCE_FACTOR, FRICTION

def apply_physics(entity, dt):
    """Apply physics calculations to an entity."""
    if not hasattr(entity, 'rigidbody') or not entity.rigidbody:
        return

    # Initialize physics attributes if they don't exist
    if not hasattr(entity, 'dy'):
        entity.dy = 0
    if not hasattr(entity, 'dx'):
        entity.dx = 0
    if not hasattr(entity, 'dz'):
        entity.dz = 0
    
    # Apply gravity
    entity.dy -= GRAVITY * dt
    
    # Update position
    entity.y += entity.dy * dt
    entity.x += entity.dx * dt
    entity.z += entity.dz * dt
    
    # Floor collision
    if entity.y < 0.5:  # Cube height is 1, so bottom at 0.5
        entity.y = 0.5
        if entity.dy < 0:  # Only bounce if moving downward
            entity.dy = -entity.dy * BOUNCE_FACTOR
            # Apply friction to horizontal movement
            entity.dx *= FRICTION
            entity.dz *= FRICTION
            
            # Stop very small movements
            if abs(entity.dy) < 0.1:
                entity.dy = 0
            if abs(entity.dx) < 0.1:
                entity.dx = 0
            if abs(entity.dz) < 0.1:
                entity.dz = 0
