import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random


class Asteroid(CircleShape):

    containers = None

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)


    def update(self, dt):
        self.position += self.velocity * dt

    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        # Generate a random angle for the direction new asteroids will travel
        angle = random.uniform(20,50)
        #Set the vector for both new asteroids to be opposite one another
        vect1 = pygame.Vector2(self.velocity).rotate(angle)
        vect2 = pygame.Vector2(self.velocity).rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        # Create 2 new asteroids from the original 
        split1 = Asteroid(0,0, new_radius)
        split1.position = pygame.Vector2(self.position)
        split1.velocity = vect1 * 1.2
        split2 = Asteroid(0,0, new_radius)
        split2.position = pygame.Vector2(self.position)
        split2.velocity = vect2 * 1.2
