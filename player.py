import pygame
from circleshape import *
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0 

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + ( forward * self.radius )
        b = self.position - ( forward * self.radius ) - right
        c = self.position - ( forward * self.radius ) + right
        return [a, b, c]

    def shoot(self):
        if self.timer > 0:
            shot = Shot(self.position.x, self.position.y)
            unit = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            shot.velocity = unit

        self.timer = PLAYER_SHOT_COOLDOWN

    def rotate(self, delta_time):
        self.rotation += delta_time * PLAYER_TURN_SPEED

    def update(self, delta_time):
        keys = pygame.key.get_pressed()
        self.timer -= delta_time        

        if keys[pygame.K_SPACE]:
            self.shoot()

        if keys[pygame.K_a]:
           self.rotate(-delta_time) 

        if keys[pygame.K_d]:
           self.rotate(delta_time) 
        
        if keys[pygame.K_w]:
            self.move(delta_time)

        if keys[pygame.K_s]:
            self.move(-delta_time)

    def move(self, delta_time):
        unit = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += unit * PLAYER_SPEED * delta_time

    def draw(self, screen):
        pygame.draw.polygon(screen, pygame.Color(255,255,255), self.triangle(), 2)

