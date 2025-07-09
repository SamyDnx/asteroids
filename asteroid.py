from circleshape import CircleShape

from constants import *

import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color(255,255,255), (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        base_angle = random.uniform(20, 50)
        angle1 = self.velocity.rotate(base_angle)
        angle2 = self.velocity.rotate(-base_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        aster1 = Asteroid(self.position.x, self.position.y, new_radius)
        aster2 = Asteroid(self.position.x, self.position.y, new_radius)

        aster1.velocity = angle1 * 1.2
        aster2.velocity = angle2 * 1.2
