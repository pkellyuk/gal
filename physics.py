from ursina import time, Vec3, distance, scene
import random
from config import GRAVITY, BOUNCE_FACTOR, FRICTION

def init_physics_attributes(entity):
    """Initialize physics attributes for an entity."""
    if not hasattr(entity, 'dy'): entity.dy = 0
    if not hasattr(entity, 'dx'): entity.dx = 0
    if not hasattr(entity, 'dz'): entity.dz = 0
    if not hasattr(entity, 'angular_velocity'): entity.angular_velocity = Vec3(0,0,0)
    if not hasattr(entity, 'energy'): entity.energy = 0

def check_cube_collision(entity1, entity2):
    """Check and handle collision between two cubes."""
    if not (hasattr(entity1, 'rigidbody') and hasattr(entity2, 'rigidbody')):
        return False
        
    # Simple sphere collision detection for performance
    if distance(entity1.position, entity2.position) < 1.0:  # Cube size is 1
        return True
    return False

def resolve_collision(entity1, entity2):
    """Handle collision physics between two entities."""
    # Calculate collision normal
    normal = (entity2.position - entity1.position).normalized()
    
    # Separate the objects
    overlap = 1.0 - distance(entity1.position, entity2.position)
    if overlap > 0:
        entity1.position -= normal * (overlap/2)
        entity2.position += normal * (overlap/2)
    
    # Calculate relative velocity
    rel_vel = Vec3(
        entity2.dx - entity1.dx,
        entity2.dy - entity1.dy,
        entity2.dz - entity1.dz
    )
    
    # Conservation of momentum and energy
    velocity_along_normal = rel_vel.dot(normal)
    if velocity_along_normal > 0:
        return
    
    restitution = BOUNCE_FACTOR
    j = -(1 + restitution) * velocity_along_normal / 2  # Assume equal mass
    
    # Apply impulse
    impulse = normal * j
    entity1.dx -= impulse.x
    entity1.dy -= impulse.y
    entity1.dz -= impulse.z
    entity2.dx += impulse.x
    entity2.dy += impulse.y
    entity2.dz += impulse.z
    
    # Transfer angular momentum
    entity1.angular_velocity += Vec3(
        random.uniform(-1, 1),
        random.uniform(-1, 1),
        random.uniform(-1, 1)
    ) * velocity_along_normal * 0.5
    entity2.angular_velocity += Vec3(
        random.uniform(-1, 1),
        random.uniform(-1, 1),
        random.uniform(-1, 1)
    ) * velocity_along_normal * 0.5

def apply_physics(entity, dt):
    """Apply physics calculations to an entity."""
    if not hasattr(entity, 'rigidbody') or not entity.rigidbody:
        return

    init_physics_attributes(entity)
    
    # Store initial energy
    initial_energy = (
        abs(entity.dx) + abs(entity.dy) + abs(entity.dz) +
        abs(entity.angular_velocity.x) + abs(entity.angular_velocity.y) + abs(entity.angular_velocity.z)
    )
    
    # Apply gravity
    entity.dy -= GRAVITY * dt
    
    # Update position
    entity.y += entity.dy * dt
    entity.x += entity.dx * dt
    entity.z += entity.dz * dt
    
    # Update rotation based on angular velocity
    entity.rotation_x += entity.angular_velocity.x * dt * 57.2958  # Convert to degrees
    entity.rotation_y += entity.angular_velocity.y * dt * 57.2958
    entity.rotation_z += entity.angular_velocity.z * dt * 57.2958
    
    # Floor collision with rotation
    if entity.y < 0.5:  # Cube height is 1, so bottom at 0.5
        entity.y = 0.5
        if entity.dy < 0:  # Only bounce if moving downward
            # Convert some vertical energy into rotation
            rotation_energy = abs(entity.dy) * 0.3
            entity.dy = -entity.dy * BOUNCE_FACTOR
            
            # Add rotation based on horizontal movement
            entity.angular_velocity = Vec3(
                entity.dz * rotation_energy,
                0,
                -entity.dx * rotation_energy
            )
            
            # Apply friction to horizontal movement
            entity.dx *= FRICTION
            entity.dz *= FRICTION
            
            # Dampen angular velocity
            entity.angular_velocity *= FRICTION
            
            # Stop very small movements
            if abs(entity.dy) < 0.1: entity.dy = 0
            if abs(entity.dx) < 0.1: entity.dx = 0
            if abs(entity.dz) < 0.1: entity.dz = 0
            if entity.angular_velocity.length() < 0.1: entity.angular_velocity = Vec3(0,0,0)
    
    # Check collisions with other cubes
    for other in scene.entities:
        if other != entity and hasattr(other, 'rigidbody') and other.rigidbody:
            if check_cube_collision(entity, other):
                resolve_collision(entity, other)
    
    # Update entity's energy
    entity.energy = (
        abs(entity.dx) + abs(entity.dy) + abs(entity.dz) +
        abs(entity.angular_velocity.x) + abs(entity.angular_velocity.y) + abs(entity.angular_velocity.z)
    )
