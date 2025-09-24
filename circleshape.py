import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collide(self, CircleShape):
        r1 = self.radius
        r2 = CircleShape.radius
        pos1 = self.position
        pos2 = CircleShape.position
        roche_limit = (r1 + r2)
        if pygame.math.Vector2.distance_to(pos1, pos2) <= roche_limit:
            return True
