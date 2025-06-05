# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Add all players into updatable and drawable containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)

    # Initialization Code
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for u in updatable:
            u.update(dt)
        for d in drawable:
            d.draw(screen)
        for i in asteroids:
            if i.check_collision(player):
                print("Game Over!")
                return

        pygame.display.flip()
        dt = clock.tick(60) / 1000 #60 fps


if __name__ == "__main__":
    main()
