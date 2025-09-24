import sys

import pygame

from constants import *

from player import *

from asteroidfield import *

from Asteroid import *

from shot import Shot

def main():
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	pygame.init()
	shots = pygame.sprite.Group()
	space_rock = pygame.sprite.Group()
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	AsteroidField.containers = (updatable)
	Asteroid.containers = (space_rock, updatable, drawable)
	Player.containers = (updatable, drawable)
	Shot.containers = (shots, updatable, drawable)
	clock = pygame.time.Clock()
	dt = 0
	x = (SCREEN_WIDTH / 2)
	y = (SCREEN_HEIGHT / 2)
	player = Player(x, y, PLAYER_RADIUS)
	field = AsteroidField()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			dt = (clock.tick(60)/1000)
			screen.fill((0, 0, 0))
			updatable.update(dt)
			for thing in drawable:
				thing.draw(screen)
			for rock in space_rock:
				rock.collide(player)
				if rock.collide(player) == True:
					print("Game over!")
					sys.exit()
				else:
					continue
			for rock in space_rock:
				for shot in shots:
					rock.collide(shot)
					if rock.collide(shot) == True:
						rock.split()
						shot.kill()
					else:
						continue
			pygame.display.flip()
			clock.tick(60)

if __name__ == "__main__":
    main()
