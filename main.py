# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        main_screen = pygame.display.get_surface()
        main_screen.fill((0,0,0))

        # update
        updatable.update(dt)

        # collision
        for thing in asteroids:
            if(thing.check_collision(player)):
                print("Game over!")
                exit()
            for shot in shots:
                if(thing.check_collision(shot)):
                    shot.kill()
                    thing.split()


        # Render
        for thing in drawable:
            thing.draw(main_screen)
        
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()