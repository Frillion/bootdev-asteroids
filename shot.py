from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color(200,200,200), self.position, self.radius, 2)

    def update(self, delta_time):
        self.position += self.velocity * delta_time
