from ursina import Entity, time
from ursina.vec3 import Vec3
import random
from config import (
    CUBE_COLORS, CUBE_SCALE, CUBE_THROW_FORCE, 
    CUBE_INITIAL_UP_VELOCITY, CUBE_ROTATION_RANGE
)

class ThrowableTriangle(Entity):
    """A triangle that can be thrown and affected by physics."""
    
    #==============================
    def __init__(self, spawn_position, throw_direction):
        super().__init__(
            model='quad',
            color=random.choice(CUBE_COLORS),
            scale=CUBE_SCALE,
            position=spawn_position,
            collider='box'
        )
        
        # Physics properties
        self.velocity = throw_direction * CUBE_THROW_FORCE + Vec3(0, CUBE_INITIAL_UP_VELOCITY, 0)
        self.gravity = Vec3(0, -9.81, 0)
        self.rotation_speed = Vec3(
            random.uniform(*CUBE_ROTATION_RANGE),
            random.uniform(*CUBE_ROTATION_RANGE),
            random.uniform(*CUBE_ROTATION_RANGE)
        )
        
    #==============================
    def update(self):
        """Update triangle physics each frame."""
        dt = time.dt
        
        # Update position based on velocity
        self.position += self.velocity * dt
        
        # Apply gravity to velocity
        self.velocity += self.gravity * dt
        
        # Update rotation
        self.rotation += self.rotation_speed * dt
        
        # Check for collisions with other entities
        hit_info = self.intersects()
        if hit_info.hit:
            # Move back to prevent intersection
            self.position -= self.velocity * dt
            
            # Calculate reflection: v - 2(v�n)n
            normal = hit_info.world_normal
            dot_product = self.velocity.dot(normal)
            reflection = self.velocity - (normal * 2 * dot_product)
            self.velocity = reflection * 0.8  # 0.8 is bounce factor
            
            # Reduce rotation speed on collision
            self.rotation_speed *= 0.9

def create_throwable_triangle(spawn_position, throw_direction):
    """Create and return a new throwable triangle instance."""
    return ThrowableTriangle(spawn_position, throw_direction)
