import pygame
import sys
from constants import *
from player import Player
from asteroidfield import * 
from asteroid import Asteroid
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")  
    clock = pygame.time.Clock()

    dt = 0
    asteroids = pygame.sprite.Group() 
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group() # here
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable) 
    AsteroidField.containers = (updatable,) 
    Shot.containers = (shots, updatable, drawable) #here
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    asteroid_field = AsteroidField() 
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        dt = clock.tick(60) / 1000
        updatable.update(dt)
        
        for obj in drawable:
 	        obj.draw(screen)

        pygame.display.flip()
        
        for asteroid in asteroids: 
            if asteroid.collision(player):
                print(f"Collision detected between asteroid and player at {asteroid.rect.topleft}")
                print("Game Over!")
                pygame.quit()
                sys.exit()

            for shot in shots:
                if asteroid.collision(shot):
                    print(f"Shot hit asteroid at {asteroid.rect.topleft}")
                    shot.kill()
                    asteroid.split()
    
if __name__ == "__main__":
    main()
    pygame.quit()
