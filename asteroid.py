from circleshape import * 
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius , 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        random_angle = random.uniform(20, 50)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        vel_a = self.velocity.rotate(random_angle) * 1.2
        vel_b = self.velocity.rotate(-random_angle) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_aster_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_aster_1.velocity = vel_a 
        new_aster_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_aster_2.velocity = vel_b 