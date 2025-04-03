# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    af = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Player.containers = (updateable, drawable)
    player = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)    
    Clock = pygame.time.Clock()
    dt = 0
    while 0 < 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, color=(0,0,0))
        for thing in drawable:
            thing.draw(screen)
        updateable.update(dt)
        for asteroid in asteroids:
            if asteroid.isColliding(player) == True:
                sys.exit("Game over!")
            for shot in shots:
                if asteroid.isColliding(shot) == True:
                    asteroid.split()
        pygame.display.flip()
        dt = Clock.tick(60)/1000

if __name__ == "__main__":
    main()

