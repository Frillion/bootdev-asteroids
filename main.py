import pygame
from shot import Shot
from asteroidfield import *
from asteroid import *
from player import Player
from constants import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time = pygame.time.Clock()
    delta_time = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = (updatable)
    Asteroid.containers = (updatable, drawable, asteroids) 
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, drawable, updatable)

    player = Player(x, y)
    asteroid_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0,0))
        for obj in updatable:
            obj.update(delta_time)

        for obj in drawable:
            obj.draw(screen)
        
        for obj in asteroids:
            if obj.is_colliding(player):
                print("Game over!")
                return 

        pygame.display.flip()
        delta_time = time.tick(60)/1000

if __name__ == "__main__":
    main()
